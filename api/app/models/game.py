from app import db
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Boolean, Float
from datetime import datetime, timezone

class Game(db.Model):
    __tablename__ = 'games'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  
    app_id = Column(Integer, nullable=False)  
    name = Column(String, nullable=False)  
    release_date = Column(String, nullable=True)  
    required_age = Column(Integer, nullable=True)  
    price = Column(Float, nullable=True) 
    dlc_count = Column(Integer, nullable=True) 
    about_game = Column(Text, nullable=True)  
    supported_languages = Column(String, nullable=True)  
    windows = Column(Boolean, nullable=True)  
    mac = Column(Boolean, nullable=True) 
    linux = Column(Boolean, nullable=True)  
    positive_reviews = Column(Integer, nullable=True)  
    negative_reviews = Column(Integer, nullable=True)  
    score_rank = Column(Float, nullable=True)  
    developer = Column(String, nullable=True)  
    publisher = Column(String, nullable=True)  
    categories = Column(Text, nullable=True)  
    genres = Column(Text, nullable=True) 
    tags = Column(Text, nullable=True)  
    uploaded_at = Column(DateTime, default=datetime.now(timezone.utc)) 
    
    
