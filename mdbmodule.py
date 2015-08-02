#!/usr/bin/python
import MySQLdb
import sys


class CSdb:

    '''
    Class to wrap basic functions of MySQLdb for handling database access.
    '''

    def __init__(self, host, port, user, passwd, db):
        '''
        open a connection to our mysql database
        '''
        try:
            self.connection = MySQLdb.connect(host=host, port=int(port),
                                              user=user, passwd=passwd, db=db)
        except MySQLdb.Error, err:
            print 'Error {d}: {s}'.format(d=err.args[0], s=err.args[1])
            sys.exit(1)
            
        self.cursor = self.connection.cursor()
        self.cursor.execute("USE {db}".format(db=db))

    def create_mapping(self, table_name):
        '''
        create a new table to store ID mapping
        '''
        try:
            self.cursor.execute("DROP TABLE IF EXISTS {tn}".format(tn=table_name))
        except MySQLdb.Warning, err:
            print 'Table does not exist. Will create!'
        self.cursor.execute("CREATE TABLE {tn}( ID INT AUTO_INCREMENT PRIMARY KEY, "
                            "PAGENAME VARCHAR(25), PAGEURL VARCHAR(100) )".format(tn=table_name))
