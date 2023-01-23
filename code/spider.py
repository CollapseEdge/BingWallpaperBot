#导入所需的库
import requests,re,time,json
from bs4 import BeautifulSoup

def get_pic():
    urls = 'https://www.bing.com/?intlF=&mkt=zh-CN'
    #请求头，爬虫伪装浏览器
    headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    }
    #爬取bing壁纸
    response = requests.get(url = urls,headers = headers)
    soup = BeautifulSoup(response.text,'html.parser')
    pic_name = soup.h2.a.contents[0]
    pic_1080 = str(soup.select(".img_cont")[0])
    pic_1080 = re.findall(r'style="background-image: url(.*?);',pic_1080)[0]
    url_1080 = pic_1080.strip('(')
    data = {
        "date":time.strftime('%Y-%m-%d', time.localtime()),
        "name":pic_name,
        "url":url_1080
    }
    return data#返回值为str格式



with open('./code/data.json',"r")as file:
    #old_data = file.read()
    old_data = json.load(file)
    old_data['data_list'].append(get_pic())
    new_data = old_data
    file.close()

with open('./code/data.json','w')as f:
    f.write(json.dumps(new_data,ensure_ascii=False,indent=4))
    f.close()
print('success')
