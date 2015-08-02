#!/usr/bin/python
# -*- coding: utf-8 -*-
import pytest

class TestCrowdstrike:
    '''
    Tests the crowdstrike webpage load times.
    '''

    def setup_method(self, method):
        '''
        setup any state tied to test execution
        '''
        self.url = "http://www.crowdstrike.com/"

    def teardown_method(self, method):
        '''
        teardown any state tied to test execution
        '''
        pass

    def test_first_function(self):
        '''
        This is a sample test for the first push.
        '''
        assert True
