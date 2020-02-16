import os
from time import sleep
import sys
import io
from selenium import webdriver

def log_in():

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码
    # 建立Phantomjs浏览器对象，括号里是phantomjs.exe在你的电脑上的路径
    browser = webdriver.PhantomJS('/Applications/phantomjs-2.1.1-macosx/bin/phantomjs')
    # print(browser.page_source.encode('utf-8').decode())
    # 登录页面
    url = r'https://account.ryjiaoshi.com/log-in'

    # 访问登录页面
    browser.get(url)

    # 等待一定时间，让js脚本加载完毕
    browser.implicitly_wait(5)

    # 输入用户名
    username = browser.find_element_by_name('Email')
    username.send_keys('用户名')
    #sleep(1)

    # 输入密码
    password = browser.find_element_by_name('Password')
    password.send_keys('密码')
    #sleep(2)
    # 点击“登录”按钮
    login_button = browser.find_element_by_class_name("col-md-7")
    # find_element_by_name("class=btn btn-primary")
    login_button.submit()
    sleep(1)
    # 网页截图
    browser.save_screenshot('picture1.png')
    #通过解析网页获取到课程目录的地址
    pages = ['https://www.ryjiaoshi.com/course/lesson/291', 'https://www.ryjiaoshi.com/course/lesson/292', 'https://www.ryjiaoshi.com/course/lesson/293', 'https://www.ryjiaoshi.com/course/lesson/314', 'https://www.ryjiaoshi.com/course/lesson/288', 'https://www.ryjiaoshi.com/course/lesson/289', 'https://www.ryjiaoshi.com/course/lesson/290', 'https://www.ryjiaoshi.com/course/lesson/287', 'https://www.ryjiaoshi.com/course/lesson/322', 'https://www.ryjiaoshi.com/course/lesson/323', 'https://www.ryjiaoshi.com/course/lesson/324', 'https://www.ryjiaoshi.com/course/lesson/325', 'https://www.ryjiaoshi.com/course/lesson/318', 'https://www.ryjiaoshi.com/course/lesson/319', 'https://www.ryjiaoshi.com/course/lesson/320', 'https://www.ryjiaoshi.com/course/lesson/315', 'https://www.ryjiaoshi.com/course/lesson/316', 'https://www.ryjiaoshi.com/course/lesson/317', 'https://www.ryjiaoshi.com/course/lesson/98', 'https://www.ryjiaoshi.com/course/lesson/333', 'https://www.ryjiaoshi.com/course/lesson/329', 'https://www.ryjiaoshi.com/course/lesson/330', 'https://www.ryjiaoshi.com/course/lesson/331', 'https://www.ryjiaoshi.com/course/lesson/332', 'https://www.ryjiaoshi.com/course/lesson/326', 'https://www.ryjiaoshi.com/course/lesson/327', 'https://www.ryjiaoshi.com/course/lesson/328', 'https://www.ryjiaoshi.com/course/lesson/321']
    vedio_links = []
    # 打开每个课程目录
    for page_url in pages:
        #sleep(1)
        browser.get(page_url)
        page_content = browser.page_source.encode('utf-8').decode()
        #print(page_content)
        urls = get_links(page_content)
        links = []
        # 进入每个目录下的视频链接
        for single_url in urls:
            browser.get(single_url)
            # 获取每个链接下的可以下载的视频链接
            vedio_link = browser.find_element_by_class_name("prism-player")
            block = vedio_link.get_attribute("innerHTML")
            # 当然这种地方可以采用正则过滤，我只是用了比较蠢的方法
            link = block.split('" poster=')[0].split('src="')[1]
            links.append(link)
            #print(links)
        vedio_links.append(links)
    browser.quit()
    return vedio_links


def get_links(text):
    # 这里是从网页源html码中过滤出想要的链接，
    # 其实完全可以用正则过滤的，只是我用了较蠢的方法
    ids = []
    for line in text.splitlines():
        if "href" in line:
            link = "https://www.ryjiaoshi.com" + line.strip().split('"')[1]
            ids.append(link)
    return ids


if __name__ == '__main__':

    p_links = log_in()
    print(p_links)

