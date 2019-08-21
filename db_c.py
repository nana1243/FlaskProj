import pymysql


# 데이타베이스 접속 함수
def get_connection():
    conn = pymysql.connect(
        host='database-1.cb6f1qkai8d4.us-east-2.rds.amazonaws.com',
        user='root',
        password='12341234',  # 자기 my sql 비번
        db='conv_db',  # 쓸 데이터베이스이름입력
        charset='utf8')  # 이거 다른지도 체크

    return conn


# 레코드를 출력하는 함수
def get_AllProductList(searchProduct, name2):
    # 데이타베이스 접속함수 호출
    conn = get_connection()

    # 작업변수 생성
    cursor = conn.cursor()

    # 쿼리문 생성
    # sql = "SELECT name, price, event from vw_productlist where name like '%" + searchProduct + "%' order by name asc"
    # sql = "SELECT * from df_cu_oneplusone where store = " + name2 + "and name like '%" + searchProduct + "%'"
    if len(name2) < 1:
        sql = " SELECT * from df_all where 품명 like '%" + searchProduct + "%'"
    else:
        sql = " SELECT * from df_all where 편의점 =" + "'" + name2 + "'" + "and 품명 like '%" + searchProduct + "%'"
    print("----------------------------------------------" + sql)
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
    sql = 'SELECT 품명, 가격, `index` as img FROM ' + df_name_oneplusone + ' LIMIT '+ page + ',20'
    cursor.execute(sql)
    oneplusone_list= cursor.fetchall()
    print(oneplusone_list)

    # 데이타베이스 종료
    conn.close()

    return oneplusone_list




def get_oneplusone_list_totCnt(df_name_oneplusone):

    # 데이타베이스 접속함수 호출
    conn = get_connection()

    # 작업변수 생성
    cursor = conn.cursor()
    sql = 'SELECT count(*) FROM ' + df_name_oneplusone
    cursor.execute(sql)
    totCnt= cursor.fetchone()
    print(totCnt[0])

    # 데이타베이스 종료
    conn.close()

    return int(totCnt[0])



# def get_EventProductList(event):
#     # 데이타베이스 접속함수 호출
#     conn = get_connection()
#
#     # 작업변수 생성
#     cursor = conn.cursor()
#
#     # 쿼리문 생성
#     # sql = "SELECT name, price, event from vw_productlist where name like '%" + searchProduct + "%' order by name asc"
#     sql = "SELECT name, price, event from view_all where name like '%" + event + "%' order by event asc"
#     cursor.execute(sql)
#
#     # 리스트 생성
#     productList2 = cursor.fetchall()
#     print(productList2)
#
#     # 데이타베이스 종료
#     conn.close()
#
#     return productList2
