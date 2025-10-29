from flask import Flask, render_template, request
import dao
from saleapp import app
import math

from saleapp.dao import count_products


@app.route("/")
def index():
    q = request.args.get("q")
    cate_id = request.args.get("cate_id")
    page = request.args.get('page')
    per_page = app.config.get("PAGE_SIZE")
    page_number = math.ceil(count_products() / per_page)
    prods = dao.load_products(q=q, cate_id=cate_id, page=page, per_page=per_page)

    return render_template("index.html", prods=prods, page=page, page_number=page_number)


@app.route("/products/<int:id>")
def details(id):
    prod = dao.get_product_by_id(id)
    return render_template("product-details.html", prod=prod)


@app.context_processor
def common_attribute():
    return {
        "cates": dao.load_categories()
    }


if __name__ == "__main__":
    app.run(debug=True)
