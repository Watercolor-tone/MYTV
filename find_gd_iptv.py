import requests

# 获取JSON数据
json_url = 'https://php.17186.eu.org/gdtv/data.json'
response = requests.get(json_url)
datas = response.json()

info_list=[]
for data in datas:
    info_list.append(f"#EXTINF:-1 ,{data['name']}\n{data['url']}")

with open("mytv_url.m3u8", "r", encoding="utf8")as f:
    m3u=f.read()

content = "\n".join(info_list)+m3u

with open("mytv.m3u8", "w", encoding="utf8")as f:
    f.write(content)

print("运行完成")
