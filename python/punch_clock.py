import time
import re
from collections import namedtuple

import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


url = 'https://xmuxg.xmu.edu.cn/platform'

Record = namedtuple('Record', 'username password')
myself = Record('34520192201485', 'lyb114228.')
data_set = {
    Record('34520192201485', 'lyb114228.')
}

url = 'https://xmuxg.xmu.edu.cn/platform'

attest_xpath = '//*[@id="loginLayout"]/div[3]/div[2]/div/button[3]'
username_css = '#username'
password_css = '#password'
log_in_css = '#casLoginForm > p:nth-child(4) > button'

daily_health_xpath = '//*[@id="mainPage-page"]/div[1]/div[3]/div[2]/div[2]/div[3]/div/div[1]'

form_xpath = '//*[@id="mainM"]//div[@title="我的表单"]'
# 哭了，整了两个小时才弄出来，从浏览器复制出来的路径太长点击没效果，不知道为什么

promise_xpath = '//*[@id="select_1582538939790"]/div/div'


class Punch:

    def __init__(self, record):
        self.record = record
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()  # 将浏览器最大化
        self.wait = WebDriverWait(self.browser, 5)

    def log_in(self):
        """打开网页登陆之后进入我的表单"""
        self.browser.get(url)
        self.wait.until(EC.presence_of_element_located((By.XPATH, attest_xpath)))
        self.browser.find_element_by_xpath(attest_xpath).click()
        # 已点击统一认证登陆
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, username_css)))
        username_input = self.browser.find_element_by_css_selector(username_css)
        username_input.send_keys(self.record[0])
        password_input = self.browser.find_element_by_css_selector(password_css)
        password_input.send_keys(self.record[1])
        self.browser.find_element_by_css_selector(log_in_css).click()
        # 已登陆
        self.wait.until(EC.presence_of_element_located((By.XPATH, daily_health_xpath)))
        self.browser.find_element_by_xpath(daily_health_xpath).click()
        # 进入健康打卡模块

    def submit_form(self):
        time.sleep(2)
        BrowserControl = self.browser.window_handles  # 获取浏览器句柄 就是顶部那个东西
        self.browser.switch_to.window(BrowserControl[-1])  # 转换页面至新打开的页面

        self.wait.until(EC.presence_of_element_located((By.XPATH, form_xpath)))
        self.browser.find_element_by_xpath(form_xpath).click()
        # 进入我的表单

    def save(self):
        self.browser.execute_script('window.scrollTo(0, 100)')
        self.wait.until(EC.presence_of_element_located((By.XPATH, promise_xpath)))
        a = self.browser.find_element(By.XPATH, promise_xpath)
        a.click()
        # 到这里可以弄到是，看看明天不能的话就要用re



if __name__ == '__main__':
    my = Punch(myself)
    my.log_in()
    my.submit_form()
    my.save()