#!/usr/bin/env python3

class DBConnection:
    single = None

    def __init__(self):
        if DBConnection.single:
            raise DBConnection.single
        DBConnection.single = self

    @staticmethod
    def get_instance():
        if not DBConnection.single:
            DBConnection.single = DBConnection()
        return DBConnection.single

    def query(self):
        print('query now')


if __name__ == '__main__':
    conn = DBConnection.get_instance()  # print "connect to db"
    conn.query()  # print "Make a query"

    newConn = DBConnection.get_instance()  # print nothing
    conn.query()  # print "Make a query"

    if conn is newConn:
        print('is the same object')
    else:
        print('not same object')
