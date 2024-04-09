
from sqlalchemy.orm import (
	Mapped,
    mapped_column
)
from sqlalchemy import (
    ForeignKey,
    DateTime
)
from typing import Optional
import datetime as dt


class Reseller(Base):
    __tablename__ = 'reseller'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


class ComputerBaseModel(Base):
    __tablename__ = 'computer_base_model'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    ram_gigabyte: Mapped[float]
    price: Mapped[float]
    storage_gigabyte: Mapped[float]
    processor: Mapped[str]
    image_path: Mapped[Optional[str]]
    description: Mapped[Optional[str]]


class OrderComputer(Base):
    __tablename__ = 'order_computer'

    id: Mapped[int] = mapped_column(primary_key=True)
    computer_base_model_id: Mapped[int] = mapped_column(ForeignKey('computer_base_model.id'))
    orderId: Mapped[int] = mapped_column(ForeignKey('orderId.id'))


class Addition(Base):
    __tablename__ = 'addition'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    value: Mapped[str]
    price: Mapped[float]


class OrderComputerAddition(Base):
    __tablename__ = 'order_computer_addition'

    id: Mapped[int] = mapped_column(primary_key=True)
    order_computer_id: Mapped[int] = mapped_column(ForeignKey('order_computer.id'))
    addition_id: Mapped[int] = mapped_column(ForeignKey('addition.id'))


class Order(Base):
    __tablename__ = 'order'

    id: Mapped[int] = mapped_column(primary_key=True)
    datetime: Mapped[dt.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class Test(Base):
    __tablename__ = 'test'

    id: Mapped[int]
    date_needed_id: Mapped[dt.datetime] = mapped_column(ForeignKey('date_needed.id'), DateTime(timezone=True), server_default=func.now())
    date_optional: Mapped[Optional[dt.datetime]] = mapped_column(DateTime(timezone=True), server_default=func.now())

