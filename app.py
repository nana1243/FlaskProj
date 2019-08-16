from flask import Flask, render_template, request

import db

app = Flask(__name__)

# 라우터 등록 => 웹상 루트 주소 생성
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cu_oneplusone')
def cu_oneplusone_list():
    # 데이타베이스 레코드 출력 함수 호출
    oneplusone_list= db.get_oneplusone_list('df_cu_oneplusone')
    num=len(oneplusone_list)
    data="cu"
    print(num)
    return render_template('oneplusone_list_new3.html', oneplusone_list=oneplusone_list, num=num, data="cu")


@app.route('/mini_oneplusone')
def ministop_oneplusone_list():
    data = "ministop"
    oneplusone_list= db.get_oneplusone_list('df_ministop_oneplusone')
    num = len(oneplusone_list)
    return render_template('oneplusone_list_3.html', oneplusone_list=oneplusone_list,num=num, data="ministop")




# 앱 실행  --> 마지막 위치 유지
# 웹주소와 포트 지정
app.run(host='127.0.0.1', port=5001, debug=True)