import json

from saleapp import db, app
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as RoleEnum
from flask_login import UserMixin

class UserRole(RoleEnum):
    USER = 1
    ADMIN = 2


class Base(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), unique=True, nullable=False)
    active = Column(Boolean, default=True)
    create_date = Column(DateTime, default=datetime.now())
    def __str__(self):
        return self.name

class User(Base, UserMixin):
    user_name = Column(String(150), unique=True, nullable=False)
    password = Column(String(150), nullable=False)
    avatar = Column(String(300), default="https://img.freepik.com/premium-vector/character-avatar-isolated_729149-194801.jpg?semt=ais_incoming&w=740&q=80")
    role = Column(Enum(UserRole), default=UserRole.USER)


class Category(Base):
    products = relationship('Product', backref='category', lazy=True)

class Product(Base):
    image = Column(String(300), default="https://media.istockphoto.com/id/2173059563/vector/coming-soon-image-on-white-background-no-photo-available.jpg?s=612x612&w=0&k=20&c=v0a_B58wPFNDPULSiw_BmPyhSNCyrP_d17i2BPPyDTk=")
    price = Column(Float, default=0.0)
    cate_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    description = Column(String(300))
    def __str__(self):
        return self.name

if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        # c1 = Category(name="LapTop")
        # c2 = Category(name="Mobile")
        # c3 = Category(name="Tablet")
        # db.session.add_all([c1,c2,c3])
        # with open('../data/product.json', encoding='utf-8') as f:
        #     product = json.load(f)
        #     for p in product:
        #         db.session.add(Product(**p))
        # db.session.commit()
        import hashlib
        password = hashlib.md5('123'.encode('utf-8')).hexdigest()
        u1 = User(name='abc', user_name='abc', password=password)
        db.session.add(u1)
        db.session.commit()
