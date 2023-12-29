#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2023 - 2023 Gosu, Inc. All Rights Reserved 
#
# @Time    : 2023/12/29 13:47
# @Author  : GosuXX
# @File    : file_helper.py

import yaml


def read_yml(file):
    return yaml.load(open(file, encoding="utf-8"), yaml.FullLoader)


def write_yml(data, file):
    with open(file, "w") as f:
        yaml.dump(data, f)
