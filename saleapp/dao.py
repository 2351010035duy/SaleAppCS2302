import json

def load_categories():
    with open('../data/category.json', encoding='utf-8') as f:
        cate = json.load(f)
        return cate

def load_products(q = None, category = None):
    with open('../data/product.json', encoding='utf-8') as f:
        product = json.load(f)
        if q:
            product = [p for p in product if p['name'].find(q)>=0]
        if category:
            product = [p for p in product if p['cate_id'] == int(category)]
        return product

def get_product_by_id(id):
    with open('../data/product.json', encoding = 'utf-8') as f:
        product = json.load(f)
        for p in product:
            if p['id'] == int(id):
                return p
    return None
if __name__ == '__main__':
    print(get_product_by_id(1))