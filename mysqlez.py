'''
Created on Sep 23, 2014
@author: dweiss
'''
import MySQLdb

def connect(dbhost,dbuser,dbpasswd,dbname):
    conn = MySQLdb.connect(host = dbhost,
            user = dbuser,
            passwd = dbpasswd,
            db = dbname)
    return conn

def grab_all(query,connection):

    cursor = connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows

def grab_one(query,connection):

        cursor = connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(query)
        rows = cursor.fetchall()
        connection.commit()
        cursor.close()
        if len(rows) > 0:
                return rows[0]
        else:
                return False

if __name__ == '__main__':
    pass