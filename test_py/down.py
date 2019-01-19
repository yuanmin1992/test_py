#coding=utf-8
import os
import urllib


print("downloading with urllib")

url0 = "http://bcmi.sjtu.edu.cn/log/files/lecture_notes/ml_2014_spring_ieee/"
for item in range(1, 15):
    file = "lecture" + str(item) + ".pdf"
    url = url0 + file
    print("downloading with " + file)
    LocalPath = os.path.join('C:\Users\yangyuanmin\Desktop',file)
    #os.path.join将多个路径组合后返回
    urllib.request.urlretrieve(url,LocalPath)
    #第一个参数url:需要下载的网络资源的URL地址
    #第二个参数LocalPath:文件下载到本地后的路径

