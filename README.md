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

 #### 每个欢迎图放在不同的文件夹，每打一个包，修改一下这个欢迎图的路径
