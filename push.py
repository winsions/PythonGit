# -*- coding: utf-8 -*-
#!/usr/bin/env python
# @Author: winsion
# @Email:   1583166253@qq.com
# @Date:   2019-10-20 01:06:24
# @Last Modified by:   winsion
# @Last Modified time: 2019-10-20 13:07:35

import os

currentBranch = input("请输入要推送的分支名:")

work_dir = os.getcwd()

list1 = ['demo', 'lianshi']
for item in list1:
	file_path = os.path.join(work_dir, item) # 拼接完整的路径

	os.chdir(file_path)
	result = os.system("git status")

	os.system("git checkout" + " " + currentBranch)

	message = input("'库' + item + '输入修改的内容(默认:fixBug) :'")
	if len(message) == 0:
		message = "fixBug"
	os.system('git add .')
	os.system("git commit -m " + message)
	os.system('git push')


