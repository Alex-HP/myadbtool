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
	点击("网易云音乐")
	sleep(5)
	点击("推荐歌单")
	点击("全部歌单")
	点击("电子")
	点击("精品歌单")
	点击("筛选")
	点击("什么是精品歌单")
	#输入("13192294549")
	#点击("请输入密码")
	#输入("caonimabi")
	#点击("登录")
	return

if __name__ == '__main__':
	main()