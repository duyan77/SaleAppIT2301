import json

from saleapp.models import Category, Product


def load_categories():
    return Category.query.all()


def load_products(q=None, cate_id=None, page=None, per_page=None):
    products = Product.query.all()

    if q:
        products = [p for p in products if q.lower() in p.name.lower()]

    if cate_id:
        products = [p for p in products if p.cate_id == int(cate_id)]

    if page:
        page = int(page)
        per_page = int(per_page)
        start = (page - 1) * per_page
        end = start + per_page
        products = products[start:end]

    return products


def get_product_by_id(id):
    return Product.query.get(id)


def count_products():
    return Product.query.count()


if __name__ == "__main__":
    print(get_product_by_id(2))
