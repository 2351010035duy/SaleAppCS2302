from flask import render_template, request, redirect
from saleapp import dao, app, login, admin
import math
from flask_login import login_user, current_user, logout_user

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

@app.route('/login', methods = ['get','post'])
def login_my_user():
    if current_user.is_authenticated:
        return redirect('/')
    err_msg = None
    if request.method.__eq__('POST'):
        user_name = request.form.get('user_name')
        password = request.form.get('password')
        user = dao.auth_user(user_name, password)
        if user:
            login_user(user)
            return redirect('/')
        else:
            err_msg = "Tài khoản hoặc mật khẩu bị lỗi!"

    return render_template('login.html', err_msg = err_msg)

@app.route('/register')
def register():
    err_msg = None
    if request.method.__eq__('POST'):
        user_name = request.form.get('user_name')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        user = dao.get_user_by_user_name(user_name)
        # if user and password.__eq__(confirm_password):

        # if user:
        #     err_msg = 'Tài khoản đã tồn tại!'
        #     return render_template('register.html', err_msg=err_msg)
        # elif not password.__eq__(confirm_password):
        #     err_msg = 'Mâật khẩu không khớp!'
        #     return render_template('register.html', err_msg=err_msg)
        # return redirect('/')
@app.route('/logout')
def logout_my_user():
    logout_user()
    return redirect('/login')


@app.context_processor
def common_attributes():
    return {
        "cate": dao.load_categories()
    }

@login.user_loader
def get_user(id):
    return dao.get_user_by_id(id)

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
