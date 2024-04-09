from re import L
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime, func
from typing import Optional, List
import datetime as dt
from .base import Base
from .product_detail import ProductDetail


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[float]
    image_path: Mapped[Optional[str]]
    product_details: Mapped[List["ProductDetail"]] = relationship()
    order_products: Mapped[List["OrderProduct"]] = relationship()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "image_path": self.image_path,
            "product_details": [item.to_dict() for item in self.product_details],
            "order_product_count": len(self.order_products),
        }

    @staticmethod
    def from_dict(dictionary) -> "Product":
        class_attributes = ["id", "name", "price", "image_path"]
        dict_attributes = {
            key: value for key, value in dictionary.items() if key in class_attributes
        }

        return Product(**dict_attributes)


class OrderProduct(Base):
    __tablename__ = "order_product"

    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    product: Mapped["Product"] = relationship()

    def to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "product_id": self.product_id,
            "product": self.product.to_dict() if self.product is not None else "",
        }

    @staticmethod
    def from_dict(dictionary) -> "OrderProduct":
        class_attributes = ["id", "order_id", "product_id"]
        dict_attributes = {
            key: value for key, value in dictionary.items() if key in class_attributes
        }

        return OrderProduct(**dict_attributes)
