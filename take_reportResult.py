# coding=utf-8


import time
import os
import HTMLTestRunnerCN

def take_report(test,title=u'名字',description=u'描述'):

    now = time.strftime('%Y-%m-%d %H_%M_%S')  # 获取当前时间，并且格式化为字符串

    # 定义个报告存放的路径，支持相对路径
    file_name = os.getcwd() + '/report_result/' + now + '.html'  # 重构文件名

    print('file_name', file_name)
    file_result = open(file_name, 'wb')
    # 定义测试报告
    runner = HTMLTestRunnerCN.HTMLTestReportCN(stream=file_result, title=title, description=description,
                                               tester=u'解振峰')
    runner.run(test)

    file_result.close()




