from flask import Flask, request, jsonify,  Blueprint
import requests
from io import StringIO
from flask_cors import CORS
import pandas as pd
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from app import db
from app.models.user import User
from app.models.game import Game
import random
from datetime import datetime
from datetime import datetime, timezone
from sqlalchemy import and_ 


game_bp = Blueprint('game', __name__)

@game_bp.route('/home', methods=['GET'])
def home():
    return jsonify({'message': 'Hello, World!'})


   
@game_bp.route('/upload_csv', methods=['POST'])
def upload_csv():
    try:
        data = request.json
        username = data['username']
        csv_link = data['csv_url']

        # Check if user exists, if not create a new user
        user = User.query.filter_by(username=username).first()
        if not user:
            user = User(username=username)
            db.session.add(user)
            db.session.commit()  
        user_id = user.id

        # Fetch CSV data from the link
        response = requests.get(csv_link)
        if response.status_code != 200:
            return jsonify({"error": "Failed to fetch CSV"}), 400
        
        csv_content = StringIO(response.text)
        csv_data = pd.read_csv(csv_content)
        for col in csv_data.columns:
            if csv_data[col].dtype == 'float64' or csv_data[col].dtype == 'int64':
        # Fill numeric columns with 0
                csv_data[col] = csv_data[col].fillna(0)
            else:
        # Fill non-numeric columns with an empty string
                csv_data[col] = csv_data[col].fillna("").replace(r'^\s*$', "", regex=True)
        
        required_columns = ['AppID', 'Name', 'Release date', 'Required age', 'Price', 'DLC count', 'About the game', 
                            'Supported languages', 'Windows', 'Mac', 'Linux', 'Positive', 'Negative', 
                            'Score rank', 'Developers', 'Publishers', 'Categories', 'Genres', 'Tags']
        
        # if not all(col in csv_data.columns for col in required_columns):
        #     return jsonify({"error": "CSV missing required columns"}), 400

        games_to_add = []

        for index, row in csv_data.iterrows():
            # Check if the game already exists for the user
            game = Game.query.filter_by(user_id=user_id, app_id=row['AppID']).first()
            
            if game:
                # Update existing game entry
                game.name = row['Name']
                game.release_date = row['Release date']
                game.required_age = row['Required age']
                game.price = row['Price']
                game.dlc_count = row['DLC count']
                game.about_game = row['About the game']
                game.supported_languages = row['Supported languages']
                game.windows = row['Windows']
                game.mac = row['Mac']
                game.linux = row['Linux']
                game.positive_reviews = row['Positive']
                game.negative_reviews = row['Negative']
                game.score_rank = row['Score rank']
                game.developer = row['Developers']
                game.publisher = row['Publishers']
                game.categories = row['Categories']
                game.genres = row['Genres']
                game.tags = row['Tags']
                game.uploaded_at = datetime.now(timezone.utc)  
            else:
               
                game = Game(
                    user_id=user_id,
                    app_id=row['AppID'],
                    name=row['Name'],
                    release_date=row['Release date'],
                    required_age=row['Required age'],
                    price=row['Price'],
                    dlc_count=row['DLC count'],
                    about_game=row['About the game'],
                    supported_languages=row['Supported languages'],
                    windows=row['Windows'],
                    mac=row['Mac'],
                    linux=row['Linux'],
                    positive_reviews=row['Positive'],
                    negative_reviews=row['Negative'],
                    score_rank= row['Score rank'],
                    developer=row['Developers'],
                    publisher=row['Publishers'],
                    categories=row['Categories'],
                    genres=row['Genres'],
                    tags=row['Tags'],
                    uploaded_at=datetime.now(timezone.utc)
                )
                games_to_add.append(game)
        
        
        if games_to_add:
            db.session.add_all(games_to_add)

        # Commit all changes
        db.session.commit()

        return jsonify({"message": "CSV data processed successfully"}), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@game_bp.route('/<username>', methods=['GET'])
def get_games_by_username(username):
    user = User.query.filter_by(username=username).first()

    if user:
        games = Game.query.filter_by(user_id=user.id).all()
        game_list = []
        
        for game in games:
            game_list.append({
                'app_id': game.app_id,
                'name': game.name,
                'release_date': game.release_date,
                'required_age': game.required_age,
                'price': game.price,
                'dlc_count': game.dlc_count,
                'about_game': game.about_game,
                'supported_languages': game.supported_languages,
                'windows': game.windows,
                'mac': game.mac,
                'linux': game.linux,
                'positive_reviews': game.positive_reviews,
                'negative_reviews': game.negative_reviews,
                'score_rank': game.score_rank,
                'developers': game.developer,
                'publishers': game.publisher,
                'categories': game.categories,
                'genres': game.genres,
                'tags': game.tags
            })
        
        return jsonify({'username': user.username, 'games': game_list}), 200
    else:
        return jsonify({'message': 'User not found'}), 404


