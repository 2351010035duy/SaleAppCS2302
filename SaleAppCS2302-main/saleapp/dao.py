import json
from models import Category, Product
import saleapp

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
if __name__ == '__main__':
    print(get_product_by_id(1))