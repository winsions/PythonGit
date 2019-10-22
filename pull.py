# -*- coding: utf-8 -*-
#!/usr/bin/env python
# @Author: winsion
# @Email:   1583166253@qq.com
# @Date:   2019-10-20 01:06:24
# @Last Modified by:   winsion
# @Last Modified time: 2019-10-22 10:53:20

import os

currentBranch = input("请输入当前分支名:")
statusBranch = input("请输入当前目标分支名:")
if len(currentBranch) == 0:
	currentBranch = "winsion"
if len(statusBranch) == 0:
	statusBranch = "dev"

work_dir = os.getcwd()

# 修改自己本地的组件目录
list1 = ['basebusinesscomponent', 'homepagecomponent', 'loginregistercompoment-', 'routercomponent', 'sportcomponent', 'taskcentercomponent', 'userinfocomponent', 'utilitytoolcomponentoc',
 'utilitytoolcomponentswift', 'walletcomponent']
for x in list1:
	file_path = os.path.join(work_dir, x) # 拼接完整的路径

	os.chdir(file_path)
	os.system("git status")

	os.system("git add .")
	os.system("git stash")

	os.system("git checkout" + " " + statusBranch)
	os.system("git pull origin" + " " + statusBranch)

	os.system("git checkout" + " " + currentBranch)
	os.system("git rebase" + " " + statusBranch)
	os.system('git stash pop')

# 进入主工程  pod install   //修改为自己主工程的目录
file_path = os.path.join(work_dir, "yyproject的副本") # 拼接完整的路径   
os.chdir(file_path)
os.system('pod install')
