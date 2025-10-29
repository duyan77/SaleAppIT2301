from saleapp import db, app
from sqlalchemy import Column, Integer, String


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False, unique=True)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Init db success!")
