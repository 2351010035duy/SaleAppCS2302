import hashlib
import json
from models import Category, Product, User
import saleapp
from saleapp import  app

def load_categories():
    # with open('../data/category.json', encoding='utf-8') as f:
    #     cate = json.load(f)
    #     return cate
    return Category.query.all()

def load_products(q = None, category = None, page = None):
    # with open('../data/product.json', encoding='utf-8') as f:
    #     product = json.load(f)
    #     if q:
    #         product = [p for p in product if p['name'].find(q)>=0]
    #     if category:
    #         product = [p for p in product if p['cate_id'] == int(category)]
    #     return product
    query = Product.query
    if q:
        query = query.filter(Product.name.contains(q))
    if category:
        query = query.filter(Product.cate_id.__eq__(category))
    if page:
        start = (int(page)-1)*(saleapp.app.config["PAGE_SIZE"])
        end = start + saleapp.app.config["PAGE_SIZE"]
        query = query.slice(start,end)
    return query.all()

def count_product():
    return Product.query.count()

def get_product_by_id(id):
    # with open('../data/product.json', encoding = 'utf-8') as f:
    #     product = json.load(f)
    #     for p in product:
    #         if p['id'] == int(id):
    #             return p
    # return None
    return Product.query.get(id)

def auth_user(user_name, password):
    password = hashlib.md5(password.encode('utf-8')).hexdigest()
    return User.query.filter(User.user_name.__eq__(user_name), User.password.__eq__(password)).first()

def get_user_by_user_name(user_name):
    return User.query.filter(User.user_name.__eq__(user_name)).first()


def get_user_by_id(user_id):
    return User.query.get(user_id)
if __name__ == '__main__':
    with app.app_context():
        print(auth_user('abc','123'))
