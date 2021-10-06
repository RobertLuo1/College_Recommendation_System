import requests
import pandas as pd
import time

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70 "
}

school_indices = pd.read_csv("学校编号.csv", engine='python', encoding="utf-8-sig")
schoolNames = school_indices["学校"].tolist()
school_indices = school_indices["编号"].tolist()

data2020 = []  # 用来存储爬取数据字典的最终列表，最后会被转换为csv保存
# 字典格式为：{'学校': '北京大学', '科类': '文科', '专业': '文科试验班类', '最低分': 425}

for i, school in enumerate(school_indices):
    for category in [1, 2]:  # 1：理科 2：文科
        page = 1  # 页面，每页只有10个专业
        time.sleep(2)  # 睡两秒，防止访问太频繁
        while True:
            url = f"https://static-data.eol.cn/www/2.0/schoolspecialindex/2020/{school}/32/{category}/7/{page}.json"
            try:
                r = requests.get(url, headers=headers)
            except:
                data2020 = pd.DataFrame(data2020, columns=['学校', '科类', '专业', '最低分'])
                data2020.to_csv("2020数据.csv", encoding="utf-8-sig", index=False)
                exit(1)

            j = r.json()
            if j == "":
                break
            # 解析json
            for data in j['data']['item']:
                d = dict()
                d['学校'] = schoolNames[i]
                d['科类'] = "理科" if category == 1 else "文科"
                d['专业'] = data['spname']
                d['最低分'] = data['min']
                data2020.append(d)
            page += 1
    print(f"爬取第{i}所学校{schoolNames[i]}完成。")

data2020 = pd.DataFrame(data2020, columns=['学校', '科类', '专业', '最低分'])
data2020.to_csv("2020数据.csv", encoding="utf-8-sig", index=False)
pass
