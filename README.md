# fire-detection
烟火检测


该项目目前有五个页面，分别是 login, overview, warning, conf, monitor

## login

![设计图](http://github.com/xwxztq/fire-
detection/raw/master/pic/login.jpg)

login是登陆页面

[登陆页面](http://188.131.241.21/login.html)

### TODO
需要完成用户登陆。

这里还必须完成后续页面访问的状态保持。

目前lxl采用cookie+session的方式来去完成

## overview

![设计图](http://github.com/xwxztq/fire-detection/raw/master/pic/overview.jpg)

这里是系统的一个总览部分，需要完成的功能点比较多。但目前有一些主要是假功能点，所以工程量尚可

[总览页面](http://188.131.241.21/overview.html)
### TODO

* 设备安装统计图（假）
* 装备在线统计图（假）
* 气象统计图（假）
* 前三个的总览图（假）
* 状态轮播图（真）
  * 需要前端完成图片轮播
  * 需要后端返回图片url
* 预警信息
	* 需要前端完成预警信息展示
	* 需要后端完成信息接口


## monitor

这是一个实时视频流的播放，需要从后端获取**该用户**要播放的视频流，然后放在页面上播放，播放时可以设置布局（如一行一个，一行两个，一行四个）

[监控页面](http://188.131.241.21/monitor.html)

**设计图**

![pic](http://github.com/xwxztq/fire-detection/raw/master/pic/monitor.jpg)

### TODO

1. 后端需要写数据库储存每个用户设置的视频流，目前设想的是对每个用户添加(user_id,video_id)数据，然后去做进一步处理
2. 后端需要去写这部分的逻辑：对于每一个用户返回改用户的所有视频流地址
3. 前端需要去写支持修改布局的逻辑（一个两个四个，适配flash窗口大小）
4. 前端去写播放多个视频流的逻辑（动态添加flash视频流）

## warning

这部分是报警信息，有审核状态和未审核状态。这部分可以支持对报警信息进行审核。

[报警页面](http://188.131.241.21/warning.html)

**设计图**
![pic](http://github.com/xwxztq/fire-detection/raw/master/pic/warning.jpg)

### TODO

#### 前端
1. 添加审核通过与不通过逻辑及按钮
2. 添加动态添加信息逻辑

#### 后端
1. 设计数据库，表示用户与报警信息之间的关系
2. 返回一个用户对应的所有的报警信息的状态，或者设置分页加载


## conf

这部分是用户的系统设置界面，目前的功能是：
1. 设置视频流的播放
2. 设置短信推送号码

### TODO

#### 前端
1. 设计页面
2. 完成以上逻辑

#### 后端
1. 设计数据库储存相关信息
2. 当有报警信息时，向每个用户设置的手机号码发送报警信息