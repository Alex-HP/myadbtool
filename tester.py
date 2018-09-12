#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
	try to use my module adbtools
"""
from adbtools import *

@计时
def main():
	点击("工具")
	点击("工具箱")
	点击("镜子")
	return

if __name__ == '__main__':
	main()