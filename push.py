# -*- coding: utf-8 -*-
#!/usr/bin/env python
# @Author: winsion
# @Email:   1583166253@qq.com
# @Date:   2019-10-20 01:06:24
# @Last Modified by:   winsion
# @Last Modified time: 2019-10-22 10:56:56

import os

currentBranch = input("请输入要推送的分支名:")
if len(currentBranch) == 0:
	currentBranch = "winsion"

work_dir = os.getcwd()

# 修改为自己组件工程的目录
list1 = ['basebusinesscomponent', 'homepagecomponent', 'loginregistercompoment-', 'routercomponent', 'sportcomponent', 'taskcentercomponent', 'userinfocomponent', 'utilitytoolcomponentoc',
 'utilitytoolcomponentswift', 'walletcomponent']
for x in list1:
	print(work_dir)
	file_path = os.path.join(work_dir, x) # 拼接完整的路径

	os.chdir(file_path)
	os.system("git status")

	os.system("git checkout" + " " + currentBranch)

	message = input('库:' + x + '输入修改的内容(默认:fixBug) :')
	if len(message) == 0:
		message = "fixBug"
	os.system('git add .')
	os.system("git commit -m " + message)
	os.system('git push origin ' + currentBranch)



