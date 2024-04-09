from sqlalchemy import text, func, desc
from ..models.product import Product
from ..models.order import Order
from ..models.product import OrderProduct
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

    session = Session(engine)
    rows = session.scalars(statement).all()

    return [row.to_dict() for row in rows]


def get_orders_last_weeks():
    textual_query = text(
        """select * from `order` o 
where o.date_ordered BETWEEN (NOW() - INTERVAL 4 WEEK) AND NOW()"""
    )
    statement = select(Order).from_statement(textual_query)

    session = Session(engine)
    rows = session.scalars(statement).all()

    return [row.to_dict() for row in rows]
