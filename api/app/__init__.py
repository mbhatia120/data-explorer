from flask import Flask, request, jsonify
import requests
from io import StringIO
from flask_cors import CORS
import pandas as pd
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://postgres:password@db:5432/gamedb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


from app.models.user import User  
from app.models.game import Game  

with app.app_context():
    db.create_all()

from app.controllers.user_controller import user_bp  
from app.controllers.game_controller import game_bp

app.register_blueprint(user_bp)
app.register_blueprint(game_bp)

CORS(app, resources={r"/*": {"origins": "*"}})