# -*- coding: utf-8 -*-
#!/usr/bin/env python
# @Author: winsion
# @Email:   1583166253@qq.com
# @Date:   2019-10-20 01:06:24
# @Last Modified by:   winsion
# @Last Modified time: 2019-10-20 12:56:49

import os

currentBranch = input("请输入当前分支名:")
statusBranch = input("请输入当前目标分支名:")
if len(currentBranch) == 0:
	currentBranch = "winsion"
if len(statusBranch) == 0:
	statusBranch = "develop"

work_dir = os.getcwd()

list1 = ['demo', 'lianshi']
for x in list1:
	file_path = os.path.join(work_dir, x) # 拼接完整的路径

	os.chdir(file_path)
	result = os.system("git status")

	os.system("git add .")
	os.system("git stash")
	

	os.system("git checkout" + " " + statusBranch)
	os.system("git pull")

	os.system("git checkout" + " " + currentBranch)
	os.system("git rebase" + " " + statusBranch)
	os.system('git stash pop')

	os.system('git add .')
	os.system("git commit -m '提交2'")
	os.system('git push')


