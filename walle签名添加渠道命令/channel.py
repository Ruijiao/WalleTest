#coding=utf-8

import zipfile
import shutil
import os
import sys

if __name__ == '__main__':

    #序列化
    #windows
    os.system('zipalign_batch.bat '+sys.argv[1])
    
    #签名
    #windows
	#--ks指定keystore 后面跟着密码  --ks-key-alias指定别名 后面跟着密码   密码都是以此开头--key-pass
    os.system('E:/softWhare/android_studio_sdk/build-tools/25.0.0/apksigner sign --ks test.jks --ks-pass pass:xxxxxx --ks-key-alias mimimi --key-pass pass:xx.comTest ./zipaligned/'+sys.argv[1]+'.apk')
    #渠道化
    if os.path.exists('./release'):
        shutil.rmtree('./release')
    os.mkdir('./release')
    os.system('java -jar walle-cli-all.jar batch -f channel'+' ./zipaligned/'+sys.argv[1]+'.apk ./release/')


