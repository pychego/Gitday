import time  # 控制时间
# import yagmail#发送邮件（可选）
from selenium import webdriver  # selenium自动浏览器
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re  # 正则表达式

# 基本个人信息
url = 'https://xmuxg.xmu.edu.cn/platform'  # 登录的网站
# user_email='xxxxxxxxx@qq.com'#(可选)发送的邮件方 我这里用的一个小号
# password_email='xxxxxxxxxx'#（可选）邮件密码不是qq密码 而是需要到自己的邮箱设置的密码 具体可以百度怎么自动发送邮件
# email_reciver='xxxxxxxxxx@qq.com'#(可选)每天接收的邮件方
User = '15220192202XXX'  # 这里是厦大账号
passwords = 'XXXXXX'  # 密码
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)  # 每次都进行显示等待，设立最大等待时间为5s，5s内不断检验如果为True则通过


# 启动浏览器
def get_web(driver):
    driver.get(url)
    print('正在打开网页....')
    # 等一下，等数据全部加载出来了再点击
    xpath_find_log_in = '//*[@id="loginLayout"]/div[3]/div[2]/div/button[2]'  # xpath 定位
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_find_log_in)))  # 等到有这个元素加载出现的时候再开始
    tong_yi = driver.find_element_by_xpath(xpath_find_log_in)  # 找到的元素为“统一身份登录”
    return tong_yi
    time.sleep(1)


def get_log(driver):
    tong_yi = get_web(driver)  # 点击“统一身份登录”
    tong_yi.click()
    print('正在尝试找到登录入口...')
    # 此时进入第一个网址，登录界面
    xpath_denglu = '//*[@id="casLoginForm"]/p[5]/button'
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_denglu)))  # 定位到点击登录的那个地方
    driver.find_element_by_id("username").send_keys(User)  # 定位账号框并输入密码
    driver.find_element_by_id("password").send_keys(passwords)  # 定位密码框并输入密码
    denglu = '//*[@id="casLoginForm"]/p[5]/button'
    DengLu = driver.find_element_by_xpath(denglu)  # 点击登录
    return DengLu


def get_system(driver):
    DengLu = get_log(driver)
    DengLu.click()
    print('正在尝试登录账号...')
    xpath_getsystem = '//*[@id="mainPage-page"]/div[1]/div[3]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div[1]'  # 登录完了后去找“健康管理”
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_getsystem)))
    GetSystem = driver.find_element_by_xpath(xpath_getsystem)
    return GetSystem


def log_system(driver):
    GetSystem = get_system(driver)
    GetSystem.click()
    print('正在尝试进入打卡系统...')

    time.sleep(3)  # 不要太快，浏览器会反应不过来
    # 在这里卡了一会，发现是这步打开了新的页面，所以得转换一下 但转换也不能太快，否则浏览器会反应不过来
    BrownserControl = driver.window_handles  # 获取浏览器句柄 就是顶部那个东西
    driver.switch_to.window(BrownserControl[-1])  # 转换页面至新打开的页面

    xpath_Health = '//*[@id="mainM"]/div/div/div/div[1]/div[2]/div/div[3]/div[2]'
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_Health)))  # 寻找“我的表单”
    My_Health = driver.find_element_by_xpath(xpath_Health)
    return My_Health


def GetData(driver):
    My_Health = log_system(driver)
    My_Health.click()
    print('正在尝试进入我的表单...')

    # 这里打开加载很慢，所以休息一会儿
    time.sleep(3)

    # 这里有些麻烦的一点就是我发现每天的打卡的xpath名称是变化的，每个人的地址也不一样，
    # 所以需要先找到新的名称作为xpath（我比较菜，只想到用正则表达式来匹配结果
    # 不知道有没有更高效的办法）
    content = driver.page_source
    return content


def daka(driver):
    content = GetData(driver)
    where_yes = re.compile('id="select_\d.*?"', re.S)  # 非贪心匹配
    where_save = re.compile('id="preview\d.*?"', re.S)
    whether_Daka = re.compile('span title=".*?"')

    whether_Daka = re.findall(whether_Daka, content)

    whether_Daka = whether_Daka[-3]  # ！！！！！这里是特别容易错的地方 学校如果在原来表单上添加了某些值，就会导致定位出错，
    # 如果程序运行是“加了什么东西”请检查这里 看一下上面返回的列表里“span=是”是倒数第几个 把-3改成-几(一般是-3或者-2)
    # 这个本来可以在列表里找，但里面有好多重复项好麻烦啊 不想写这个， 学校改表也不频繁 就手动检查一下吧
    print('你今天的打卡状态为:', whether_Daka)
    where_yes = re.findall(where_yes, content)
    where_save = re.findall(where_save, content)
    where_yes = where_yes[-1]  # 列表取出文字。这里的打卡一般是最后一项
    where_save = where_save[0]  # 经过试验，保存的那个按键是倒数第二个span title

    print('你今天的选择地址为:', where_yes)
    print('你今天的保存地址为:', where_save)  # 检查一下
    if whether_Daka == 'span title="是 Yes"':
        final_content = '你今天已经打过卡了'
        time.sleep(2)


    else:

        xpath_yes = '//*[@' + str(where_yes) + ']/div/div'
        # 更改新的xpath路径,检查一下
        xpath_save = '//*[@' + str(where_save) + ']/span/span/i'

        wait.until(EC.presence_of_element_located((By.XPATH, xpath_yes)))
        try:
            driver.find_element_by_xpath(xpath_yes).click()
            print('请选择')

            time.sleep(3)
            # 这里卡了好一会儿，因为下拉栏时总是挡住定位，所以只能祭出execute大法
            element = driver.find_element_by_xpath('/html/body/div[8]/ul/div/div[3]/li/label')
            driver.execute_script("arguments[0].click();", element)

            print('确认')
            wait.until(EC.presence_of_element_located((By.XPATH, xpath_save)))
            driver.find_element_by_xpath(xpath_save).click()
            print('保存')

            time.sleep(2)
            # 这里会有来着xmu的弹窗提醒是否保存，选择是
            try:
                alert = driver.switch_to.alert
                print(alert.text)  # 获取弹窗上的文本
                alert.accept()  # 确认，相当于点击[确定]按钮
                print('选择"是"')
                time.sleep(2)
                content = driver.page_source
                final_data = driver.page_source
                where_yes = re.compile('id="select_\d.*?"', re.S)
                whether_Daka = re.compile('span title=".*?"')
                whether_Daka = re.findall(whether_Daka, content)
                whether_Daka = whether_Daka[-3]

                if whether_Daka == 'span title="是 Yes"':
                    final_content = '完成了每日打卡'
                    print(final_content)
                else:  # 检查的时候发现是从“是”变成“否”你本来就打过卡了但是检查的时候定位不准重新运行了一遍 请更改一下程序
                    final_content = '出现这种情况多半是学校又加了什么东西导致定位不准但是你已经打过卡啦'
                time.sleep(3)
            except Exception:  # 如果没有弹窗出来 说明你本来就打过卡了但是检查的时候定位不准重新运行了一遍 请更改一下程序
                final_content = "出现这种情况多半是学校又加了什么东西导致定位不准但是你已经打过卡啦"
        except Exception:
            final_content = '无法点击 是不是错过了打卡时间'
    time.sleep(10)
    driver.quit()
    print(final_content)
    return final_content



# 主函数
final_content = daka(driver)
# send_message(final_content)