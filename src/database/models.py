from typing import List
from datetime import datetime

from sqlalchemy import String, Table, Column, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import declarative_base, mapped_column, Mapped, relationship
from flask_sqlalchemy import SQLAlchemy


Base = declarative_base()
db = SQLAlchemy(model_class=Base, engine_options=dict(echo=True))


rev_prod_assoc = Table( 
    "rev_prod_assoc",
    Base.metadata,
    Column("review_id", ForeignKey("reviews.id"), primary_key=True),
    Column("product_id", ForeignKey("products.id"), primary_key=True)
)

user_prod_assoc = ( 
    "user_prod_assoc",
    Base.metadata,
    Column("user_id", ForeignKey("users.id", primary_key=True)),
    Column("product_id", ForeignKey("products.id"), primary_key=True)
)


user_shop_list_assoc = ( 
    "user_shop_list_assoc",
    Base.metadata,
    Column("user_id", ForeignKey("users.id", primary_key=True)),
    Column("product_id", ForeignKey("products.id"), primary_key=True)
)

class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[str] = mapped_column(String(), primary_key=True)
    text: Mapped[str] = mapped_column(String())

class Product(Base):
    __tablename__ = "products"

    id: Mapped[str] = mapped_column(String(), primary_key=True)
    name: Mapped[str] = mapped_column(String())
    description: Mapped[str] = mapped_column(String())
    ing_url: Mapped[str] = mapped_column(String())
    price: Mapped[float] = mapped_column()
    reviews : Mapped[List[Review]] = relationship(secondary=rev_prod_assoc)


class User(Base):
    id: Mapped[str] = mapped_column(String(), primary_key=True)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String())
    password: Mapped[str] = mapped_column(String())
    temp_password: Mapped[str] = mapped_column(String())
    time_password: Mapped[datetime] = mapped_column(DateTime())
    is_admin: Mapped[bool] = mapped_column(Boolean(), default=False)
    products: Mapped[List[Product]] = relationship()
    shop_list: Mapped[List[Product]] = relationship()