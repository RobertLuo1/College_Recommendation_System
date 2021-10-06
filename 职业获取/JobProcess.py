from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd

ch_options = Options()
ch_options.add_argument('--headless')

browser = webdriver.Chrome(options=ch_options)
# 隐式等待
browser.implicitly_wait(10)
url = 'https://m.youzy.cn/careers/h5?activeName=second'
browser.get(url)

joblist = []
for i in range(10):
    iframe_element = browser.find_element_by_xpath("//iframe")

    browser.switch_to.frame(iframe_element)
    eles = browser.find_elements_by_xpath('//span[@class="name-hot"]')
    print(eles[i].text)
    jobName = eles[i].text
    # Jobsubdist = {
    #     jobName: []
    # }
    eles[i].click()

    sleep(2)
    browser.switch_to.frame(0)

    # 添加职业信息
    eles2 = browser.find_elements_by_xpath('//div[@class="van-list-row bordered van-row"]')
    for ele in eles2:
        job = ele.find_elements_by_tag_name("span")
        # Jobsubdist[jobName].append({job[0].text: job[1].text})
        d = {
            '大职业': jobName,
            '子职业': job[0].text,
            '薪资': job[1].text
        }
        joblist.append(d)

    browser.switch_to.default_content()
    retBut = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/i")
    retBut.click()
    sleep(2)

JobDataFrame = pd.DataFrame(joblist)
JobDataFrame.to_csv("jobhot.csv", encoding="utf_8_sig")

joblist = []
for i in range(10):
    iframe_element = browser.find_element_by_xpath("//iframe")

    browser.switch_to.frame(iframe_element)
    eles = browser.find_elements_by_xpath('//span[@class="name-lack"]')
    print(eles[i].text)
    jobName = eles[i].text
    eles[i].click()

    sleep(2)
    browser.switch_to.frame(0)

    # 添加职业信息
    eles2 = browser.find_elements_by_xpath('//div[@class="van-list-row bordered van-row"]')
    for ele in eles2:
        job = ele.find_elements_by_tag_name("span")
        d = {
            '大职业': jobName,
            '子职业': job[0].text,
            '薪资': job[1].text
        }
        joblist.append(d)

    browser.switch_to.default_content()
    retBut = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/div[1]/div/i")
    retBut.click()
    sleep(2)

JobDataFrame = pd.DataFrame(joblist)
JobDataFrame.to_csv("joblack.csv", encoding="utf_8_sig")