def convert_to_datetime(date_string):
    """Convert string like 'Oct 21, 2008' to datetime"""
    try:
        return datetime.strptime(date_string, '%b %d, %Y')
    except ValueError:
        return None

@game_bp.route('/api/searchGames', methods=['POST'])
def search_games():

    data = request.json
    username = data['username']
    user = User.query.filter_by(username=username).first()

    filters = []
    
    # Filters for specific parameters
    if 'username' in data:
        filters.append(Game.user_id == user.id)

    if 'app_id' in data:
        filters.append(Game.app_id == data['app_id'])
    
    if 'name' in data:
        if data.get('name_condition') == 'contains':
            filters.append(Game.name.ilike(f"%{data['name']}%"))
        else:
            filters.append(Game.name == data['name'])
    
    if 'release_date' in data:
        release_date = convert_to_datetime(data['release_date'])
        if release_date:
            if data.get('release_date_condition') == '>':
                filters.append(db.func.to_date(Game.release_date, 'Mon DD, YYYY') > release_date)
            elif data.get('release_date_condition') == '<':
                filters.append(db.func.to_date(Game.release_date, 'Mon DD, YYYY') < release_date)
            else:
                filters.append(db.func.to_date(Game.release_date, 'Mon DD, YYYY') == release_date)
  
    if 'required_age' in data:
        if data.get('age_condition') == '>':
            filters.append(Game.required_age > data['required_age'])
        elif data.get('age_condition') == '<':
            filters.append(Game.required_age < data['required_age'])
        else:
            filters.append(Game.required_age == data['required_age'])
    
    if 'price' in data:
        if data.get('price_condition') == '>':
            filters.append(Game.price > data['price'])
        elif data.get('price_condition') == '<':
            filters.append(Game.price < data['price'])
        else:
            filters.append(Game.price == data['price'])

    if 'dlc_count' in data:
        filters.append(Game.dlc_count == data['dlc_count'])
    
    if 'about_game' in data:
        if data.get('about_game_condition') == 'contains':
            filters.append(Game.about_game.ilike(f"%{data['about_game']}%"))
        else:
            filters.append(Game.about_game == data['about_game'])
    
    if 'supported_languages' in data:
        filters.append(Game.supported_languages.ilike(f"%{data['supported_languages']}%"))
    
    if 'windows' in data:
        filters.append(Game.windows == data['windows'])
    
    if 'mac' in data:
        filters.append(Game.mac == data['mac'])
    
    if 'linux' in data:
        filters.append(Game.linux == data['linux'])
    
    if 'positive' in data:
        if data.get('positive_condition') == '>':
            filters.append(Game.positive_reviews > data['positive'])
        elif data.get('positive_condition') == '<':
            filters.append(Game.positive_reviews < data['positive'])
        else:
            filters.append(Game.positive_reviews == data['positive'])
    
    if 'negative' in data:
        if data.get('negative_condition') == '>':
            filters.append(Game.negative_reviews > data['negative'])
        elif data.get('negative_condition') == '<':
            filters.append(Game.negative_reviews < data['negative'])
        else:
            filters.append(Game.negative_reviews == data['negative'])
    
    if 'score_rank' in data:
        if data.get('score_rank_condition') == '>':
            filters.append(Game.score_rank > data['score_rank'])
        elif data.get('score_rank_condition') == '<':
            filters.append(Game.score_rank < data['score_rank'])
        else:
            filters.append(Game.score_rank == data['score_rank'])

    if 'developer' in data:
        filters.append(Game.developer.ilike(f"%{data['developer']}%"))
    
    if 'publisher' in data:
        filters.append(Game.publisher.ilike(f"%{data['publisher']}%"))
    
    if 'categories' in data:
        filters.append(Game.categories.ilike(f"%{data['categories']}%"))
    
    if 'genres' in data:
        filters.append(Game.genres.ilike(f"%{data['genres']}%"))
    
    if 'tags' in data:
        filters.append(Game.tags.ilike(f"%{data['tags']}%"))

    # Apply the filters to the query
    query = Game.query.filter(and_(*filters))
    results = query.all()

    # Format the results into a list
    games_list = [{

        "app_id": game.app_id,
        "name": game.name,
        "release_date": game.release_date,
        "price": game.price,
        "required_age": game.required_age,
        "dlc_count": game.dlc_count,
        "about_game": game.about_game,
        "supported_languages": game.supported_languages,
        "windows": game.windows,
        "mac": game.mac,
        "linux": game.linux,
        "positive_reviews": game.positive_reviews,
        "negative_reviews": game.negative_reviews,
        "score_rank": game.score_rank,
        "developers": game.developer,
        "publishers": game.publisher,
        "categories": game.categories,
        "genres": game.genres,
        "tags": game.tags,
        "uploaded_at": game.uploaded_at
    } for game in results]

    return jsonify({"games": games_list})
