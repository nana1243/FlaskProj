# flask 모듈 임포트
from flask import Flask, render_template, request
# db 모듈 임포트
import db
from flask import Blueprint
from flask_paginate import Pagination, get_page_parameter

# 지도에 필요한 임포트
import pandas as pd
import folium


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

###########################cu ##########################################
# cu_search
@app.route('/search_cu_list')
def search_cu_list():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'CU')
        return render_template('allList.html', productList=productList)


#cu_one/two/three/dum

@app.route('/cu_oneplusone/<int:page>', methods=['GET'])
def cu_oneplusone_list(page):
    if db.get_oneplusone_list_totCnt == 0:
        message = "해당 상품이 없습니다."
    else:
        message = "총 " + str(db.get_oneplusone_list_totCnt('df_cu_oneplusone')) + "개 입니다."
    data = "cu_oneplusone"
    oneplusone_list= db.get_oneplusone_list('df_cu_oneplusone', page)
    num = db.get_oneplusone_list_totCnt('df_cu_oneplusone')
    pagenum= (num//20)+2
    return render_template('cu_list.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data , message=message, active = 'cu_oneplusone')


@app.route('/cu_twoplusone/<int:page>', methods=['GET'])
def cu_twoplusone_list(page):
    data = "cu_twoplusone"
    oneplusone_list= db.get_oneplusone_list('df_cu_twoplusone', page)
    if db.get_oneplusone_list_totCnt == 0:
        message = "해당 상품이 없습니다."
    else:
        message = "총 " + str(db.get_oneplusone_list_totCnt('df_cu_twoplusone')) + "개 입니다."
    num = db.get_oneplusone_list_totCnt('df_cu_twoplusone')
    pagenum= (num//20)+2
    return render_template('cu_list.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data,message=message, active = 'cu_twoplusone')


@app.route('/cu_threeplusone/<int:page>', methods=['GET'])
def cu_threeplusone_list(page):
    data = "cu_threeplusone"
    oneplusone_list= db.get_oneplusone_list('df_cu_threeplusone', page)
    if db.get_oneplusone_list_totCnt == 0:
        message = "해당 상품이 없습니다."
    else:
        message = "총 " + str(db.get_oneplusone_list_totCnt('df_cu_threeplusone')) + "개 입니다."
    num = db.get_oneplusone_list_totCnt('df_cu_threeplusone')
    pagenum= (num//20)+2
    return render_template('cu_list.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data,message=message, active = 'cu_threeplusone')

@app.route('/cu_dum/<int:page>', methods=['GET'])
def cu_dum_list(page):
    data = "cu_dum"
    oneplusone_list= db.get_dum_list('df_cu_dum', page)
    num = db.get_oneplusone_list_totCnt('df_cu_dum')
    if db.get_oneplusone_list_totCnt == 0:
        message = "해당 상품이 없습니다."
    else:
        message = "총 " + str(db.get_oneplusone_list_totCnt('df_cu_dum')) + "개 입니다."
    pagenum= (num//20)+2
    return render_template('cu_list.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data,message=message, active = 'cu_dum')

@app.route('/cu_discount/<int:page>', methods=['GET'])
def cu_discount_list(page):
    data = "cu_discount"
    oneplusone_list= db.get_dum_list('df_cu_discount', page)
    num = db.get_oneplusone_list_totCnt('df_cu_discount')
    if db.get_oneplusone_list_totCnt == 0:
        message = "해당 상품이 없습니다."
    else:
        message = "총 " + str(db.get_oneplusone_list_totCnt('df_cu_discount')) + "개 입니다."
    pagenum= (num//20)+2
    return render_template('cu_list.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data,message=message, active = 'cu_discount')


########################### seven11 ##########################################

#seven11_search

@app.route('/search_seven_list')
def search_seven_list():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'seven')
        return render_template('allList.html', productList=productList)

# seven11 oneplusone + twoplusone +dum+ discount

@app.route('/seven_oneplusone/<int:page>', methods=['GET'])
def seven_oneplusone_list(page):
    data = "seven_oneplusone"
    if db.get_oneplusone_list_totCnt == 0:
        message = "해당 상품이 없습니다."
    else:
        message = "총 " + str(db.get_oneplusone_list_totCnt('df_seven11_oneplusone')) + "개 입니다."
    oneplusone_list= db.get_oneplusone_list('df_seven11_oneplusone', page)
    num = db.get_oneplusone_list_totCnt('df_seven11_oneplusone')
    pagenum= (num//20)+2
    return render_template('seven_list.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data,message=message, active = 'seven_oneplusone')



@app.route('/seven_twoplusone/<int:page>', methods=['GET'])
def seven_twoplusone_list(page):
    data = "seven_twoplusone"
    if db.get_oneplusone_list_totCnt == 0:
        message = "해당 상품이 없습니다."
    else:
        message = "총 " + str(db.get_oneplusone_list_totCnt('df_seven11_twoplusone')) + "개 입니다."
    oneplusone_list= db.get_oneplusone_list('df_seven11_twoplusone', page)
    num = db.get_oneplusone_list_totCnt('df_seven11_twoplusone')
    pagenum= (num//20)+2
    return render_template('seven_list.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data,message=message, active = 'seven_twoplusone')

@app.route('/seven_dum/<int:page>', methods=['GET'])
def seven_dum_list(page):
    data = "seven_dum"
    conv_name="seven"
    oneplusone_list= db.get_dum_list('df_seven11_dum', page)
    num = db.get_oneplusone_list_totCnt('df_seven11_dum')
    if db.get_oneplusone_list_totCnt == 0:
        message = "해당 상품이 없습니다."
    else:
        message = "총 " + str(db.get_oneplusone_list_totCnt('df_seven11_dum')) + "개 입니다."
    pagenum= (num//12)+2
    return render_template('seven_list.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data,message=message,conv_name=conv_name, active = 'seven_dum')


@app.route('/seven_discount/<int:page>', methods=['GET'])
def seven_discount_list(page):
    data = "seven_discount"
    if db.get_oneplusone_list_totCnt == 0:
        message = "해당 상품이 없습니다."
    else:
        message = "총 " + str(db.get_oneplusone_list_totCnt('df_seven11_discount')) + "개 입니다."
    oneplusone_list= db.get_oneplusone_list('df_seven11_discount', page)
    num = db.get_oneplusone_list_totCnt('df_seven11_discount')
    pagenum= (num//20)+2
    return render_template('seven_list.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data,message=message, active = 'seven_discount')

################### ministop####################################


# search for ministop
@app.route('/search_ministop_list')
def search_ministop_list():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        productList = db.get_AllProductList(searchProduct, 'ministop')
        return render_template('allList.html', productList=productList)


# ministop 1+1,2+1,discount,dum

@app.route('/ministop_oneplusone/<int:page>', methods=['GET'])
def ministop_oneplusone_list(page):
    data = "ministop_oneplusone"
    if db.get_oneplusone_list_totCnt == 0:
        message = "해당 상품이 없습니다."
    else:
        message = "총 " + str(db.get_oneplusone_list_totCnt('df_ministop_oneplusone')) + "개 입니다."
    oneplusone_list= db.get_oneplusone_list('df_ministop_oneplusone', page)
    num = db.get_oneplusone_list_totCnt('df_ministop_oneplusone')
    pagenum= (num//20)+2
    return render_template('ministop_list.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data,message=message, active = 'ministop_oneplusone')

@app.route('/ministop_twoplusone/<int:page>', methods=['GET'])
def ministop_twoplusone_list(page):
    data = "ministop_twoplusone"
    oneplusone_list= db.get_oneplusone_list('df_ministop_twoplusone', page)
    if db.get_oneplusone_list_totCnt == 0:
        message = "해당 상품이 없습니다."
    else:
        message = "총 " + str(db.get_oneplusone_list_totCnt('df_ministop_twoplusone')) + "개 입니다."
    num = db.get_oneplusone_list_totCnt('df_ministop_twoplusone')
    pagenum= (num//20)+2
    return render_template('ministop_list.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data,message=message, active = 'ministop_twoplusone')

@app.route('/ministop_dum/<int:page>', methods=['GET'])
def ministop_dum_list(page):
    data = "ministop_dum"
    oneplusone_list= db.get_dum_list('df_ministop_dum', page)
    num = db.get_oneplusone_list_totCnt('df_ministop_dum')
    conv_name="ministop"
    if db.get_oneplusone_list_totCnt == 0:
        message = "해당 상품이 없습니다."
    else:
        message = "총 " + str(db.get_oneplusone_list_totCnt('df_ministop_dum')) + "개 입니다."
    pagenum= (num//20)+2
    return render_template('ministop_list.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data,message=message,conv_name=conv_name, active = 'ministop_dum')

@app.route('/ministop_discount/<int:page>', methods=['GET'])
def ministop_discount_list(page):
    print(page)
    data = "ministop_discount"
    oneplusone_list= db.get_oneplusone_list('df_ministop_discount', page)
    if db.get_oneplusone_list_totCnt == 0:
        message = "해당 상품이 없습니다."
    else:
        message = "총 " + str(db.get_oneplusone_list_totCnt('df_ministop_discount')) + "개 입니다."
    num = db.get_oneplusone_list_totCnt('df_ministop_discount')
    pagenum= (num//20)+2
    return render_template('ministop_list.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data,message=message, active = 'ministop_discount')


##############################gs25################################

# gs search list
@app.route('/search_gs_list')
def search_gs_list():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'gs')
        return render_template('allList.html', productList=productList)

# gs의 1+1,2+1,....

@app.route('/gs25_oneplusone/<int:page>', methods=['GET'])
def gs25_oneplusone_list(page):
    data = "gs25_oneplusone"
    oneplusone_list= db.get_oneplusone_list('df_gs25_oneplusone', page)
    num = db.get_oneplusone_list_totCnt('df_gs25_oneplusone')
    if db.get_oneplusone_list_totCnt == 0:
        message = "해당 상품이 없습니다."
    else:
        message = "총 " + str(db.get_oneplusone_list_totCnt('df_gs25_oneplusone')) + "개 입니다."
    pagenum= (num//20)+2
    return render_template('gs_list.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data,message=message, active = 'gs25_oneplusone')

@app.route('/gs25_twoplusone/<int:page>', methods=['GET'])
def gs25_twoplusone_list(page):
    data = "gs25_twoplusone"
    oneplusone_list= db.get_oneplusone_list('df_gs25_twoplusone', page)
    if db.get_oneplusone_list_totCnt == 0:
        message = "해당 상품이 없습니다."
    else:
        message = "총 " + str(db.get_oneplusone_list_totCnt('df_gs25_twoplusone')) + "개 입니다."
    num = db.get_oneplusone_list_totCnt('df_gs25_twoplusone')
    pagenum= (num//20)+2
    return render_template('gs_list.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data,message=message, active = 'gs25_twoplusone')



@app.route('/gs25_threeplusone/<int:page>', methods=['GET'])
def gs25_threeplusone_list(page):
    data = "gs25_threeplusone"
    oneplusone_list= db.get_oneplusone_list('df_gs25_threeplusone', page)
    if db.get_oneplusone_list_totCnt == 0:
        message = "해당 상품이 없습니다."
    else:
        message = "총 " + str(db.get_oneplusone_list_totCnt('df_gs25_threeplusone')) + "개 입니다."
    num = db.get_oneplusone_list_totCnt('df_gs25_threeplusone')
    pagenum= (num//20)+2
    return render_template('gs_list.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data,message=message, active = 'gs25_threeplusone')


@app.route('/gs25_dum/<int:page>', methods=['GET'])
def gs25_dum_list(page):
    data = "gs25_dum"
    conv_name="gs25"
    if db.get_oneplusone_list_totCnt == 0:
        message = "해당 상품이 없습니다."
    else:
        message = "총 " + str(db.get_oneplusone_list_totCnt('df_gs25_dum')) + "개 입니다."
    oneplusone_list= db.get_dum_list('df_gs25_dum', page)
    num = db.get_oneplusone_list_totCnt('df_gs25_dum')
    pagenum= (num//20)+2
    return render_template('gs_list.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data,message=message,conv_name=conv_name, active = 'gs25_dum')

@app.route('/gs25_discount/<int:page>', methods=['GET'])
def gs25_discount_list(page):
    data = "gs25_discount"
    if db.get_oneplusone_list_totCnt == 0:
        message = "해당 상품이 없습니다."
    else:
        message = "총 " + str(db.get_oneplusone_list_totCnt('df_gs25_discount')) + "개 입니다."
    oneplusone_list= db.get_oneplusone_list('df_gs25_discount', page)
    num = db.get_oneplusone_list_totCnt('df_gs25_discount')
    pagenum= (num//20)+2
    return render_template('dum.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data,message=message, active = 'gs25_discount')




################################## emart24###############################################


# search for emart24
@app.route('/search_emart_list')
def search_emart_list():
    if request.method == 'GET':
        searchProduct = request.args.get('searchProduct')
        print(searchProduct)
        productList = db.get_AllProductList(searchProduct, 'emart')
        return render_template('allList.html', productList=productList)

# emart24 1+1,2+1,.....

@app.route('/emart24_oneplusone/<int:page>', methods=['GET'])
def emart24_oneplusone_list(page):
    data = "emart24_oneplusone"
    if db.get_oneplusone_list_totCnt == 0:
        message = "해당 상품이 없습니다."
    else:
        message = "총 " + str(db.get_oneplusone_list_totCnt('df_emart24_oneplusone')) + "개 입니다."
    oneplusone_list= db.get_oneplusone_list('df_emart24_oneplusone', page)
    num = db.get_oneplusone_list_totCnt('df_emart24_oneplusone')
    pagenum= (num//20)+2
    return render_template('emart_list.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data,message=message, active = 'emart24_oneplusone')

@app.route('/emart24_twoplusone/<int:page>', methods=['GET'])
def emart24_twoplusone_list(page):
    data = "emart24_twoplusone"
    oneplusone_list= db.get_oneplusone_list('df_emart24_twoplusone', page)
    if db.get_oneplusone_list_totCnt == 0:
        message = "해당 상품이 없습니다."
    else:
        message = "총 " + str(db.get_oneplusone_list_totCnt('df_emart24_twoplusone')) + "개 입니다."
    num = db.get_oneplusone_list_totCnt('df_emart24_twoplusone')
    pagenum= (num//20)+2
    return render_template('emart_list.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data,message=message, active = 'emart24_twoplusone')

@app.route('/emart24_threeplusone/<int:page>', methods=['GET'])
def emart24_threeplusone_list(page):
    data = "emart24_threeplusone"
    oneplusone_list= db.get_oneplusone_list('df_emart24_threeplusone', page)
    num = db.get_oneplusone_list_totCnt('df_emart24_threeplusone')
    if db.get_oneplusone_list_totCnt == 0:
        message = "해당 상품이 없습니다."
    else:
        message = "총 " + str(db.get_oneplusone_list_totCnt('df_emart24_threeplusone')) + "개 입니다."
    pagenum= (num//20)+2
    return render_template('emart_list.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data,message=message, active = 'emart24_threeplusone')

@app.route('/emart24_dum/<int:page>', methods=['GET'])
def emart24_dum_list(page):
    data = "emart24_dum"
    conv_name="emart24"
    if db.get_oneplusone_list_totCnt == 0:
        message = "해당 상품이 없습니다."
    else:
        message = "총 " + str(db.get_oneplusone_list_totCnt('df_emart24_dum')) + "개 입니다."
    oneplusone_list= db.get_dum_list('df_emart24_dum', page)
    num = db.get_oneplusone_list_totCnt('df_emart24_dum')
    pagenum= (num//20)+2
    return render_template('emart_list.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data,message=message,conv_name=conv_name, active = 'emart24_dum')

@app.route('/emart24_discount/<int:page>', methods=['GET'])
def emart24_discount_list(page):
    data = "emart24_discount"
    if db.get_oneplusone_list_totCnt == 0:
        message = "해당 상품이 없습니다."
    else:
        message = "총 " + str(db.get_oneplusone_list_totCnt('df_emart24_discount')) + "개 입니다."
    oneplusone_list= db.get_oneplusone_list('df_emart24_discount', page)
    num = db.get_oneplusone_list_totCnt('df_emart24_discount')
    pagenum= (num//20)+2
    return render_template('emart_list.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data,message=message, active = 'emart24_discount')


###############################게시판 목록##########################3

@app.route('/board/', methods=['GET'])
@app.route('/board/<int:page>', methods=['GET'])
def board_list(page=None):
    if page == None:
       page = 1

    board_list = db.get_board_list('df_board', page)
    num = db.get_board_list_totCnt('df_board')
    pagenum = (num // 10) + 2
    return render_template('board.html', board_list=board_list, num=num, pagenum=pagenum, curpage=page, active='board')



# 게시판 추가
@app.route('/add_board_pro', methods=['post'])
def add_board_pro():
    a_title = request.form['title']
    a_content = request.form['content']
    a_name = request.form['name']

    # db.py 에 레코드를 추가하는 함수 등록
    db.addDb_board(a_title, a_content, a_name)
    return render_template('board.html', active='board')


@app.route('/add_board')
def add_board():
    return render_template('add_board.html', active='board')


@app.route('/detail', methods=['GET'])
def detailed():
    data = request.args['data']
    data = int(data)
    board_record = db.get_board_record('df_board', data)
    return render_template('board_content.html', board_record=board_record, active='board')

#####################################위치 서비스 ###################################################

@app.route('/location_service')
def location_service():
    return render_template('location_service.html')

@app.route('/map/', methods=["GET", "POST"])

@app.route('/map/<store>', methods=["GET", "POST"])
def showMap(store=None):
    if store == None:
        store = "gs25"

    gs_loc = pd.read_csv("C:/workspace/data/" + store + "_location_upgrade.csv", index_col=0, encoding="utf-8")

    if request.method == "POST":
        gugun = request.form['gugun']
        print(gugun)
        gs_loc = gs_loc[gs_loc['구'] == gugun]

    map = folium.Map(location=[gs_loc['위도'].mean(), gs_loc['경도'].mean()], zoom_start=13)

    for n in gs_loc.index:

        if pd.notnull(gs_loc['위도'][n]):
            popup_name = gs_loc['지점명'][n] + ' - ' + gs_loc['주소'][n]

            if store == 'cu':
                icon_color = 'darkpurple'

            elif store == 'gs25':
                icon_color = 'lightblue'

            elif store == 'emart24':
                icon_color = 'gray'

            elif store == '7eleven':
                icon_color = 'green'

            else:
                icon_color = 'darkblue'

            folium.Marker([gs_loc['위도'][n],
                           gs_loc['경도'][n]],
                          popup=popup_name,
                          icon=folium.Icon(color=icon_color)).add_to(map)

    return map._repr_html_()





# 앱 실행  --> 마지막 위치 유지
# 웹주소와 포트 지정
app.run(host='127.0.0.1', port=5001, debug=True)