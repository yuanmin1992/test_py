#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time

def progress_bar(total):
    """
    进度条效果
    """
    # 获取标准输出
    _output = sys.stdout
    # 通过参数决定你的进度条总量是多少
    for count in range(0,total + 1):
        # 这里的second只是作为工作总量的一种代替
        # 这里应该是有你的总程序，main（）
        _second = 0.1
        # 模拟业务的消耗时间发
        time.sleep(_second)
        # 输出进度条
        _output.write('\rcomplete percent:{0:.0f}'.format(count))
    # 将标准输出一次性刷新
    _output.flush()
progress_bar(100)


def main():
    pass


if __name__ == "__main__":
    main()