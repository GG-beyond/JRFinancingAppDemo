# coding=utf-8
import os
import socket
import random
import time
import subprocess
from concurrent.futures import ThreadPoolExecutor
import multiprocessing #导入多进程模块

class myserver(object):

    def isOpen(self,ip,port):#判断端口是否被占用
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#创建TCP Socket(socket.AF_INET :服务器之间网络通信)(socket.SOCK_STREAM :流式socket , for TCP)
        try:
            s.connect((ip,int(port)))
            s.shutdown(2)#shotdown参数标识后续可否读写
            print('%d is used'%port)
            return True
        except Exception:
            print('%d is availabel' %port)
            return False


    def getport(self):#随机获取端口号，且判断端口是否已经在使用、端口是否已经被占用
        port = random.randint(4723,4800)

        if port not in self.ports:
            # 判断端口是否被占用
            while self.isOpen('127.0.0.1', port):
                port = self.getport()
        else: port = self.getport()

        return port


    def serverrun(self,port):
        '''启动appium服务
        ：return port_list'''
        print('start appium service')

        now_time = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

        cmd_appium = 'appium -p '+str(port)+'--session-override'#终端命令

        try: #启动appium服务
            appiumlog = open(now_time + '_log.txt', 'w')
            subprocess.Popen(cmd_appium,shell=True,stdout=appiumlog)
        except Exception as msg:
            print('error message:',msg)
            raise

    executor = ThreadPoolExecutor(6)
    ports = list()
    def create_pools(self,device_list_lenth):
        for i in device_list_lenth:

            port = self.getport()
            self.ports.append(port)
            self.serverrun(port)
            # self.executor.submit(self.serverrun(port))
            # desired=multiprocessing.Process(self.serverrun(port))
            # desired.start()  # 每个进程去启动

        return ('running')

    # 关闭所有的appium服务器
    def kill_appium(self):

        # cmd_kill = 'pkill node'
        # os.system(cmd_kill)
        for i in range(len(self.ports)):
            self.kill_appium_port(self.ports[i])

        print('close appium service')

    #杀死进程pid
    def kill_appium_pid(self,pid):
        cmd_kill = 'kill -9 {0}'.format(pid)
        os.popen(cmd_kill)
        print('close pid service')

    #根据port查找pid，并杀死进程
    def kill_appium_port(self,port):
        cmd = 'lsof -i :{0}'.format(port)
        plist = os.popen(cmd).readlines()
        plisttmp = plist[1].split("    ")
        plists = plisttmp[1].split(" ")
        pid = plists[0]
        self.kill_appium_pid(pid)

