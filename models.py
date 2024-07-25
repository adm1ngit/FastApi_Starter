from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy import Table, Column, Integer, String, Text, Boolean, ForeignKey


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    orders = relationship('Order', back_populates='user')

    def __repr__(self):
        return f"<user {self.username}"

class Order(Base):
    ORDER_STATUES = (
        ("PENDING", "Pending"),
        ("In_Transit", "in_transit"),
        ("Delivered", "delivered"),
    )
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="orders")
    product_id = Column(Integer, ForeignKey("products.id"))
    product = relationship("Product", back_populates="orders")

    def __repr__(self):
        return f"<order {self.id}"


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    price = Column(Integer)
    orders = relationship("Order", back_populates="user")

    def __repr__(self):
        return f"<product {self.name}"