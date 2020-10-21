#!/usr/bin/env python
#coding:utf-8
from flask import Flask, Blueprint, render_template, request, flash, session, redirect, url_for, g, jsonify
import datetime, os
from app.models import db, User, Order
from werkzeug.utils import secure_filename
from app.pdf_operate import read_pdf_pages, switch_topdf
from PyPDF2 import PdfFileReader
from app.config import RedisConfig
import redis
printer = Blueprint(
    'printer',
    __name__
)

@printer.route('/select', methods=['GET', 'POST'])
def select():
    global datetimes
    global now
    datetimes = datetime.datetime.now()
    now = str(datetimes.year)+"-"+str(datetimes.month)+"-"+str(datetimes.day)+"_"+str(datetimes.hour)+"-"+str(datetimes.minute)+"-"+str(datetimes.second)
    if request.method == 'POST':
        printfile = request.files['uploadfile']         # 文件
        place = request.form.get("place")               # 打印点
        copies = request.form.get("copies")             # 份数
        direction = request.form.get("direction")       # 排版方向
        colour = request.form.get("colour")             # 彩色或黑白
        paper_size = request.form.get("paper_size")     # 纸张大小
        print_way = request.form.get("print_way")       # 单双面
        time_way = request.form.get("time_way")         # 预约或自动排队
        pageCount = 1                                   # 文件页数
        cost = 0.2*int(copies)


        filename = printfile.filename
        index_point = filename.rindex(".")
        new_filename = str(g.current_user.Tel_Number)+"_" + now + filename[index_point:]
        # basepath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        basepath = os.path.abspath(os.path.dirname(__file__))       # 当前文件所在目录
        parentdir = os.path.dirname(basepath)                       # 父级目录
        # 判断文件类型

        # 识别不需要转换的文件

        if filename[index_point:] in [".pdf", ".jpg", ".png", ".jpeg"]:
            upload_path = os.path.join(parentdir, 'static/Upload_Files', secure_filename(new_filename))
            printfile.save(upload_path)

            if filename[index_point:] != '.pdf':        # 图片文件一律按1页处理
                pageCount = 1
                cost = pageCount*cost
            else:
                # 读取页数
                pageCount = read_pdf_pages(upload_path)
                cost = pageCount*cost



        # 需要转换格式的文件
        else:
            # 先将文件保存再处理
            upload_path = os.path.join(parentdir, 'static/Upload_Files/BeforeSwitchFile/', secure_filename(new_filename))
            printfile.save(upload_path)

            # 对doc,ppt,xml文件转换，以及文件页数读取
            switch = switch_topdf(upload_path)
            if switch == 0:
                i = new_filename.rindex(".")
                new_filename = new_filename[:i]+".pdf"
                switched_dir = os.path.join(parentdir, 'static/Upload_Files', secure_filename(new_filename))  # 转换pdf后的文件路径
                # 读取文件页数
                pageCount = read_pdf_pages(switched_dir)
                cost = pageCount*cost

            else:
                # 转换失败,返回用户文件格式不对
                error = 1
                return render_template('select.html', now=now, error=error)

        # 写入数据库
        user = User.query.filter(User.Tel_Number == g.current_userphone).first()
        order_forsql = Order()
        order_forsql.User_Id = user.Id
        order_forsql.File_Dir = new_filename
        order_forsql.File_Name = filename
        order_forsql.Time_Way = time_way
        order_forsql.Print_Place = place
        order_forsql.Print_Copies = copies
        order_forsql.Print_Direction = direction
        order_forsql.Print_Colour = colour
        order_forsql.Print_size = paper_size
        order_forsql.Print_way = print_way
        order_forsql.Print_Money = cost
        order_forsql.Print_Status = 0
        order_forsql.Print_pages = pageCount

        db.session.add(order_forsql)
        db.session.commit()

        param_order = Order.query.filter(Order.File_Dir == new_filename, Order.User_Id == user.Id).first()
        param = param_order.Id

        param = (float(param) + 111)*73*1.3

        tradeid = str(g.current_user.Tel_Number)+"_" + now
        data = {"printfile": printfile, "new_filename": new_filename, "place": place, "copies": copies, "direction": direction, "colour": colour, "paper_size": paper_size,
                "print_way": print_way, "time_way": time_way, "cost": cost, "pageCount": pageCount, "tradeid": new_filename}


        return render_template('confirm.html', data=data, param=param)

    return render_template('select.html', now=now)

