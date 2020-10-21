# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
import datetime, os, time

#数据模型部分
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'User'  #表名字默认是类名字的小写版本(如果没有此语句)

    Id = db.Column(db.Integer(), primary_key=True)
    Tel_Number = db.Column(db.String(255), nullable=False)
    Password = db.Column(db.String(255), nullable=False)
    Register_Date = db.Column(db.DateTime, default=datetime.datetime.now)




class Order(db.Model):
    __tablename__ = 'Order'

    Id = db.Column(db.Integer(), primary_key=True)
    File_Dir = db.Column(db.String(255), nullable=False)
    File_Name = db.Column(db.String(255))                           # 文件原始名字
    Born_Date = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)
    Time_Way = db.Column(db.Integer())                              # 打印时间规划方式，自由排队
    Print_Date = db.Column(db.DateTime)                             # 打印时间点 *
    Print_Place = db.Column(db.String(255), nullable=False)
    Print_pages = db.Column(db.Integer())                           # 每份页数  *
    Print_Copies = db.Column(db.Integer())                          # 份数
    Print_Direction = db.Column(db.String(255), nullable=False)     # 横向，纵向
    Print_Colour = db.Column(db.String(255), nullable=False)
    Print_size = db.Column(db.String(255), nullable=False)
    Print_way = db.Column(db.String(255), nullable=False)           # 打印的方式，单面或双面
    Print_Money = db.Column(db.Float())                             # 订单价格
    Print_Status = db.Column(db.Integer(), default=0)               # 订单状态，0:已提交文件但未支付, 1:已经支付但未打印, 2:已经加入下载队列, 3:已打印
    Trade_Number = db.Column(db.String(255))                        # 支付订单号


    User_Id = db.Column(db.Integer(), db.ForeignKey('User.Id'), nullable=False)
    user = db.relationship('User', foreign_keys='Order.User_Id')

    def to_json(self):
        born_date = str(self.Born_Date.year)+"-"+str(self.Born_Date.month)+"-"+str(self.Born_Date.day)+" "+str(self.Born_Date.hour)+":"+str(self.Born_Date.minute)+":"+str(self.Born_Date.second)
        return {
                'Print_Money': self.Print_Money,
                'File_Name': self.File_Name,
                'Born_Date': born_date,
                'Print_Place': self.Print_Place,
                'Print_Status': self.Print_Status
        }





