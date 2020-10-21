# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from flask import Flask, redirect, url_for, render_template, session, g, jsonify, request
from config import DevConfig
from models import db, User, Order
from controllers.printer import printer
from controllers.login import login
from controllers.document_share import document_share
# 实际使用支付时，请取消下面的注视
# from controllers.daoinkpay import daoinkpay
import datetime, json

app = Flask(__name__)
app.config.from_object(DevConfig)

db.init_app(app)
# app.permanent_session_lifetime = datetime.timedelta(seconds=10*60)          #设置sission过期时间为10min

# 自定义jinja过滤器
def time_format(l):
    return str(l)[:-7]
app.add_template_filter(time_format, 'format_time')


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        page = request.form.get('page')
        page = int(page)
        pagination = Order.query.filter(Order.User_Id == g.current_user.Id).order_by(Order.Id.desc()).paginate(page, per_page=10, error_out=False)
        user_order = pagination.items
        lenth = len(user_order)
        tem = []
        for x in user_order:
            tem.append(x.to_json())
        # return render_template('index.html', user_order=user_order, lenth=lenth, pagination=pagination)
        print jsonify(tem)
        return jsonify(objects = tem)
    if g.current_user != None:
        # user_order = Order.query.filter(Order.User_Id == g.current_user.Id).order_by(Order.Id.desc()).all()
        # lenth = len(user_order)
        #
        # return render_template('index.html', user_order=user_order, lenth=lenth)
        page = request.form.get('page', 1)
        page = int(page)
        pagination = Order.query.filter(Order.User_Id == g.current_user.Id).order_by(Order.Id.desc()).paginate(page, per_page=10, error_out=False)
        user_order = pagination.items
        lenth = len(user_order)
        return render_template('index.html', user_order=user_order, lenth=lenth, pagination=pagination)
    else:
        user_order = None
        lenth = 0
        return render_template('index.html')
        # return redirect('/login')
        # return render_template('index.html', user_order=user_order, lenth=lenth)


@app.before_request
def check_user():
    if 'user_phone' in session:
        g.current_userphone = session['user_phone']
        user = User.query.filter(User.Tel_Number == g.current_userphone).first()
        g.current_user = user

    else:
        g.current_userphone = json.dumps(None)
        g.current_user = None




app.register_blueprint(printer)
app.register_blueprint(login)
app.register_blueprint(document_share)
# 实际使用支付时，请取消下面的注视
# app.register_blueprint(daoinkpay)

if __name__ == '__main__':
    app.run(host='localhost', port=8090)
