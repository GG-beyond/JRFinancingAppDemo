# coding=utf-8
from BaseTest import BaseTestClass
from take_screebShot import take_screenShot
from time import sleep
from Singlenton import SinglentonClass


class SimpleIOSTests(BaseTestClass):

    def setUp(self):
        self.driver = SinglentonClass().mywebdriver


    def test_recharge(self):

        #'''测试充值流程'''
        #操作 找到tabbar "我的"，点击

        el1 = self.driver.find_element_by_name("我的")
        el1.click()
        sleep(5)

        return
        #操作 点击"我的"-"充值"
        el2 = self.driver.find_element_by_name("充值")
        el2.click()
        sleep(3)


        el3 = self.driver.find_elements_by_class_name('XCUIElementTypeTextField')

        el3[0].send_keys('1000')

        take_screenShot(self,u'充值')


        sleep(2)
        el4 = self.driver.find_element_by_name("下一步")
        el4.click()

        return
        sleep(6)

        view0 = self.driver.contexts
        print ('view0 = ',view0)


        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="知道了"]').click()


        sleep(4)
        #
        # self.driver.switch_to.context(view[0])
        #
        # self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="JRFinancing back black"]').click()
        #
        # sleep(1)
        # self.driver.switch_to.context(view[1])
        # el6 = self.driver.find_elements__by_xpath('//*/XCUIElementTypeTextField')

        el6 = self.driver.find_elements_by_class_name('XCUIElementTypeTextField')
        print ('el6=',el6)
        el6[0].send_keys('123213')

        sleep(1)

        el7 = self.driver.find_elements_by_class_name('XCUIElementTypeSecureTextField')
        el7[0].send_keys('qqwwee')
        sleep(1)

        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="忘记密码？"]').click()

        sleep(1)
        aa = self.driver.find_element_by_name('输入验证码')
        aa.click()
        aa.send_keys('123123')


        sleep(3)
        self.driver.back()
        sleep(3)

        el00 = self.driver.find_elements_by_class_name('XCUIElementTypeSecureTextField')
        el00[0].send_keys('qqwwee')
        sleep(1)
        #
        el8 = self.driver.find_element_by_name("同意协议并支付")
        el8.click()

        sleep(8)

        self.driver.find_element_by_name("确定").click()

        sleep(4)





