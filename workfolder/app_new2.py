# flask 모듈 임포트
from flask import Flask, render_template, request
# db 모듈 임포트
import db


# flask 객체 생성
app = Flask(__name__)

# 라우터 등록 => 웹상 루트 주소 생성
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cu_oneplusone/<int:page>', methods=['GET'], defaults={"page": 1})
def cu_oneplusone_list(page):
    oneplusone_list= db.get_oneplusone_list('df_cu_oneplusone', page)
    num=len(oneplusone_list)
    data="cu"
    return render_template('oneplusone_list_new4.html', oneplusone_list=oneplusone_list, num=num, data="cu")

# @app.route('/cu_oneplusone/<int:page>', methods=['GET'])
# def pagination(page):
#     page = page
#     per_page = 5
#     users = User.query.paginate(page,per_page,error_out=False)
#     return render_template("oneplusone_list_new4.html", users=users)

# @app.route('/cu_oneplusone/<int:page>',methods=['GET'])
# def view(page=1):
#     per_page = 10
#     posts = Posts.query.order_by(Posts.time.desc()).paginate(page,per_page,error_out=False)
#     return render_template('oneplusone_list.html',posts=posts)






@app.route('/mini_oneplusone')
def ministop_oneplusone_list():
    data = ministop
    oneplusone_list= db.get_oneplusone_list('df_ministop_oneplusone')
    num = len(oneplusone_list)
    return render_template('oneplusone_list.html', oneplusone_list=oneplusone_list,num=num, data=data)



@app.route('/twoplusone_list')
def twoplusone_list():
    # 데이타베이스 레코드 출력 함수 호출
    twoplusone_list= db.get_twoplusone_list()
    # print(country_list)
    # return 'Success'
    return render_template('twoplusone_list.html', twoplusone_list=twoplusone_list)

@app.route('/dum_list')
def dum_list():
    # 데이타베이스 레코드 출력 함수 호출
    dum_list= db.get_dum_list()
    # print(country_list)
    # return 'Success'
    return render_template('dum_list.html', dum_list=dum_list)


@app.route('/discount_list')
def discount_list():
    # 데이타베이스 레코드 출력 함수 호출
    discount_list= db.get_discount_list()
    # print(country_list)
    # return 'Success'
    return render_template('discount_list.html', discount_list=discount_list)







# 앱 실행  --> 마지막 위치 유지
# 웹주소와 포트 지정
app.run(host='127.0.0.1', port=5001, debug=True)