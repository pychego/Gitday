import time
import re


import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


url = 'https://xmuxg.xmu.edu.cn/platform'
username = '34520192201485'
password = 'lyb114228.'

browser = webdriver.Chrome()
browser.get(url)
wait = WebDriverWait(browser, 5)

attest_xpath = '//*[@id="loginLayout"]/div[3]/div[2]/div/button[3]'
wait.until(EC.presence_of_element_located((By.XPATH, attest_xpath)))
attest = browser.find_element_by_xpath(attest_xpath)
attest.click()
time.sleep(1)

username_css = '#username'
password_css = '#password'
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, username_css)))
username_input = browser.find_element_by_css_selector(username_css)
username_input.send_keys(username)
password_input = browser.find_element_by_css_selector(password_css)
password_input.send_keys(password)
browser.find_element_by_css_selector('#casLoginForm > p:nth-child(4) > button').click()




