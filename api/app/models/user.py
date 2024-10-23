from app import db
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
import random
from sqlalchemy.orm import relationship


class User(db.Model):
    __tablename__ = 'users' 
    
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)  
    username = Column(String, nullable=False, unique=True) 
    created_at = Column(DateTime, default=datetime.now(timezone.utc) )  
    
    def to_dict(self):
        return {
            "username": self.username,
        }
  
    def __repr__(self):
        return f'<User {self.username}>'