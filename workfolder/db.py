import pymysql

# 데이타베이스 접속 함수
def get_connection():
    conn = pymysql.connect(
        host='database-1.cb6f1qkai8d4.us-east-2.rds.amazonaws.com',
        user = 'root',
        password = '12341234',
        db='conv_db',
        charset='utf8')

    return conn

# 레코드를 출력하는 함수


def get_AllProductList(searchProduct, name2):
    conn = get_connection()
    cursor = conn.cursor()
    if len(name2) < 1:
        sql = " SELECT * from df_all where 품명 like '%" + searchProduct + "%'"
    else:

        sql = " SELECT * from df_all where 편의점 =" + "'" + name2 + "'" + "and 품명 like '%" + searchProduct + "%'"

    cursor.execute(sql)

    # 리스트 생성

    productList = cursor.fetchall()

    print(productList)
    # 데이타베이스 종료

    conn.close()

    return productList

def get_oneplusone_list(df_name_oneplusone, page):

    # 데이타베이스 접속함수 호출
    conn = get_connection()
    # 작업변수 생성
    cursor = conn.cursor()
    print(page)
    page=(int(page)-1)*20
    page = str(page)
    sql = 'SELECT 품명, 가격, img from ' + df_name_oneplusone + ' LIMIT '+ page + ',20';
    cursor.execute(sql)
    oneplusone_list= cursor.fetchall()
    print(oneplusone_list)
    # 데이타베이스 종료
    conn.close()
    return oneplusone_list
    # 데이타베이스 종료
    conn.close()

    return oneplusone_list

def get_oneplusone_list_totCnt(df_name_oneplusone):

    # 데이타베이스 접속함수 호출
    conn = get_connection()

    # 작업변수 생성
    cursor = conn.cursor()
    sql = 'SELECT count(*) FROM ' + df_name_oneplusone ;
    cursor.execute(sql)
    totCnt= cursor.fetchone()
    print(totCnt[0])

    # 데이타베이스 종료
    conn.close()

    return int(totCnt[0])





