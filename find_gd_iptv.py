import requests

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0", }
# 获取JSON数据
json_url = 'https://php.17186.eu.org/gdtv/data.json'
response = requests.get(json_url, headers=header)
datas = response.json()

info_list = []
my_list = ["广东珠江", "广东影视", "广东新闻", "广东体育", "广东民生", "大湾区卫视（海外版）", "广东经济科教",
           "大湾区卫视", "广东4K超高清", "嘉佳卡通", "广东移动"]

for data in datas:
    if data['name'] in my_list:
        info_list.append(f"#EXTINF:-1 ,{data['name']}\n{data['url']}")

with open("mytv_url.m3u8", "r", encoding="utf8")as f:
    m3u=f.read()

content = "\n".join(info_list)+m3u

with open("mytv.m3u8", "w", encoding="utf8") as f:
    f.write(content)

print("运行完成")
