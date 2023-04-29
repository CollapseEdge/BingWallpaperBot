#导入所需的库
import requests,time,json

def get_pic():
    urls = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
    #请求头，爬虫伪装浏览器
    headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    }
    #爬取bing壁纸
    response = requests.get(url = urls,headers = headers)
    data1 = json.loads(response.text)
    image_url = data1["images"][0]["url"]
    image_title = data1["images"][0]["title"]
    data = {
        "date":time.strftime('%Y-%m-%d', time.localtime()),
        "name":image_title,
        "url":image_url
    }
    return data#返回值为str格式
    


with open('data.json',"r",encoding='utf-8')as file:
    #old_data = file.read()
    old_data = json.load(file)
    old_data['data_list'].append(get_pic())
    new_data = old_data
    file.close()

with open('data.json','w')as f:
    f.write(json.dumps(new_data,ensure_ascii=False,indent=4))
    f.close()
print('success')
