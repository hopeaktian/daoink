# rooins
- 袋鼠打印，在线共享打印平台: http://www.daoink.com

![APP首页1](https://github.com/hopeaktian/demo/blob/master/rooins1.png)
![APP首页2](https://github.com/hopeaktian/demo/blob/master/rooins2.png)
![APP首页3](https://github.com/hopeaktian/demo/blob/master/rooins3.png)
![APP首页4](https://github.com/hopeaktian/demo/blob/master/rooins4.png)

## 1. 简介
### 理念 
袋鼠打印是一个互联网在线共享打印平台，此平台旨在将普通打印店的打印机连接至我们的平台上，然后使用户可以通过我们的平台快速找到附近最近的打印点，再使用APP远程提交打印文件，打印点打印完成后再通知用户前往打印店领取打印好的文件。
### 特色
- 袋鼠打印平台非常适用于用户庞大的地点，例如学校，医院等，这些场所有庞大的打印需求用户但是打印点不多，容易造成用户在打印店排队。
- 就学校而言，我们调查发现，大学里的打印店一般为4个左右，学生前往打印店打印文件需要排队的概率大概为80%, 每次去打印店完成一次普通的打印,平均需要花费5分钟左右的时间(不包括排队时间)，加上排队，花费的时间一般就需要10分钟以上了。袋鼠打印平台很好地解决了用户打印排队以及在打印店电脑上操作的时间，用户只需远程通过APP选择附近打印点，提交打印文件，然后系统打印好后会通知用户前往打印店领取文件。整个流程免去了人工排队环节，省时省力，方便快捷。
### 开发团队
国内某一本大学的在校大学生，对互联网技术充满热情，渴望通过技术打破传统常规，梦想着用知识改变世界。
- 前端：糯米 https://github.com/Aninassimova
- 后端：落风 http://git.careyou.xin

## 2. 技术文档
### 技术架构
1. 后端：python2.7版本，Flask Web框架，MySQL数据库
2. 前端：Weui框架，light框架，mui框架
3. 服务端：centos7 apache(或Nginx)
4. 硬件：raspberry3B(树莓派), 普通打印机
### APP的安装部署
#### 1. 下载源码到服务器, 下载目录自定义, 此文全篇以```/var/www/```为例子
``cd /var/www``\
``git clone https://github.com/hopeaktian/rooins.git``
#### 2. 创建python2.7 虚拟环境 
1. 安装 virtualenv 工具
 - centos: ``sudo yum install virtualenv -y``
 - debian: ``sudo apt-get install virtualenv -y`` 
2. 使用virtualenv创建虚拟环境，注意：先cd进入rooins 项目目录再执行virtualenv命令 
 ``cd /var/www/rooins`` \
 ``virtualenv env -p /usr/bin/python2.7``
#### 3. 安装此项目的python依赖包
1. 首先激活虚拟环境的python命令
``cd /var/www/rooins``\
``source ./env/bin/activate``
2. 安装依赖包\
``pip install -r /var/www/rooins/requirements.txt``
#### 4. 修改数据库配置文件
1. 首先请自行准备好MySQL数据库,并在数据库中创建好此项目的库(此教程以库名rooprint为例)
2. 在服务器上修改数据库配置 \
``cd /var/www/roorins/app``\
``vim config.py``\
将config.py中的第9行修改为自己的数据库用户，密码，数据库地址，数据库名
#### 5. 运行
1. 方法一：直接使用python命令运行(不推荐)\
首先激活python虚拟环境
``source /var/www/rooins/env/bin/activate``\
然后运行
``python manage.py server``

2. 方法二：以Apache wsgi的的方式运行
- 首先创建wsgi文件
参考示例：\
rooins.wsgi
```
import sys


python_home = '/var/www/rooins/env'

activate_this = python_home + '/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

sys.path.insert(0, '/var/www/rooins/')

from app import app

application = app
```
- 然后在Apache中配置wsgi，具体方法参考https://dormousehole.readthedocs.io/en/latest/deploying/mod_wsgi.html \
配置好后，重启Apache,就可以访问。

### 树莓派端部署
具体请参考树莓派端代码库：https://github.com/hopeaktian/rooins-raspberry
