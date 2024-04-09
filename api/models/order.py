from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, DateTime, func
from typing import Optional
import datetime as dt
from .base import Base


class Order(Base):
    __tablename__ = "order"

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"))
    delivery_address_id: Mapped[int] = mapped_column(ForeignKey("delivery_address.id"))
    payment_method: Mapped[str]
    date_ordered: Mapped[Optional[dt.datetime]]

    def to_dict(self):
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "delivery_address_id": self.delivery_address_id,
            "payment_method": self.payment_method,
            "date_ordered": self.date_ordered,
        }

    @staticmethod
    def from_dict(dictionary) -> "Order":
        class_attributes = [
            "id",
            "customer_id",
            "delivery_address_id",
            "payment_method",
            "date_ordered",
        ]
        dict_attributes = {
            key: value for key, value in dictionary.items() if key in class_attributes
        }

        return Order(**dict_attributes)
