# coding=utf-8
from moreDevice_test import *
import unittest
from appium_server import *
from modules import Recharge_UITest
from time import sleep
from multiprocessing import Pool
import os
from Singlenton import SinglentonClass


def runnerPool():

    arr = caps()
    pool = Pool(len(arr))
    pool.map(test_run, arr)
    pool.close()
    pool.join()

def test_run(app):

    print('running case====%s' %os.getpid())
    port=app['port']
    desired_caps=app['desired_caps']
    SinglentonClass().mywebdriver = appium_desire(port,desired_caps)
    sc_path = os.path.join(os.getcwd(), "modules") #用例所在路径
    suite = unittest.TestLoader().discover(sc_path, pattern="*.py", top_level_dir=None)
    # 运行测试用例
    unittest.TextTestRunner(verbosity=2).run(suite)
    print "\n" + u'测试结束!'


if __name__ == '__main__':

    #根据需要测试的设备个数，启动appium服务个数
    #启动appium服务
    myserver().create_pools(range(len(devices_list)))

    sleep(2)
    runnerPool()

    print('kill appium服务')
    myserver().kill_appium()







