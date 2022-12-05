import sys
from dbms.connection import Connect
from libs.customer_libs import Customer_Libs



def total_customer():
    conn=None
    sql="""SELECT count(cid) from customers"""
    result=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        result=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return result