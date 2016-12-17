#coding=utf-8


#一个简单的示例爬虫
# http://blog.csdn.net/evankaka/
import urllib.request
url = "http://qa.eqiutian.com:8030/api/v1/products/10000"
webPage=urllib.request.urlopen(url)
data = webPage.read()
data = data.decode('UTF-8')
print(data)
# print(type(webPage))
# print(webPage.geturl())
# print(webPage.info())
# print(webPage.getcode())