from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey, Boolean, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class ProductCategory(Base):
    __tablename__ = 'product_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    desc = Column(Text)
    created_at = Column(DateTime)
    modified_at = Column(DateTime)
    deleted_at = Column(DateTime)

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    desc = Column(Text)
    created_at = Column(DateTime)
    modified_at = Column(DateTime)
    deleted_at = Column(DateTime)
    SKU = Column(String(255))
    category_id = Column(Integer, ForeignKey('product_category.id'))
    inventory_id = Column(Integer)
    price = Column(Numeric(10, 2))
    discount_id = Column(Integer)
    quantity = Column(Integer)
    active = Column(Boolean)
    discount_percent = Column(Numeric(5, 2))
    category = relationship("ProductCategory")

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///sqlalchemy_example.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
