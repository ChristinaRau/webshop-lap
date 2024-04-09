from sqlalchemy import text, func, desc
from ..models.product import Product
from ..models.order_product import OrderProduct
from urllib import response
from ..app import app
from flask.views import MethodView
from sqlalchemy import select
from sqlalchemy.orm import Session
from ..db import engine
from flask import jsonify, Flask, request, make_response


def get_top_selling_products():
    textual_query = text(
        """SELECT p.*, count(*) as ordercount FROM `product` p
left join order_product op on op.product_id = p.id 
group by p.id
order by ordercount desc
limit 5"""
    )
    statement = select(Product).from_statement(textual_query)
    """  statement = (
        select(Product, func.count(Product.id).label("count"))
        .join(OrderProduct)
        .order_by(
            desc("count"),
        )
        .limit(5)
    ) """
    session = Session(engine)
    rows = session.scalars(statement).all()

    return [row.to_dict() for row in rows]


def get_worst_selling_products():
    textual_query = text(
        """SELECT p.*, count(*) as ordercount FROM `product` p
left join order_product op on op.product_id = p.id 
group by p.id
order by ordercount asc
limit 5"""
    )
    statement = select(Product).from_statement(textual_query)

    """ statement = (
        select(Product, func.count(Product.id).label("count"))
        .join(OrderProduct)
        .order_by(
            "count",
        )
        .limit(5)
    ) """

    session = Session(engine)
    rows = session.scalars(statement).all()

    return [row.to_dict() for row in rows]
