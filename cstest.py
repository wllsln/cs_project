#!/usr/bin/python
# -*- coding: utf-8 -*-
import ConfigParser
import pytest
from mdbmodule import CSdb


class TestCrowdstrike:

    '''
    Tests the crowdstrike webpage load times.
    '''

    def setup_class(cls):
        '''
        setup any state tied to the test class
        runs once per Test class
        '''
        cls.config = ConfigParser.SafeConfigParser()
        cls.config.read('settings.cfg')
        cls.db = CSdb(cls.config.get('mysql', 'host'),
                      cls.config.get('mysql', 'port'),
                      cls.config.get('mysql', 'user'),
                      cls.config.get('mysql', 'passwd'),
                      cls.config.get('mysql', 'db'))

    def teardown_class(cls):
        '''
        teardown any state tied to the test class
        runs once per Test class
        '''
        pass

    def setup_method(self, method):
        '''
        setup any state tied to test execution
        runs before every test
        '''
        pass

    def teardown_method(self, method):
        '''
        teardown any state tied to test execution
        runs before every test
        '''
        pass

    def test_insert_mapping(self):
        '''
        This is a sample test for the first push.
        '''
        table_name = self.config.get('table_names', 'mapping')
        self.db.create_mapping(table_name)
        self.db.cursor.execute("SELECT * FROM {tn} LIMIT 0".format(tn=table_name))
        headers = [column[0] for column in self.db.cursor.description]
        
        assert headers == ['ID', 'PAGENAME', 'PAGEURL']
