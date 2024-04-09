from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime, func
from typing import Optional
import datetime as dt
from .base import Base
from .product import Product


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
