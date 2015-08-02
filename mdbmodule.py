#!/usr/bin/python
import MySQLdb


class CSdb:

    '''
    Class to wrap basic functions of MySQLdb for handling database access.
    '''

    def __init__(self, host, port, user, passwd, db):
        '''
        open a connection to our mysql database
        '''
        self.connection = MySQLdb.connect(host=host, port=int(port),
                                          user=user, passwd=passwd, db=db)
        self.cursor = self.connection.cursor()

    def create_mapping(self, table_name):
        '''
        create a new table to store ID mapping
        '''
        self.cursor.execute("DROP TABLE IF EXISTS {tn}".format(tn=table_name))
        self.cursor.execute("CREATE TABLE {tn} ( \
                            ID INT AUTO_INCREMENT PRIMARY KEY, \
                            PAGENAME VARCHAR(25), \
                            PAGEURL VARCHAR(200) )")
