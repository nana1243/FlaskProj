import pymysql

# 데이타베이스 접속 함수
def get_connection():
    conn = pymysql.connect(
        host='127.0.0.1',
        user = 'root',
        password = '1234',
        db='conv_db',
        charset='utf8')

    return conn

# 레코드를 출력하는 함수



def get_oneplusone_list(df_name_oneplusone, page):

    # 데이타베이스 접속함수 호출
    conn = get_connection()

    # 작업변수 생성
    cursor = conn.cursor()
    print(page)
    page=(int(page)-1)*20
    page = str(page)
    sql = 'SELECT 품명, 가격, `index` as img FROM ' + df_name_oneplusone + ' LIMIT '+ page + ',20';
    cursor.execute(sql)
    oneplusone_list= cursor.fetchall()
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


def get_cu_size_big(df_name_oneplusone):
    # 데이타베이스 접속함수 호출
    conn = get_connection()
    cursor = conn.cursor()
    sql = 'SELECT 품명, 가격, `index` as img FROM ' + df_name_oneplusone
    cursor.execute(sql)
    size_big_list= cursor.fetchall()
    # 데이타베이스 종료
    conn.close()

    return size_big_list

get_cu_size_big("df_cu_oneplusone")




def get_twoplusone_list(df_name_twoplusone):

    # 데이타베이스 접속함수 호출
    conn = get_connection()

    # 작업변수 생성
    cursor = conn.cursor()

    # 쿼리문 생성
    sql = 'SELECT 품명, 가격, `index` as img FROM ' + df_name_twoplusone
    cursor.execute(sql)

    # 리스트 생성
    twoplusone_list= cursor.fetchall()
    #print(oneplusone_list)

    # 데이타베이스 종료
    conn.close()

    return twoplusone_list



def get_three_plusone_list(df_name_threeplusone):

    # 데이타베이스 접속함수 호출
    conn = get_connection()

    # 작업변수 생성
    cursor = conn.cursor()

    # 쿼리문 생성
    sql = 'SELECT 품명, 가격, `index` as img FROM ' + df_name_threeplusone
    cursor.execute(sql)

    # 리스트 생성
    twoplusone_list= cursor.fetchall()
    #print(oneplusone_list)

    # 데이타베이스 종료
    conn.close()

    return twoplusone_list



def get_dum_list(df_name_dum):

    # 데이타베이스 접속함수 호출
    conn = get_connection()

    # 작업변수 생성
    cursor = conn.cursor()

    # 쿼리문 생성
    sql = 'SELECT 품명, 가격, `index` as img FROM ' + df_name_dum

    cursor.execute(sql)

    # 리스트 생성
    dum_list= cursor.fetchall()

    # 데이타베이스 종료
    conn.close()

    return dum_list


def get_discount_list(df_name_discount):

    # 데이타베이스 접속함수 호출
    conn = get_connection()

    # 작업변수 생성
    cursor = conn.cursor()

    # 쿼리문 생성
    sql = 'SELECT 품명, 가격, `index` as img FROM ' + df_name_discount
    cursor.execute(sql)

    # 리스트 생성
    discount_list= cursor.fetchall()

    # 데이타베이스 종료
    conn.close()

    return discount_list

