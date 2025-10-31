from flask import render_template, request
from saleapp import dao, app
import math

@app.route('/')
def index():
    q = request.args.get('q')
    category = request.args.get('cate')
    page = request.args.get('page')
    product = dao.load_products(q=q, category=category, page=page)
    pages = math.ceil(dao.count_product()/app.config["PAGE_SIZE"])
    return render_template("index.html", product=product, pages=pages)


@app.route('/products/<int:id>')
def details(id):
    product = dao.get_product_by_id(id)
    return render_template('product-details.html', product=product)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.context_processor
def common_attributes():
    return {
        "cate": dao.load_categories()
    }
if __name__ == '__main__':
    app.run(debug=True)
