# -*- coding: utf-8 -*-
import itchat
import random
import os
import image
import math
import pillow
def headImg():
    itchat.login()
    friends = itchat.get_friends(update=True)
    # itchat.get_head_img() 获取到头像二进制，并写入文件，保存每张头像
    for count, f in enumerate(friends):
        # 根据userName获取头像
        img = itchat.get_head_img(userName=f["UserName"])
        imgFile = open("img/" + str(count) + ".jpg", "wb")
        imgFile.write(img)
        imgFile.close()
def createImg():
    x = 0
    y =0
    imgs = os.listdir("img")
    random.shuffle(imgs)
    newImg = image.new("RGBA",(640,640))
    width = int(math.sqrt(640*640/len(imgs)))
    numLine = int(640 / width)

    for i in imgs:
        img = image.open("img/" + i)
        img = img.resize((width,width),image.ANTIALIAS)
        newImg.paste(img,(x * width, y * width))
        x += 1
        if x >= numLine:
            x = 0
            y += 1
    newImg.save("all.png")

# createImg()
def getSex():
    itchat.login()
    friends = itchat.get_friends(update=True)
    sex = dict()
    for f in friends:
        if f["Sex"] == 1: #男
            sex["man"] = sex.get("man", 0) + 1
        elif f["Sex"] == 2: #女
            sex["women"] = sex.get("women", 0) + 1
        else: #未知
            sex["unknown"] = sex.get("unknown", 0) + 1
    # 柱状图展示
    for i, key in enumerate(sex):
        plt.bar(key, sex[key])
    plt.show()