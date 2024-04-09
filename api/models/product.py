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

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "image_path": self.image_path,
            "product_details": [item.to_dict() for item in self.product_details],
        }

    @staticmethod
    def from_dict(dictionary) -> "Product":
        class_attributes = ["id", "name", "price", "image_path"]
        dict_attributes = {
            key: value for key, value in dictionary.items() if key in class_attributes
        }

        return Product(**dict_attributes)
