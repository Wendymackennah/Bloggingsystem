from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

post_comments = Table(
    'post_comments',
    Base.metadata,
    Column('post_id', Integer, ForeignKey('posts.id')),
    Column('comment_id', Integer, ForeignKey('comments.id'))
)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)

    post_comments = relationship("Comment", secondary=post_comments, backref="posts")

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    text = Column(String)

    comment_posts = relationship("Post", secondary=post_comments, backref="comments")
