
from sqlalchemy.orm import (
	Mapped,
    mapped_column
)
from sqlalchemy import (
    ForeignKey,
    DateTime,
    func
)
from typing import Optional
import datetime as dt
from .base import Base


class Product(Base):
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[float]
    image_path: Mapped[Optional[str]]


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "image_path": self.image_path
        }


    @staticmethod
    def from_dict(dictionary) -> "Product":
        class_attributes = ['id', 'name', 'price', 'image_path']
        dict_attributes = {key : value for key, value in dictionary.items() if key in class_attributes}

        return Product(**dict_attributes)
        