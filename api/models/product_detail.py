from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, DateTime, func
from typing import Optional
import datetime as dt
from .base import Base


class ProductDetail(Base):
    __tablename__ = "product_detail"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    name: Mapped[str]
    value: Mapped[str]

    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "name": self.name,
            "value": self.value,
        }

    @staticmethod
    def from_dict(dictionary) -> "ProductDetail":
        class_attributes = ["id", "product_id", "name", "value"]
        dict_attributes = {
            key: value for key, value in dictionary.items() if key in class_attributes
        }

        return ProductDetail(**dict_attributes)
