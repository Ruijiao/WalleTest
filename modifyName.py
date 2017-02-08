import os
#通过python脚本修改打包后的apk名字
for file in os.listdir('.'):
	if os.path.isfile(file):
		extension = os.path.splitext(file)[1][1:]
        if extension in 'apk':
			filename = os.path.basename(file)
			newfilename = filename
			#把默认的app-release-去掉，只留以渠道名作为apk的名字
			if filename.find("app-release-") != -1:
				newfilename = filename.replace("app-release-","",1)
				os.rename(filename,newfilename)
			if newfilename.find("xiangha") != -1:
				os.rename(newfilename,newfilename.replace("xiangha","Xiangha",1))
			