@printer.route('/select2', methods=['GET', 'POST'])
def select2():
    global datetimes
    global now
    datetimes = datetime.datetime.now()
    now = str(datetimes.year)+"-"+str(datetimes.month)+"-"+str(datetimes.day)+"_"+str(datetimes.hour)+"-"+str(datetimes.minute)+"-"+str(datetimes.second)
    if request.method == 'POST':
        printfile = request.files['uploadfile']         # 文件
        place = request.form.get("place")               # 打印点
        copies = request.form.get("copies")             # 份数
        direction = request.form.get("direction")       # 排版方向
        colour = request.form.get("colour")             # 彩色或黑白
        paper_size = request.form.get("paper_size")     # 纸张大小
        print_way = request.form.get("print_way")       # 单双面
        time_way = request.form.get("time_way")         # 预约或自动排队
        pageCount = 1                                   # 文件页数
        cost = 0.2*int(copies)


        filename = printfile.filename
        index_point = filename.rindex(".")
        new_filename = str(g.current_user.Tel_Number)+"_" + now + filename[index_point:]
        # basepath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        basepath = os.path.abspath(os.path.dirname(__file__))       # 当前文件所在目录
        parentdir = os.path.dirname(basepath)                       # 父级目录
        # 判断文件类型

        # 识别不需要转换的文件

        if filename[index_point:] in [".pdf", ".jpg", ".png", "jpeg"]:
            upload_path = os.path.join(parentdir, 'static/Upload_Files', secure_filename(new_filename))
            printfile.save(upload_path)

            if filename[index_point:] != '.pdf':        # 图片文件一律按1页处理
                pageCount = 1
                cost = pageCount*cost
            else:
                # 读取页数
                pageCount = read_pdf_pages(upload_path)
                cost = pageCount*cost



        # 需要转换格式的文件
        else:
            # 先将文件保存再处理
            upload_path = os.path.join(parentdir, 'static/Upload_Files/BeforeSwitchFile/', secure_filename(new_filename))
            printfile.save(upload_path)

            # 对doc,ppt,xml文件转换，以及文件页数读取
            switch = switch_topdf(upload_path)
            if switch == 0:
                i = new_filename.rindex(".")
                new_filename = new_filename[:i]+".pdf"
                switched_dir = os.path.join(parentdir, 'static/Upload_Files', secure_filename(new_filename))  # 转换pdf后的文件路径
                # 读取文件页数
                pageCount = read_pdf_pages(switched_dir)
                cost = pageCount*cost

            else:
                # 转换失败,返回用户文件格式不对
                error = 1
                return render_template('select.html', now=now, error=error)

        # 写入数据库
        user = User.query.filter(User.Tel_Number == g.current_userphone).first()
        order_forsql = Order()
        order_forsql.User_Id = user.Id
        order_forsql.File_Dir = new_filename
        order_forsql.File_Name = filename
        order_forsql.Time_Way = time_way
        order_forsql.Print_Place = place
        order_forsql.Print_Copies = copies
        order_forsql.Print_Direction = direction
        order_forsql.Print_Colour = colour
        order_forsql.Print_size = paper_size
        order_forsql.Print_way = print_way
        order_forsql.Print_Money = cost
        order_forsql.Print_Status = 0
        order_forsql.Print_pages = pageCount

        db.session.add(order_forsql)
        db.session.commit()

        param_order = Order.query.filter(Order.File_Dir == new_filename, Order.User_Id == user.Id).first()
        param = param_order.Id

        param = (float(param) + 111)*73*1.3

        tradeid = str(g.current_user.Tel_Number)+"_" + now
        data = {"printfile": printfile, "new_filename": new_filename, "place": place, "copies": copies, "direction": direction, "colour": colour, "paper_size": paper_size,
                "print_way": print_way, "time_way": time_way, "cost": cost, "pageCount": pageCount, "tradeid": new_filename}


        return render_template('confirm.html', data=data, param=param)

    return render_template('select.html', now=now)

@printer.route('/get_printer_status', methods=['POST'])
def get_printer_status():
    r = redis.Redis(host=RedisConfig.host,
                    password=RedisConfig.password,
                    port=RedisConfig.port,
                    db=0,
                    decode_responses=True)
    status = int(r.lindex(RedisConfig.REDIS_PRINTER_KEY, 2))
    status = {'status': status}
    return jsonify(status)