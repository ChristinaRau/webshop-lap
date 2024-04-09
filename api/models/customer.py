from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime, func
from typing import Optional
import datetime as dt
from .base import Base
from .address import Address


class Customer(Base):
    __tablename__ = "customer"

    id: Mapped[int] = mapped_column(primary_key=True)
    billing_address_id: Mapped[int] = mapped_column(ForeignKey("billing_address.id"))
    email_address: Mapped[str]
    tel_number: Mapped[Optional[str]]
    billing_address: Mapped["Address"] = relationship()

    def to_dict(self):
        return {
            "id": self.id,
            "billing_address_id": self.billing_address_id,
            "email_address": self.email_address,
            "tel_number": self.tel_number,
            "billing_address": (
                self.billing_address.to_dict()
                if self.billing_address is not None
                else ""
            ),
        }

    @staticmethod
    def from_dict(dictionary) -> "Customer":
        class_attributes = ["id", "billing_address_id", "email_address", "tel_number"]
        dict_attributes = {
            key: value for key, value in dictionary.items() if key in class_attributes
        }

        return Customer(**dict_attributes)
