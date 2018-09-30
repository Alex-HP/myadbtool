#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
	try to use my module adbtools
"""
from adbtools import *
from time import sleep

@计时
def main():
	# sleep(60*60*3)
	点击("钉钉")
	输入("13192294549")
	点击("请输入密码")
	输入("caonimabi")
	点击("登录")
	return

if __name__ == '__main__':
	main()