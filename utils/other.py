#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2023 - 2023 Gosu, Inc. All Rights Reserved 
#
# @Time    : 2023/12/29 14:02
# @Author  : GosuXX
# @File    : other.py

import hashlib


def str2Int(s):
    # 使用utf-8编码将字符串转换为字节
    byte_str = s.encode('utf-8')
    # 创建一个md5对象
    md5 = hashlib.md5()
    # 更新md5对象
    md5.update(byte_str)
    # 获取十六进制的哈希值
    hex_hash = md5.hexdigest()
    # 将十六进制的哈希值转换为整数
    return int(hex_hash, 16)


if __name__ == "__main__":
    s = str2Int("zhangyuhang")
    print(s)
