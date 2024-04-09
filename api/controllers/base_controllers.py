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
from ..models.product import Product, OrderProduct
from ..models.product_detail import ProductDetail


class ItemAPI(MethodView):
    init_every_request = False

    def __init__(self, model):
        self.model = model

    def __get_by_id__(self, id):
        statement = select(self.model).where(self.model.id == id)
        session = Session(engine)
        return session.scalars(statement).first()

    def get(self, id):
        statement = select(self.model).where(self.model.id == id)
        session = Session(engine)
        row = session.scalars(statement).first()

        print(row)
        if row is None:
            return make_response("Not found", 404)

        print(row.to_dict())

        return jsonify(row.to_dict())

    def patch(self, id):
        with Session(engine, expire_on_commit=False) as session:
            select_statement = select(self.model).where(self.model.id == id)
            obj = session.scalars(select_statement).first()
            for name, value in request.json.items():
                if name in obj.__dict__.keys():
                    setattr(obj, name, value)
            session.commit()
        return jsonify(obj.to_dict())

    def delete(self, id):
        try:
            with Session(engine) as session:
                obj = session.get(self.model, id)
                session.delete(obj)
                session.commit()
                return make_response("Successfully deleted object", 200)
        except Exception as e:
            print(e, repr(e))
            return make_response(f"Could not delete object with id {id}", 500)


class GroupAPI(MethodView):
    init_every_request = False

    def __init__(self, model):
        self.model = model

    # list all items
    def get(self):
        statement = select(self.model)
        session = Session(engine)
        rows = session.scalars(statement).all()

        return jsonify([row.to_dict() for row in rows])

    def post(self):
        print(request)
        print(request.json)
        # object in transient state
        new_item = self.model.from_dict(request.json)
        new_id = None
        with Session(engine, expire_on_commit=False) as session:
            # object in pending state (look at session.new)
            session.add(new_item)
            # object in persistent state
            session.commit()
            new_id = new_item.id

        return jsonify({"id": new_id})


def register_api(app: Flask, model, name: str):
    item = ItemAPI.as_view(f"{name}-item", model)
    group = GroupAPI.as_view(f"{name}-group", model)
    app.add_url_rule(rule=f"/{name}/<int:id>", view_func=item)
    app.add_url_rule(rule=f"/{name}", view_func=group)


register_api(app, Product, "product")
register_api(app, Customer, "customer")
# register_api(app, Order, "order")
register_api(app, Order, "order")
register_api(app, ProductDetail, "product_detail")
register_api(app, OrderProduct, "order_product")
register_api(app, Address, "address")
