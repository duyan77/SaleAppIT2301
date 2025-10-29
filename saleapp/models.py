import json

from sqlalchemy.orm import relationship

from saleapp import db, app
from sqlalchemy import Column, Integer, String, Float, ForeignKey


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False, unique=True)
    products = relationship("Product", backref="category", lazy=True)

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False, unique=True)
    price = Column(Float, default=0.0)
    image = Column(String(300), default="")
    cate_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        with open("data/product.json", encoding="utf-8") as f:
            product = json.load(f)
            for p in product:
                db.session.add(Product(name=p["name"], price=p["price"], image=p["image"], cate_id=p["cate_id"]))
            db.session.commit()
        print("Init db success!")
