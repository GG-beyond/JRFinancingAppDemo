
# coding=utf-8
import unittest
from time import sleep
from Singlenton import SinglentonClass
from BaseTest import BaseTestClass

class SimpleInvestTests(BaseTestClass):

    def setUp(self):
        self.driver = SinglentonClass().mywebdriver


        
        
    def test_invest(self):

        #'''测试充值流程'''
        #操作 找到tabbar "我的"，点击

        el1 = self.driver.find_element_by_name("投资")
        el1.click()
        sleep(5)

        return