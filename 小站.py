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
    header = {'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
              'cookie': " _ga=GA1.2.148899270.1613441373; _gat=1; _gid=GA1.2.28517347.1616058633; viptellfromwhere=fa6ebcdc5528966517ba435575cf062cc151f8c7f8ae8ebd0bd6a3c7387f9091a%3A2%3A%7Bi%3A0%3Bs%3A16%3A%22viptellfromwhere%22%3Bi%3A1%3Bi%3A1%3B%7D; PHPSESSID=42ru9h24n377s8moonlm362nl3"

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
    header = {'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
              'cookie': " _ga=GA1.2.148899270.1613441373; _gat=1; _gid=GA1.2.28517347.1616058633; viptellfromwhere=fa6ebcdc5528966517ba435575cf062cc151f8c7f8ae8ebd0bd6a3c7387f9091a%3A2%3A%7Bi%3A0%3Bs%3A16%3A%22viptellfromwhere%22%3Bi%3A1%3Bi%3A1%3B%7D; PHPSESSID=42ru9h24n377s8moonlm362nl3"
              }
    req = request.Request(url, headers=header)
    response = request.urlopen(req)
    data = response.read()
    data = str(data, encoding="utf-8")
    be = str(BeautifulSoup(data, "html.parser"))
    find=re.findall(r"/work.{39,50}3D",be)
    return find
get=bighttp("https://vip.zhan.com/work/homework/info.html?workId=1006718")
for i in range(0,len(get)):
    http=str("https://vip.zhan.com"+get[i]).replace('§','&sect')
    gethttp=beautiful(http)
    mp3(gethttp,i)