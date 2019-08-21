from flask import Flask, render_template, request

import db

from flask import Blueprint
from flask_paginate import Pagination, get_page_parameter



# import flask_sqlalchemy

app = Flask(__name__)


# 홈
@app.route('/')
def index():
    return render_template('index.html', active='home')

# 세븐일레븐 ( 1+1, 2+1, 할인, 증정)
@app.route('/seven_oneplusone/', methods=['GET'])
@app.route('/seven_oneplusone/<int:page>', methods=['GET'])
def seven_oneplusone_list(page=None):
    if page == None:
        page = 1
    print(page)
    data = "seven"
    oneplusone_list= db.get_oneplusone_list('df_seven11_oneplusone', page)
    num = db.get_oneplusone_list_totCnt('df_seven11_oneplusone')
    pagenum= (num//20)+2
    return render_template('seven_oneplusone.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data, active='seven_oneplusone')

@app.route('/seven_twoplusone/', methods=['GET'])
@app.route('/seven_twoplusone/<int:page>', methods=['GET'])
def seven_twoplusone_list(page=None):
    if page == None:
        page = 1
    print(page)
    data = "seven"
    oneplusone_list= db.get_oneplusone_list('df_seven11_twoplusone', page)
    num = db.get_oneplusone_list_totCnt('df_seven11_twoplusone')
    pagenum= (num//20)+2
    return render_template('seven_twoplusone.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data, active='seven_twoplusone')


@app.route('/seven_threeplusone/', methods=['GET'])
@app.route('/seven_threeplusone/<int:page>', methods=['GET'])
def seven_threeplusone_list(page=None):
    if db.get_oneplusone_list('df_seven11_threeplusone', page) == -1:
        return render_template('seven_threeplusone.html', oneplusone_list = -1)
    else:
        if page == None:
            page = 1
        print(page)
        data = "seven"
        oneplusone_list= db.get_oneplusone_list('df_seven11_threeplusone', page)
        num = db.get_oneplusone_list_totCnt('df_seven11_threeplusone')
        pagenum= (num//20)+2
        return render_template('seven_threeplusone.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data, active='seven_threeplusone')

@app.route('/seven_discount/', methods=['GET'])
@app.route('/seven_discount/<int:page>', methods=['GET'])
def seven_discount_list(page=None):
    if page == None:
        page = 1
    print(page)
    data = "seven"
    oneplusone_list= db.get_oneplusone_list('df_seven11_discount', page)
    num = db.get_oneplusone_list_totCnt('df_seven11_discount')
    pagenum= (num//20)+2
    return render_template('seven_discount.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data, active='seven_discount')

@app.route('/seven_dum/', methods=['GET'])
@app.route('/seven_dum/<int:page>', methods=['GET'])
def seven_dum_list(page=None):
    if page == None:
        page = 1
    print(page)
    data = "seven"
    oneplusone_list= db.get_oneplusone_list('df_seven11_dum', page)
    num = db.get_oneplusone_list_totCnt('df_seven11_dum')
    pagenum= (num//20)+2
    return render_template('seven_dum.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data, active='seven_dum')

# 미니스탑(1+1)
@app.route('/ministop_oneplusone')
def ministop_oneplusone():
    productList = db.get_AllProductList('', "ministop1")
    print(productList)
    return render_template('ministop_oneplusone.html', productList=productList, active = 'ministop_oneplusone')

# 미니스탑 검색(1+1)
@app.route('/search_ministop_list1')
def search_ministop_list1():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList('', 'ministop1')
        return render_template('ministop_oneplusone.html', productList=productList)

# 미니스탑(2+1)
@app.route('/ministop_twoplusone')
def ministop_twoplusone():
    productList = db.get_AllProductList('', "ministop2")
    return render_template('ministop_twoplusone.html', productList=productList, active = 'ministop_twoplusone')


# 미니스탑(2+1) 검색
@app.route('/search_ministop_list2')
def search_ministop_list2():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'ministop2')
        return render_template('ministop_twoplusone.html', productList=productList)

# 미니스탑 증정
@app.route('/ministop_dum')
def ministop_dum():
    productList = db.get_AllProductList('', "ministop_dum")
    return render_template('ministop_dum.html', productList=productList, active = 'ministop_dum')

# 미니스탑 증정(검색)
@app.route('/search_ministop_list3')
def search_ministop_list3():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'ministop_dum')
        return render_template('ministop_dum.html', productList=productList)

# 미니스탑 할인
@app.route('/ministop_discount')
def ministop_discount():
    productList = db.get_AllProductList('', "ministop_dis")
    return render_template('ministop_discount.html', productList=productList, active = 'ministop_discount')

# 미니스탑 할인(검색)
@app.route('/search_ministop_list4')
def search_ministop_list4():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'ministop_dis')
        return render_template('ministop_discount.html', productList=productList)










@app.route('/add_board_pro', methods=['post'])
def add_board_pro():
    a_title = request.form['a_title']
    a_content = request.form['a_content']
    a_writer = request.form['a_writer']


    print(a_title, a_writer)
    # db.py 에 레코드를 추가하는 함수 등록
    db.addDb_board(a_title, a_content, a_writer)


    return render_template('board.html')



'''
@app.route('/board/', methods=['GET'])
@app.route('/board/<int:page>', methods=['GET'])
def board_list(page=None):
    if page == None:
        page = 1
def borad_list(page):
    # print(board_list)
    # return 'Success'
    print(page)
    data = "board"
    board_list = db.get_board_list('df_board', page)
    print(board_list)
    num = db.get_board_list_totCnt('df_board')
    pagenum = (num // 20) + 2
    return render_template('board.html', board_list=board_list, num=num, pagenum=pagenum, curpage=page, data=data, active='board')


@app.route('/board_content', methods=['POST'])
def board_content() :
    board_list = db.get_board_list()
    # print(board_list)
    # return 'Success'
    print(board_list)
    return render_template('board_content.html', board_list=board_list)

@app.route('/add_board')
def add_board():
    return render_template('add_board.html')
'''
'''
@app.route('/big_image', methods=['GET'])
def show_info():
    num = request.args['data']

    name_list = db.get_data('df_seven11_oneplusone', num)
    return render_template('big.html', name_list=name_list)
'''
# 앱 실행  --> 마지막 위치 유지
# # 웹주소와 포트 지정
app.run(host='127.0.0.1', port=5001, debug=True)