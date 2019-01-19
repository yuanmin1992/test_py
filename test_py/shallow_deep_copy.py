#! /usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    # 赋值，同一个对象的引用
    old_list = [1,2,3,4]
    new_list = old_list
    new_list.append(5)
    print("new list items:%s" %new_list)
    print("old list items:%s" %old_list)

    #浅拷贝
    import copy
    old_list = [1, 2, 3, 4]
    new_list = copy.copy(old_list)
    new_list.append(5)
    print("new list items:%s" % new_list)
    print("old list items:%s" % old_list)

    #浅拷贝
    old_list = [[1,2],[3,4]]
    new_list = copy.copy(old_list)
    new_list[0].append(5)
    print("new list items:%s" % new_list)
    print("old list items:%s" % old_list)

    print("*"*30)
    #深拷贝
    list_of_list = [[1,2],[3,4],["A","B"]]
    new_list_of_list = copy.deepcopy(list_of_list)
    new_list_of_list[0].append(10)
    new_list_of_list[1].remove(3)
    list_of_list[2].append("c")
    print("list_of_list items:%s" %list_of_list)
    print("new_list_of_list items:%s" %new_list_of_list)


if __name__ == "__main__":
    main()