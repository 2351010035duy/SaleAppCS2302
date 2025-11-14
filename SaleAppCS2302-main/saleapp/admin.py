from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from  flask_admin.theme import Bootstrap4Theme

from models import Category, Product
from saleapp import app, db

admin = Admin(app=app, name='E-COMMERCE', theme=Bootstrap4Theme())

class MyCategoryView(ModelView):
    column_list = ['name','products']


class MyIndexView(AdminIndexView):
    @expose('/')
    def index(self) -> str:
        return self.render('admin/index')

admin.add_view(MyCategoryView(Category,db.session))
admin.add_view(ModelView(Product,db.session))