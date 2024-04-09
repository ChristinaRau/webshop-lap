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
from ..models.product import OrderProduct
from ..models.product import Product
from ..models.product_detail import ProductDetail


@app.get("/billing/order/<int:id>")
def get_order(id):
    statement = select(Order).join(OrderProduct).join(Product).where(Order.id == id)
    session = Session(engine)
    row = session.scalars(statement).first()

    if row is None:
        return make_response("Not found", 404)

    return jsonify(row.to_dict())
