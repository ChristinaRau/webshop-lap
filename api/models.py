from sqlalchemy.orm import (
    relationship,
    Session,
    mapped_column,
    Mapped,
    DeclarativeBase,
    relationship
)
from typing import List
from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    ForeignKey,
    MetaData,
    select,
    func,
    create_engine,
)

# UserMixin provides default implementations for methods that are needed for flask-login
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

# dataclass annotation that automatically adds special methods like __init__ and __repr__
from dataclasses import dataclass
from config import DB_URI


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
engine = create_engine(DB_URI)

@dataclass 
class ComputerBaseModel(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    base_ram_gigabyte: Mapped[float]
    base_price: Mapped[float]
    base_storage_id: Mapped[int] = db.Column(db.Integer, db.ForeignKey("storage.id"))
    base_processor_id: Mapped[int] = db.Column(db.Integer, db.ForeignKey("processor.id"))
    image_path: Mapped[str]
    description: Mapped[str]
    base_storage: Mapped["Storage"] = relationship()


@dataclass 
class Storage(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str]
    amount_gigabyte: Mapped[float]
    # computer_base_models: Mapped[List["ComputerBaseModel"]] = relationship(back_populates="base_storage")


@dataclass
class Processor(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
