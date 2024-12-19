from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DateTime, Float, Text, Table
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

# Association table for the many-to-many relationship between Products and Consumers
consumer_product_association = Table(
    'consumer_product',
    Base.metadata,
    Column('consumer_id', Integer, ForeignKey('consumers.id'), primary_key=True),
    Column('product_id', Integer, ForeignKey('products.id'), primary_key=True)
)

# Wholesale Model
class Wholesale(Base):
    __tablename__ = "wholesales"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    location = Column(String(200), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    products = relationship("Product", back_populates="wholesale")
    employees = relationship("Employee", back_populates="wholesale")


# Product Model
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text, nullable=True)
    wholesale_id = Column(Integer, ForeignKey('wholesales.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    wholesale = relationship("Wholesale", back_populates="products")
    consumers = relationship(
        "Consumer",
        secondary=consumer_product_association,
        back_populates="products"
    )


# Employee Model
class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    role = Column(String(100), nullable=False)
    salary = Column(Float, nullable=False)
    wholesale_id = Column(Integer, ForeignKey('wholesales.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship
    wholesale = relationship("Wholesale", back_populates="employees")


# Consumer Model
class Consumer(Base):
    __tablename__ = "consumers"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    contact_info = Column(String(200), nullable=True)
    preferences = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    products = relationship(
        "Product",
        secondary=consumer_product_association,
        back_populates="consumers"
    )
