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
        sql = " SELECT * from df_all where 편의점 like" + "'%" + name2 + "%'" + "and 품명 like '%" + searchProduct + "%'"

    cursor.execute(sql)

    # 리스트 생성

    productList = cursor.fetchall()
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
    sql = 'SELECT * from ' + df_name_oneplusone + ' LIMIT '+ page + ',20';
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


def get_dum_list(df_name_oneplusone, page):

    # 데이타베이스 접속함수 호출
    conn = get_connection()
    # 작업변수 생성
    cursor = conn.cursor()
    page=(int(page)-1)*6
    page = str(page)
    sql = 'SELECT * from ' + df_name_oneplusone + ' LIMIT '+ page + ',6';
    cursor.execute(sql)
    oneplusone_list= cursor.fetchall()
    print(oneplusone_list)
    # 데이타베이스 종료
    conn.close()
    return oneplusone_list
    # 데이타베이스 종료
    conn.close()

    return oneplusone_list

##################3 게시판 DB 리스트########################
def get_board_list(df_board, page):

    # 데이타베이스 접속함수 호출
    conn = get_connection()

    # 작업변수 생성
    cursor = conn.cursor()
    print(page)
    page=(int(page)-1)*10
    page = str(page)
    sql = 'SELECT num, title, name, date, views FROM ' + df_board + ' ORDER BY num DESC LIMIT '+ page + ',10';
    cursor.execute(sql)
    board_list= cursor.fetchall()

    # 데이타베이스 종료
    conn.close()

    return board_list

def get_board_record(df_board, num):
    conn = get_connection()
    cursor = conn.cursor()
    sql = 'SELECT * FROM ' + df_board + ' WHERE num = ' + str(num);
    cursor.execute(sql)
    board_record = cursor.fetchall()
    conn.close()
    return board_record

def get_board_update(df_board, num):
    conn = get_connection()
    cursor = conn.cursor()
    sql = 'UPDATE ' + df_board + ' set views = views + 1 WHERE num = "num"' ;
    cursor.execute(sql)
    board_record = cursor.fetchall()
    print(board_record)
    conn.close()
    return board_record

get_board_update('df_board', 2)

def get_board_list_totCnt(df_board):

    # 데이타베이스 접속함수 호출
    conn = get_connection()

    # 작업변수 생성
    cursor = conn.cursor()
    sql = 'SELECT count(*) FROM ' + df_board ;
    cursor.execute(sql)
    totCnt= cursor.fetchone()

    # 데이타베이스 종료
    conn.close()

    return int(totCnt[0])


# 게시판 레코드 추가
def addDb_board(a_title, a_content, a_name):
    sql = '''
            INSERT INTO df_board
                (title, content, name, date, views)
                values (%s, %s, %s, curdate(), 0)
            '''
    # 데이타베이스 접속함수 호출
    conn = get_connection()

    # 작업변수 생성
    cursor = conn.cursor()
    cursor.execute(sql, (a_title, a_content, a_name))
    conn.commit()

    conn.close()

def table_check(df_table):
    conn = get_connection()
    cursor = conn.cursor()
    sql = 'SELECT count(*) FROM ' + df_table ;
    cursor.execute(sql)
    totCnt = cursor.fetchone()
    conn.close()
    return str(totCnt[0])

