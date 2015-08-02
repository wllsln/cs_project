#!/usr/bin/python
# -*- coding: utf-8 -*-
import ConfigParser
import pytest
import mysql.connector

class TestCrowdstrike:
    '''
    Tests the crowdstrike webpage load times.
    '''

    def setup_method(self, method):
        '''
        setup any state tied to test execution
        '''
        self.url = 'http://www.crowdstrike.com/'
        self.config = ConfigParser.RawConfigParser()
        self.config.read('settings.cfg')

    def teardown_method(self, method):
        '''
        teardown any state tied to test execution
        '''
        pass

    def test_first_function(self):
        '''
        This is a sample test for the first push.
        '''
        db_name = self.config.get('MySQL', 'db_name')
        count = self.config.get('MySQL', 'count')
        assert db_name == 'default_name'
        assert int(count) == 7