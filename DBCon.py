import cx_Oracle


def DB_connect():
    cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_19_13")
    # 본인이 Instant Client 넣어놓은 경로를 입력해준다

    connection = cx_Oracle.connect(user='admin', password='Ehdfbf8749**', dsn='orcl_high')
    # 본인이 접속할 오라클 클라우드 DB 사용자이름, 비밀번호, dsn을 넣어준다.

    return connection

def DB_Select(conn):
    curs = conn.cursor()
    sql = "select sum(price) from ex;"
    curs.execute(sql)
    rows = curs.fetchall()
    for row in rows:
        print(row)

def DB_Insert(conn,DB_list):
    try:
        curs = conn.cursor()
        sql = "insert into ex(menu,time,price,kind) values('H아메리카노,ICE아메리카노',DEFAULT,8000,'카드');"
        sql = "insert into pos_table values(tmp_seq.NEXTVAL, TO_CHAR(sysdate,'MM-DD-YYYY hh24:mi:ss'), '{}', {}, '{}')".format(str(DB_list[0]),int(DB_list[1]),str(DB_list[2]))
        #curs.execute(sql,('H아메리카노,ICE아메리카노',8000,'카드'))
        curs.execute(sql)
        conn.commit()

    except Exception as e:
        print(e)

def DB_Test(conn,dateText):
    list1 = []
    list2 = []
    curs = conn.cursor()
    #sql = "select * from ex where time between '2020-11-27 00:00:00' and '2020-11-27 23:59:59';"
    sql = "select * from post_table where time between '"+ dateText + " 00:00:00' and '"+ dateText + " 23:59:59';"

    curs.execute(sql)
    rows = curs.fetchall()
    print(rows)
    rcount = int(curs.rowcount)

    for i in range(0,rcount):
        list1 = []
        for j in range(1,5):
            list1.append(rows[i][j])
        list2.append(list1)
    return rcount,list2

def DB_Delect(conn,item):
    curs = conn.cursor()
    sql = "delete from ex where time = '"+str(item)+"';"
    curs.execute(sql)
    rows = curs.fetchall()
    conn.commit()

def DB_order_count(conn,dateText,time1,time2):
    curs = conn.cursor()
    sql = "select count(menu) from ex where time between '" + dateText + " " + time1 + "' and '" + dateText +" " +time2 +"';"
    curs.execute(sql)
    rows = curs.fetchone()

    return int(rows[0])

def DB_total_Price(conn,dateText,time1,time2):
    curs = conn.cursor()
    sql = "select sum(price) from ex where time between '" + dateText + " " + time1 + "' and '" + dateText +" " +time2 +"';"
    curs.execute(sql)
    rows = curs.fetchone()
    value = str(rows[0])            #값을 String으로 변환

    if value == "None":             # 값이 없으면 value를 0으로 처리
        return int("0")
    else:
        return rows[0]

def DB_get_total_price(conn,dateText):

    curs = conn.cursor()
    sql = "select sum(price) from ex where time between '"+ dateText + " 00:00:00' and '"+ dateText + " 23:59:59';"

    curs.execute(sql)
    rows = curs.fetchone()
    value = str(rows[0])  # 값을 String으로 변환

    if value == "None":  # 값이 없으면 value를 0으로 처리
        return int("0")
    else:
        return rows[0]



