# flask 모듈 임포트
from flask import Flask, render_template, request
# db 모듈 임포트
import db

from flask import Blueprint
from flask_paginate import Pagination, get_page_parameter



# flask 객체 생성
app = Flask(__name__)

# 인덱스
@app.route('/')
def index():
    return render_template('index.html')




# 메인 검색창

@app.route('/search_list')
def search_list():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, '')
        return render_template('allList.html', productList=productList)

# cu_search

@app.route('/search_cu_list1')
def search_cu_list1():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'CU1')
        return render_template('oneplusone.html', productList=productList)

@app.route('/search_cu_list2')
def search_cu_list2():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'CU2')
        return render_template('oneplusone.html', productList=productList)

@app.route('/search_cu_list3')
def search_cu_list3():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'CU3')
        return render_template('oneplusone.html', productList=productList)


@app.route('/search_cu_list4')
def search_cu_list4():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'CU4')
        return render_template('oneplusone.html', productList=productList)



#cu_one/two/three/dum

@app.route('/cu_oneplusone/<int:page>', methods=['GET'])
def cu_oneplusone_list(page):
    print(page)
    conv_name = "CU"
    data = "cu_oneplusone"
    oneplusone_list= db.get_oneplusone_list('df_cu_oneplusone', page)
    num = db.get_oneplusone_list_totCnt('df_cu_oneplusone')
    pagenum= (num//20)+2
    return render_template('oneplusone.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data)


@app.route('/cu_twoplusone/<int:page>', methods=['GET'])
def cu_twoplusone_list(page):
    data = "cu_twoplusone"
    oneplusone_list= db.get_oneplusone_list('df_cu_twoplusone', page)
    print("appppppp")
    print(page)
    print(oneplusone_list)
    num = db.get_oneplusone_list_totCnt('df_cu_twoplusone')
    pagenum= (num//20)+2
    return render_template('oneplusone.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data)


@app.route('/cu_threeplusone/<int:page>', methods=['GET'])
def cu_threeplusone_list(page):
    data = "cu_threeplusone"
    oneplusone_list= db.get_oneplusone_list('df_cu_threeplusone', page)
    num = db.get_oneplusone_list_totCnt('df_cu_threeplusone')
    pagenum= (num//20)+2
    return render_template('oneplusone.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data)

########## seven11

@app.route('/search_seven_list1')
def search_seven_list1():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'seven1')
        return render_template('oneplusone.html', productList=productList)

@app.route('/search_seven_list2')
def search_seven_list2():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'seven2')
        return render_template('oneplusone.html', productList=productList)

@app.route('/search_seven_list3')
def search_seven_list3():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'seven_dum')
        return render_template('oneplusone.html', productList=productList)


@app.route('/search_seven_list4')
def search_seven_list4():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'seven_dis')
        return render_template('oneplusone.html', productList=productList)



@app.route('/seven_oneplusone/<int:page>', methods=['GET'])
def seven_oneplusone_list(page):
    print(page)
    conv_name = "7eleven"
    data = "seven_oneplusone"
    oneplusone_list= db.get_oneplusone_list('df_seven11_oneplusone', page)
    num = db.get_oneplusone_list_totCnt('df_seven11_oneplusone')
    pagenum= (num//20)+2
    return render_template('oneplusone.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data, conv_name=conv_name)



@app.route('/seven_twoplusone/<int:page>', methods=['GET'])
def seven_twoplusone_list(page):
    print(page)
    conv_name="7eleven"
    data = "seven_twoplusone"
    oneplusone_list= db.get_oneplusone_list('df_seven11_twoplusone', page)
    num = db.get_oneplusone_list_totCnt('df_seven11_twoplusone')
    pagenum= (num//20)+2
    return render_template('oneplusone.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data, conv_name=conv_name)

@app.route('/seven_dum/<int:page>', methods=['GET'])
def seven_dum_list(page):
    print(page)
    data = "seven_dum"
    oneplusone_list= db.get_oneplusone_list('df_seven11_dum', page)
    num = db.get_oneplusone_list_totCnt('df_seven11_dum')
    pagenum= (num//20)+2
    return render_template('oneplusone.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data)


@app.route('/seven_discount/<int:page>', methods=['GET'])
def seven_discount_list(page):
    print(page)
    data = "seven_discount"
    oneplusone_list= db.get_oneplusone_list('df_seven11_discount', page)
    num = db.get_oneplusone_list_totCnt('df_seven11_discount')
    pagenum= (num//20)+2
    return render_template('oneplusone.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data)



@app.route('/mini_oneplusone/<int:page>',methods=['GET'])
def ministop_oneplusone_list(page):
    data = "ministop"
    oneplusone_list= db.get_oneplusone_list('df_ministop_oneplusone')
    pagenum = (num // 20) + 2
    return render_template('oneplusone_list_new4.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum,curpage=page, data=data)


@app.route('/gs25_oneplusone/<int:page>', methods=['GET'])
def gs25_oneplusone_list(page):
    data = "gs25"
    oneplusone_list= db.get_oneplusone_list('df_gs25_oneplusone', page)
    num = db.get_oneplusone_list_totCnt('df_gs25_oneplusone')
    pagenum= (num//20)+2
    return render_template('oneplusone_list_new4.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data)


@app.route('/emart24_oneplusone/<int:page>', methods=['GET'])
def emart24_oneplusone_list(page):
    print(page)
    data = "emart24"
    oneplusone_list= db.get_oneplusone_list('df_emart24_oneplusone', page)
    num = db.get_oneplusone_list_totCnt('df_emart24_oneplusone')
    pagenum= (num//20)+2
    return render_template('oneplusone_list_new4.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data)




# @app.route('/seven11_twoplusone/<int:page>', methods=['GET'])
# def seven_oneplusone_list(page):
#     print(page)
#     data = "seven11"
#     oneplusone_list= db.get_oneplusone_list('df_seven11_twoplusone', page)
#     num = db.get_oneplusone_list_totCnt('df_seven11_twoplusone')
#     pagenum= (num//20)+2
#     return render_template('oneplusone_list_new4.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data)
#
#
# @app.route('/mini_oneplusone/<int:page>',methods=['GET'])
# def ministop_oneplusone_list(page):
#     data = "ministop"
#     oneplusone_list= db.get_oneplusone_list('df_ministop_oneplusone')
#     pagenum = (num // 20) + 2
#     return render_template('oneplusone_list_new4.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum,curpage=page, data=data)
#
#
# @app.route('/gs25_oneplusone/<int:page>', methods=['GET'])
# def gs25_oneplusone_list(page):
#     data = "gs25"
#     oneplusone_list= db.get_oneplusone_list('df_gs25_oneplusone', page)
#     num = db.get_oneplusone_list_totCnt('df_gs25_oneplusone')
#     pagenum= (num//20)+2
#     return render_template('oneplusone_list_new4.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data)
#
#
# @app.route('/emart24_oneplusone/<int:page>', methods=['GET'])
# def emart24_oneplusone_list(page):
#     print(page)
#     data = "emart24"
#     oneplusone_list= db.get_oneplusone_list('df_emart24_oneplusone', page)
#     num = db.get_oneplusone_list_totCnt('df_emart24_oneplusone')
#     pagenum= (num//20)+2
#     return render_template('oneplusone_list_new4.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data)



@app.route('/board')
def borad_list():
    board_list = db.get_board_list()
    # print(board_list)
    # return 'Success'
    print(board_list)
    return render_template('board.html', board_list=board_list, active='board')


@app.route('/add_board_pro', methods=['post'])
def add_board_pro():
    a_title = request.form['a_title']
    a_content = request.form['a_content']
    a_writer = request.form['a_writer']


    print(a_title, a_writer)
    # db.py 에 레코드를 추가하는 함수 등록
    db.addDb_board(a_title, a_content, a_writer)


    return render_template('board.html')

@app.route('/board_content', methods=['POST'])
def board_content() :
    board_list = db.get_board_list()
    # print(board_list)
    # return 'Success'
    print(board_list)
    return render_template('board_content.html', board_list=board_list)


@app.route('/detailed')
def detailed():
    return render_template('board_content.html')

@app.route('/add_board')
def add_board():
    return render_template('add_board.html')










# 앱 실행  --> 마지막 위치 유지
# 웹주소와 포트 지정
app.run(host='127.0.0.1', port=5001, debug=True)