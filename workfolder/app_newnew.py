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

@app.route('/seven_oneplusone/', methods=['GET'])
@app.route('/seven_oneplusone/<int:page>', methods=['GET'])
def seven_oneplusone_list(page=None):
    if page == None:
        page = 1
    print(page)
    if db.get_oneplusone_list_totCnt == 0:
        message = "해당 상품이 없습니다."
    else :
        message = "총 " + db.table_check('df_seven11_oneplusone') + "개 입니다."
    data = "seven"
    oneplusone_list= db.get_oneplusone_list('df_seven11_oneplusone', page)
    num = db.get_oneplusone_list_totCnt('df_seven11_oneplusone')
    pagenum= (num//20)+2
    return render_template('seven_oneplusone.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data, active='seven_oneplusone', message=message)

@app.route('/gs25_threeplusone/', methods=['GET'])
@app.route('/gs25_threeplusone/<int:page>', methods=['GET'])
def gs25_oneplusone_list(page=None):
    if page == None:
        page = 1
    print(page)
    if db.get_oneplusone_list_totCnt('df_gs25_threeplusone') == 0:
        message = "해당 상품이 없습니다."
    else :
        message = "총 " + str(db.get_oneplusone_list_totCnt('df_gs25_threeplusone')) + "개 입니다."
    data = "seven"
    oneplusone_list= db.get_oneplusone_list('df_gs25_threeplusone', page)
    num = db.get_oneplusone_list_totCnt('df_gs25_threeplusone')
    pagenum= (num//20)+2
    return render_template('gs25_threeplusone.html', oneplusone_list=oneplusone_list, num=num, pagenum=pagenum, curpage=page, data=data, active='seven_oneplusone', message=message)


####################################################################################


# 게시판 목록

@app.route('/board/', methods=['GET'])
@app.route('/board/<int:page>', methods=['GET'])
def board_list(page=None):
    if page == None:
       page = 1
    print(page)

    board_list = db.get_board_list('df_board', page)
    num = db.get_board_list_totCnt('df_board')
    pagenum = (num // 10) + 2
    # print(board_list)
    # return 'Success'
    print(board_list)
    return render_template('board.html', board_list=board_list, num=num, pagenum=pagenum, curpage=page, active='board')



# 게시판 추가
@app.route('/add_board_pro', methods=['post'])
def add_board_pro():
    a_title = request.form['title']
    a_content = request.form['content']
    a_name = request.form['name']


    print(a_title, a_name)
    # db.py 에 레코드를 추가하는 함수 등록
    db.addDb_board(a_title, a_content, a_name)


    return render_template('board.html')

@app.route('/add_board')
def add_board():
    return render_template('add_board.html')

'''
@app.route('/board_content', methods=['POST'])
def board_content() :
    board_list = db.get_board_list()
    # print(board_list)
    # return 'Success'
    print(board_list)
    return render_template('board_content.htmlSample', board_list=board_list)
'''

@app.route('/detail', methods=['GET'])
def detailed():
    data = request.args['data']
    data = int(data)
    board_record = db.get_board_record('df_board', data)

    # borad_list = db.get_board_list('df_board')
    return render_template('board_content.html', board_record=board_record)




# 앱 실행  --> 마지막 위치 유지
# 웹주소와 포트 지정
app.run(host='127.0.0.1', port=5001, debug=True)