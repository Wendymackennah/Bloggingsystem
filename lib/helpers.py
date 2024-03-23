from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import User,Post,Comment,Base 

db_path = '../lib/db/bloggingsystem.db'

engine = create_engine(f'sqlite:///{db_path}')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()



def main_menu():
  print("Main Menu")
  print("1. Add posts")
  print("2. Add comment")
  print("3. View post")
  print("4. Search post")
  print("5. Exit")


def add_post():
    print("Add post")

    title = input("Enter the title of the post: ")
    content = input("Enter the content of the post: ")

    post = Post(title=title, content=content)
    session.add(post)
    session.commit()
    print("Post added successfully!")


def add_comment(post_id):
    print("Add comment")

    text = input("Enter your comment: ")

    comment = Comment(text=text)
    session.add(comment)
    session.commit()

    post = session.query(Post).filter(Post.id == post_id).first()
    if post:
        post.comments.append(comment)
        session.commit()
        print("Comment added successfully to the post!")
    else:
        print(f"Post with ID {post_id} not found.")

def view_post_comments(post_id):
    post = session.query(Post).filter(Post.id == post_id).first()
    if post:
        print(f"Comments for Post '{post.title}':")
        if post.comments:
            for idx, comment in enumerate(post.comments, 1):
                print(f"{idx}. {comment.text}")
        else:
            print("No comments found for this post.")
    else:
        print(f"Post with ID {post_id} not found.")

def search_posts(keyword):
    posts = session.query(Post).filter(
        (Post.title.like(f"%{keyword}%")) | (Post.content.like(f"%{keyword}%"))
    ).all()

    if posts:
        print(f"Search results for keyword '{keyword}':")
        for idx, post in enumerate(posts, 1):
            print(f"{idx}. Title: {post.title}")
            print(f"   Content: {post.content}")
            print("--------------------------------")
    else:
        print(f"No posts found containing the keyword '{keyword}'.")




  
  

