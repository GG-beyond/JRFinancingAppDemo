# coding=utf-8

import time
import os


def takeScreenShot(self, name="takeShot"):
    '''
    :param self: driver
    :param name: 截图的名称
    :return: 获取当前屏幕截图
    '''

    print('***********')
    # 截屏
    now1 = time.strftime('%Y-%m-%d %H_%M_%S')  # 获取当前时间，并且格式化为字符串
    screen_path = os.getcwd() + '/screen_ capture/'

    print(os.path.dirname(os.path.abspath("__file__")))
    print(os.path.pardir)
    print(os.path.join(os.path.dirname("__file__"), os.path.pardir))
    print(os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir)))

    type = '.png'
    if os.path.exists(screen_path):
        screen_path = screen_path+now1+name+type
    else:
        os.makedirs(screen_path)
        screen_path = screen_path+now1+name+type
    print('screen_path = ',screen_path)
    self.driver.get_screenshot_as_file(screen_path)