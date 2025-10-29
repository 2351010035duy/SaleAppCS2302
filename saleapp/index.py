from flask import Flask, render_template, request
from saleapp import dao

app = Flask(__name__)


@app.route('/')
def index():
    q = request.args.get('q')
    category = request.args.get('cate')
    print(category)
    product = dao.load_products(q=q, category=category)
    return render_template("index.html", product=product)


@app.route('/products/<int:id>')
def details(id):
    product = dao.get_product_by_id(id)
    return render_template('product-details.html', product=product)

@app.context_processor
def common_attributes():
    return {
        "cate": dao.load_categories()
    }
if __name__ == '__main__':
    app.run(debug=True)
