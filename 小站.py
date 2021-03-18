from urllib import request
import ssl
import re
from bs4 import BeautifulSoup
ssl._create_default_https_context = ssl._create_unverified_context
def mp3(name,range):
    url=name
    img = request.Request(url)
    img = request.urlopen(img)
    img = img.read()
    with open("小站/xiaozhan"+str(range)+".mp3", mode='wb') as f:
        f.write(img)
def beautiful(name):
    url=name
    header = {'user-agent': "",
              'cookie': " "
#input your cookie and agent
              }
    req = request.Request(url, headers=header)
    response = request.urlopen(req)
    data = response.read()
    data = str(data, encoding="utf-8")

    be = BeautifulSoup(data, "html.parser")
    get=be.find_all("script")
    get=str(get[8])
    get=re.findall(r"http.+mp3",get)
    return get[0]
def bighttp(name):
    url = name
    header = {'user-agent': "",
              'cookie': ""
              }
    req = request.Request(url, headers=header)
    response = request.urlopen(req)
    data = response.read()
    data = str(data, encoding="utf-8")
    be = str(BeautifulSoup(data, "html.parser"))
    find=re.findall(r"/work.{39,50}3D",be)
    return find
get=bighttp("https://vip.zhan.com/work/homework/info.html?workId=1006718")#input http
for i in range(0,len(get)):
    http=str("https://vip.zhan.com"+get[i]).replace('§','&sect')
    gethttp=beautiful(http)
    mp3(gethttp,i)
