# 弃用文件

import time
from selenium import webdriver
import urllib3
import pandas as pd

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # 取消警告

# 这里从已有的文件里获取学校列表
sciSchools = pd.read_csv("江苏省理科预测数据.csv", engine='python', encoding="utf-8-sig")
artSchools = pd.read_csv("江苏省文科预测数据.csv", engine='python', encoding="utf-8-sig")
sciSchools = sciSchools['学校'].tolist()
artSchools = artSchools['学校'].tolist()

# 除去重复出现的学校名
schoolNames = []  # 保存在这里
for school in sciSchools:
    if school not in schoolNames:
        schoolNames.append(school)
for school in artSchools:
    if school not in schoolNames:
        schoolNames.append(school)

result = []
# 这里想办法获得数据库中有的每个学校的相应编号
for i in range(20, 40):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(
        # options=option  # 不打开浏览器窗口
    )
    driver.get("https://gkcx.eol.cn/headSearch?search=" + schoolNames[i])
    driver.implicitly_wait(10)

    element = driver.find_element_by_class_name("school_name")
    time.sleep(2)  # 等一秒，否则没加载完全
    element.click()
    new_page = driver.window_handles[1]
    driver.switch_to.window(new_page)
    time.sleep(1)  # 这里也得等一秒，否则url是错的
    current_url = driver.current_url
    index = current_url.split('/')[-1]

    result.append([schoolNames[i], index])
    driver.quit()
    print(f"已获取第{i}所学校的编号。")

df = pd.DataFrame(result, columns=['学校', '编号'])
df.to_csv("学校编号2.csv", index=False, encoding="utf-8-sig")
