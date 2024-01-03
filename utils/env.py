#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2023 - 2023 Gosu, Inc. All Rights Reserved 
#
# @Time    : 2023/12/29 11:12
# @Author  : GosuXX
# @File    : env.py
import os
import shutil


def clear_path(path):
    # try:
    #     shutil.rmtree(path)
    # except Exception as e:
    #     pass
    os.makedirs(path, exist_ok=True)

