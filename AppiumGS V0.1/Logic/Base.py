__author__ = 'shaonianshaonian'

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

class Base:
    driver = None
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.12.101:5555'
    desired_caps['appPackage'] = 'honc.td'
    desired_caps['appActivity'] = 'honc.td.feature.main.MainActivity'
    desired_caps['unicodeKeyboard'] = 'true'
    desired_caps['resetKeyboard'] = 'true'

    def __init__(self):
        pass

    def connectAppium(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)

    # 获取屏幕截图
    def saveScreenShot(self,name):
        fmt = '%Y%m%d%H%M%S'  # 定义时间显示格式
        Date = time.strftime(fmt, time.localtime(time.time()))  # 把传入的元组按照格式，输出字符串
        PicName = "../Result/" + name +"-"+ Date + ".jpg"
        self.driver.get_screenshot_as_file(PicName)

    # 获得机器屏幕大小x,y
    def getWindowsSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    # 屏幕向上滑动
    def swipeUp(self,time=800):
        l = self.getWindowsSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.75)  # 起始y坐标
        y2 = int(l[1] * 0.25)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, time)

    # 屏幕向下滑动
    def swipeDown(self,time=800):
        l = self.getWindowsSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.25)  # 起始y坐标
        y2 = int(l[1] * 0.75)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, time)

    # 屏幕向左滑动
    def swipeLeft(self,time=800):
        l = self.getWindowsSize()
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.05)
        self.driver.swipe(x1, y1, x2, y1, time)

    # 屏幕向右滑动
    def swipeRight(self,time=800):
        l = self.getWindowsSize()
        x1 = int(l[0] * 0.05)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, time)

    #重新封装单个元素定位方法
    def find_element(self,loc,wait=15):
        try:
            WebDriverWait(self.driver,wait).until(lambda driver:driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            print ("%s 页面中未能找到 %s 元素" %(self,loc))
            return False

    #重新封装一组元素定位方法
    def find_elements(self,loc):
        try:
            if len(self.driver.find_elements(*loc)):
                return self.driver.find_elements(*loc)
        except:
            print ("%s 页面中未能找到 %s 元素" %(self,loc))
            return False

    #重新封装按钮点击方法
    def clickButton(self,loc,find_first=False):
        try:
            if find_first:
                self.find_element(loc)
            self.find_element(loc).click()
        except AttributeError:
            print ("%s 页面中未能找到 %s 按钮" %(self,loc))
            return False
        return True

    #重新封装输入方法
    def sendKeys(self,loc,value,clear_first=False,click_first=False):
        try:
            if click_first:
                self.find_element(loc).click()
            if clear_first:
                self.find_element(loc).clear()
            self.find_element(loc).send_keys(value)
        except AttributeError:
            print ("%s 页面中未能找到 %s 元素" %(self,loc))
            return False
        return True

    #重新封装读属性方法
    def getAttribute(self,loc,clear_first=False,click_first=False):
        try:
            if click_first:
                self.find_element(loc).click()
            if clear_first:
                self.find_element(loc).clear()
            return self.find_element(loc).get_attribute('text')
        except AttributeError:
            print ("%s 页面中未能找到 %s 元素" %(self, loc))
            return False