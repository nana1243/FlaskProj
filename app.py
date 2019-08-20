# flask 모듈 임포트
from flask import Flask, render_template, request
import db

from flask import Blueprint
from flask_paginate import Pagination, get_page_parameter
# flask 객체 생성
app = Flask(__name__)

# 라우터 등록 => 웹상 루트 주소 생성
@app.route('/')
def index():
    return render_template('index.html')

# 메인 검색창
@app.route('/search_list')
def search_list():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'CU')
        return render_template('allList.html', productList=productList)

# CU 목록표 + 검색창
@app.route('/cu_oneplusone')
def cu_oneplusone():
    productList = db.get_AllProductList('', "CU1")
    return render_template('cu_oneplusone.html', productList=productList)

@app.route('/search_cu_list1')
def search_cu_list1():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'CU1')
        return render_template('cu_oneplusone.html', productList=productList)

@app.route('/cu_twoplusone')
def cu_twoplusone():
    productList = db.get_AllProductList('', "CU2")
    return render_template('cu_twoplusone.html', productList=productList)

@app.route('/search_cu_list2')
def search_cu_list2():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'CU2')
        return render_template('cu_twoplusone.html', productList=productList)

@app.route('/cu_threeplusone')
def cu_threeplusone():
    productList = db.get_AllProductList('', "CU3")
    return render_template('cu_threeplusone.html', productList=productList)

@app.route('/search_cu_list3')
def search_cu_list3():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'CU3')
        return render_template('cu_threeplusone.html', productList=productList)

@app.route('/cu_dum')
def cu_dum():
    productList = db.get_AllProductList('', "CU4")
    return render_template('cu_dum.html', productList=productList)

@app.route('/search_cu_list4')
def search_cu_list4():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'CU4')
        return render_template('cu_dum.html', productList=productList)

# 7eleven
@app.route('/seven_oneplusone')
def seven_oneplusone():
    productList = db.get_AllProductList('', "seven1")
    return render_template('seven_oneplusone.html', productList=productList)

@app.route('/search_seven_list1')
def search_seven_list1():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'seven1')
        return render_template('seven_oneplusone.html', productList=productList)

@app.route('/seven_twoplusone')
def seven_twoplusone():
    productList = db.get_AllProductList('', "seven2")
    return render_template('seven_twoplusone.html', productList=productList)

@app.route('/search_seven_list2')
def search_seven_list2():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'seven2')
        return render_template('seven_twoplusone.html', productList=productList)

@app.route('/seven_dum')
def seven_dum():
    productList = db.get_AllProductList('', "seven_dum")
    return render_template('seven_dum.html', productList=productList)

@app.route('/search_seven_list3')
def search_seven_list3():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'seven_dum')
        return render_template('seven_dum.html', productList=productList)

@app.route('/seven_discount')
def seven_discount():
    productList = db.get_AllProductList('', "seven_dis")
    return render_template('seven_discount.html', productList=productList)

@app.route('/search_seven_list4')
def search_seven_list4():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'seven_dis')
        return render_template('seven_discount.html', productList=productList)

# ministop
@app.route('/ministop_oneplusone')
def ministop_oneplusone():
    productList = db.get_AllProductList('', "ministop1")
    return render_template('ministop_oneplusone.html', productList=productList)

@app.route('/search_ministop_list1')
def search_ministop_list1():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'ministop1')
        return render_template('ministop_oneplusone.html', productList=productList)

@app.route('/ministop_twoplusone')
def ministop_twoplusone():
    productList = db.get_AllProductList('', "ministop2")
    return render_template('ministop_twoplusone.html', productList=productList)

@app.route('/search_ministop_list2')
def search_ministop_list2():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'ministop2')
        return render_template('ministop_twoplusone.html', productList=productList)

@app.route('/ministop_dum')
def ministop_dum():
    productList = db.get_AllProductList('', "ministop_dum")
    return render_template('ministop_dum.html', productList=productList)

@app.route('/search_ministop_list3')
def search_ministop_list3():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'ministop_dum')
        return render_template('ministop_dum.html', productList=productList)

@app.route('/ministop_discount')
def ministop_discount():
    productList = db.get_AllProductList('', "ministop_dis")
    return render_template('ministop_discount.html', productList=productList)

@app.route('/search_ministop_list4')
def search_ministop_list4():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'ministop_dis')
        return render_template('ministop_discount.html', productList=productList)
# @app.route('/cu_oneplusone/<int:page>', methods=['GET'])
# def cu_oneplusone_list(page):
#     print(page)
#     oneplusone_list= db.get_oneplusone_list('df_cu_oneplusone', page)
#     num = db.get_oneplusone_list_totCnt('df_cu_oneplusone')
#     pagenum= (num//20)+2
#     return render_template('cu.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page)

@app.route('/gs25')
def gs():
    return render_template('gs25.html')


@app.route('/emart')
def mini():
    return render_template('emart.html')

# if __name__ == "__main__" :
#     app.run()

# 앱 실행  --> 마지막 위치 유지
# 웹주소와 포트 지정
app.run(host='127.0.0.1', port=1001, debug=True)

