
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


class Address(Base):
    __tablename__ = 'address'

    id: Mapped[int] = mapped_column(primary_key=True)
    street: Mapped[str]
    house_number: Mapped[str]
    zip_code: Mapped[str]
    city: Mapped[str]
    country: Mapped[str]


    def to_dict(self):
        return {
            "id": self.id,
            "street": self.street,
            "house_number": self.house_number,
            "zip_code": self.zip_code,
            "city": self.city,
            "country": self.country
        }


    @staticmethod
    def from_dict(dictionary) -> "Address":
        class_attributes = ['id', 'street', 'house_number', 'zip_code', 'city', 'country']
        dict_attributes = {key : value for key, value in dictionary.items() if key in class_attributes}

        return Address(**dict_attributes)
        