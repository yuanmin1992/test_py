# from IPy import IP

# ip_1 = IP('192.168.1.0/24')
# print(ip_1.len())
# a = []
# for  i in ip_1:
	# a.append(i)
	# print(a)
	# print(i)
	
# ip_2 = IP("192.168.1.1")
# print(ip_2.reverseNames())
# print(ip_2.iptype())
# print(ip_2.int())
# print(ip_2.strHex())
# print(ip_2.strBin())
# print(IP(0x8188808))
class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("进入")
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, exc_type=None, exc_val=None, exc_tbs=None):
        print("退出")
        self.f.close()
		
with File('file.txt', 'w') as f:
    print("正在写入...")
    f.write('Hello')