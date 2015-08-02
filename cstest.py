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
                      cls.config.get('mysql', 'db')).connection

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

    def test_first_function(self):
        '''
        This is a sample test for the first push.
        '''
        assert self.db.cursor == False
