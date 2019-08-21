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


#oneplusone_list

@app.route('/cu_oneplusone/<int:page>', methods=['GET'])
def cu_oneplusone_list(page):
    print(page)
    data = "cu"
    oneplusone_list= db.get_oneplusone_list('df_cu_oneplusone', page)
    num = db.get_oneplusone_list_totCnt('df_cu_oneplusone')
    pagenum= (num//20)+2
    return render_template('oneplusone_list_new4.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data)


@app.route('/seven11_oneplusone/<int:page>', methods=['GET'])
def seven_oneplusone_list(page):
    print(page)
    data = "seven11"
    oneplusone_list= db.get_oneplusone_list('df_seven11_oneplusone', page)
    num = db.get_oneplusone_list_totCnt('df_seven11_oneplusone')
    pagenum= (num//20)+2
    return render_template('oneplusone_list_new4.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data)


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