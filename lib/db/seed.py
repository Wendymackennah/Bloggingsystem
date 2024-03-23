from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User,Post,Comment,Base 

fake = Faker()
db_path = '../bloggingsystem.db'

engine = create_engine(f'sqlite:///{db_path}')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


if __name__ == '__main__':
    for i in range(50):
        user = User(name=fake.name())
        session.add(user)
    session.commit()
    print("Users added")

    for i in range(50):
        post = Post(title=fake.sentence(nb_words=5), content=fake.text())
        session.add(post)
    session.commit()
    print("Posts added")

    for i in range(50):
        comment = Comment(text=fake.sentence(nb_words=5))
        session.add(comment)
    session.commit()



    print("Comments added")

