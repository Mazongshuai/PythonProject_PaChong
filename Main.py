import urllib.request
import re
from typing import Any


def getHtmlContent(url: Any):
    page = urllib.request.urlopen(url)
    return page.read()

def getJPGs(html: Any):
    jpgReg = re.compile(r'<img.+?src="(.+?\.jpg)" width')

    jpgs = re.findall(jpgReg, html.decode('utf-8'))
    return jpgs

def downloadJPG(imgUrl, fileName):
    urllib.request.urlretrieve(imgUrl, fileName)

def batchDownloadJPGs(imgUrls, path='F:/zdl/'):
    # 用于给图片命名
    count = 1
    for url in imgUrls:
        downloadJPG(url, ''.join([path, '{0}.jpg'.format(count)]))
        print ("正在下载第" + str(count) + "张")
        count = count + 1

def download(url):
    html = getHtmlContent(url)
    jpgs = getJPGs(html)
    batchDownloadJPGs(jpgs)

def main():
    url = 'http://tieba.baidu.com/p/2256306796'
    download(url)

main()