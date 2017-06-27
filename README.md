# WalleTest
## 美团打包工具walle的集成
### 集成步骤按照<a href="https://github.com/Meituan-Dianping/walle">官方文档</a>
### 这只是能打出一个或一批apk，但是不能满足我的需求
#### 需求一、修改打出后的文件名为渠道名
##### walle目前办不到，也询问过维护文员，目前还不支持，打出的包是以app-release-开头。
#### 解决办法：
##### 通过python脚本批量修改apk文件名，<a href="https://github.com/Ruijiao/WalleTest/blob/master/modifyName.py">脚本文件</a> 已上传 
#### 需求二、不同渠道换不同的欢迎图
##### 由于欢迎图片都要编译在apk中，在channelinfo中指明用那张图，欢迎页通过获取channelinfo中的图片再去加载对应的图
#### 解决办法：
<pre>
<code>
sourceSets {
        main {
            res.srcDirs = ['src\\main\\res', 'src\\main\\res_normal']
//            res.srcDirs = ['src\\main\\res','src\\main\\res_360']
            jniLibs.srcDirs = ['libs']
        }
    }
</code>
</pre>
 #### 每个欢迎图放在不同的文件夹，每打一个包，修改一下这个欢迎图的路径
 
## 用法
### 1、打一个渠道
 gradlew clean assembleRelease -PchannelList=baidu
### 2、打多个渠道,用逗号分隔
 gradlew clean assembleRelease -PchannelList=baidu,360
### 3、批量打包，<a href="https://github.com/Ruijiao/WalleTest/blob/master/channel_all">批量打包实例文档 channel_all</a>
 gradlew clean assembleRelease -PchannelFile=channel_all

##### 需求三 一些平台需要加固，加固后则walle的渠道就丢失了<加固的方式把walle的渠道文件删除了>
##### 解决办法：
加固后，通过脚本重新进行签名与添加渠道
第一步：安装python工具
第二步：下载我demo中所需的工具与脚本，文件夹名：walle签名添加渠道命令
第三步：在cmd中进入下载的资源文件夹，运行adb命令
test.apk是加固后的apk；test.jks是你的签名文件；channel是要签名后出哪几个渠道包，执行命令.txt记录了要执行的adb命令；
channel.py是编写的python脚本；其他为用到的工具