# coding=utf-8

from appium import webdriver
import yaml
from appium_server import *

dfile=open('yaml_appium.yaml','r')  #yaml和脚本文件处于同一个文件夹下，故直接引用文件即可；‘r’表示读取的意思
data=yaml.load(dfile,yaml.FullLoader)
print(data)

devices_list=['11A945BC-92F2-4829-A46E-D9C028E6EEB9','BCA421E3-CF35-402F-84ED-719201FE225C']  #启动多个模拟器,'00008030-000459213450802E','11A945BC-92F2-4829-A46E-D9C028E6EEB9'
driver_caps=[]
def appium_desire(port,caps):

    time.sleep(5)
    driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(port)+'/wd/hub',caps)
    return driver

def caps():

    #组装数据[ {"port":"xxxxx","desired_caps":{ 配置信息 }},{} ]
    #
    for i in range(len(devices_list)):

        out_caps={}
        desired_caps={}
        desired_caps['platformName'] = data['platformName']
        desired_caps['platformVersion'] = data['platformVersion']
        desired_caps['deviceName'] = data['deviceName']
        desired_caps['udid'] = devices_list[i]
        desired_caps['bundleId'] = data['bundleId']
        desired_caps['automationName'] = data['automationName']
        desired_caps['wdaLocalPort'] = 8100+i*2
        desired_caps['useNewWDA'] = True

        out_caps['port'] = myserver.ports[i]
        out_caps['desired_caps'] =desired_caps
        driver_caps.append(out_caps)

    return driver_caps