from urllib import response
from ..app import app
from flask.views import MethodView
from sqlalchemy import select
from sqlalchemy.orm import Session
from ..db import engine
from flask import jsonify, Flask, request, make_response

from ..models.order import Order
from ..models.address import Address
from ..models.customer import Customer
from ..models.order_product import OrderProduct
from ..models.product import Product
from ..models.product_detail import ProductDetail

from ..services.statistics import get_top_selling_products, get_worst_selling_products


@app.get("/statistics")
def get_stats():
    return jsonify(
        {
            "top_products": get_top_selling_products(),
            "worst_products": get_worst_selling_products(),
        }
    )
