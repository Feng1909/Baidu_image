from BaiduImagesDownload.crawler import Crawler
import os

word = input("请输入名称: ")
num_ = eval(input("下载数量: "))
file_name = input("文件夹名称: ")

if os.path.exists(file_name):
    print("文件已存在")
else:
    os.mkdir(file_name)

net, num, urls = Crawler.get_images_url(word, num_, original=False)
Crawler.download_images(urls, rule='.jpg', path=file_name)
