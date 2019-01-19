#coding:utf-8
import random,string

def GetPassword(length):

    # 随机生成数字个数
    Ofnum=random.randint(1,length)
    Ofletter=length-Ofnum

    # 选中ofnum个数字
    slcNum=[random.choice(string.digits) for i in range(Ofnum)]

    # 选中ofletter个字母
    slcLetter=[random.choice(string.ascii_letters) for i in range(Ofletter)]

    # 打乱组合
    slcChar=slcLetter+slcNum
    random.shuffle(slcChar)

    # 生成随机密码
    getPwd=''.join([i for i in slcChar])
    return getPwd

if __name__=='__main__':
    print( GetPassword(6)) #GetPassword()自定义随机密码长度