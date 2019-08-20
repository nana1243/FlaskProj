from flask import Flask, render_template, request

import db

from flask import Blueprint
from flask_paginate import Pagination, get_page_parameter



# import flask_sqlalchemy

app = Flask(__name__)

# 라우터 등록 => 웹상 루트 주소 생성
@app.route('/')
def index():
    return render_template('index.html', active='home')

@app.route('/seven_oneplusone/<int:page>', methods=['GET'])
def seven_oneplusone_list(page):
    print(page)
    data = "seven"
    oneplusone_list= db.get_oneplusone_list('df_seven_oneplusone', page)
    num = db.get_oneplusone_list_totCnt('df_seven_oneplusone')
    pagenum= (num//20)+2
    return render_template('seven_oneplusone.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data)





@app.route('/mini_oneplusone')
def ministop_oneplusone_list():
    data = "ministop"
    oneplusone_list= db.get_oneplusone_list('df_ministop_oneplusone')
    num = len(oneplusone_list)
    return render_template('oneplusone_list_3.html', oneplusone_list=oneplusone_list,num=num, data="ministop")


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