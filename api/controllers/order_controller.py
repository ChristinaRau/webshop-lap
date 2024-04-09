from ..app import app
from flask.views import MethodView
from sqlalchemy import select
from sqlalchemy.orm import Session
from ..db import engine
from flask import jsonify, Flask

from ..models.computer_base_model import ComputerBaseModel
from ..models.reseller import Reseller
from ..models.order import Order
from ..models.addition import Addition
from ..models.order_computer import OrderComputer
from ..models.order_computer_addition import OrderComputerAddition

from .base_controllers import ItemAPI, GroupAPI


class OrderItemAPI(ItemAPI):
    init_every_request = False

    def __init__(self, model):
        self.model = model

    def get(self, id):
        statement = (
            select(self.model)
            .join_from(self.model, Reseller)
            .where(self.model.id == id)
        )
        session = Session(engine)
        row = session.scalars(statement).first()

        print(row)
        print(row.to_dict())

        return jsonify(row.to_dict())


class OrderGroupAPI(GroupAPI):
    init_every_request = False

    def __init__(self, model):
        self.model = model

    def get(self):
        statement = select(self.model, Reseller).join_from(self.model, Reseller)
        session = Session(engine)
        rows = session.scalars(statement).all()

        print(rows)
        # print(row.to_dict())

        return jsonify([row.to_dict() for row in rows])


# def register_api(app: Flask, model, name: str):
# 	item = ItemAPI.as_view(f"{name}-item", model)
# 	group = GroupAPI.as_view(f"{name}-group", model)
# 	app.add_url_rule(f"/{name}/<int:id>", view_func=item)
# 	app.add_url_rule(f"/{name}", view_func=group)

# register_api(app, Order, "order")

app.add_url_rule("/order/<int:id>", view_func=OrderItemAPI.as_view("order-item", Order))
app.add_url_rule("/order", view_func=OrderGroupAPI.as_view("order-group", Order))


# stuff with relationships
