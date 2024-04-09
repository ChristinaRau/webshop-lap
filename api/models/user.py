from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, DateTime, func
from typing import Optional
import datetime as dt
from .base import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"))
    username: Mapped[str]
    password: Mapped[str]

    def to_dict(self):
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "username": self.username,
            "password": self.password,
        }

    @staticmethod
    def from_dict(dictionary) -> "User":
        class_attributes = ["id", "customer_id", "username", "password"]
        dict_attributes = {
            key: value for key, value in dictionary.items() if key in class_attributes
        }

        return User(**dict_attributes)
