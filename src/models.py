import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    
class Followers(Base):
    __tablename__ = 'followers'
    community_id = Column(Integer, primary_key=True) # Should it be necessary!?
    follower_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    followed_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)

class Posts(Base):
    __tablename__ = 'posts'
    post_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)

class Media(Base):
    __tablename__ = 'media'
    media_id = Column(Integer, primary_key=True)
    media_type = Column(String, nullable=False) # 'enum'!?
    media_url = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey('posts.post_id'), nullable=False)

class Comments(Base):
    __tablename__ = 'comments'
    comment_id = Column(Integer, primary_key=True)
    comment_text = Column(String)
    author_user_id = Column(String, ForeignKey('users.user_id'), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.post_id'), nullable=False)
    
    def to_dict(self):
        return {}

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
