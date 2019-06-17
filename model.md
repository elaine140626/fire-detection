# 数据库设计


## user

储存用户的基本信息

* id(primary_key)
* name（用户名）
* password
* email
* phone
* c_time（用户注册时间）
* layout（用户对布局的设置 在设置页面中）


## video

这个表储存的是用户在设置页面中添加的视频源，因为可能有多个，所以新建一张表

* id(primary_key)
* user_id
* video_url

## message 

这个表储存的是告警信息

* id(primary_key)
* content (告警内容）
* img_url
* c_time(该条信息的生成时间，用户排序）
* serial_number (foreign_key 表示告警设备的序列号）


## user_message

这个表储存的是用户处理过的信息，因为需要标识每个用户对于哪些信息还没有处理，所以反向标记一下处理的...

* id (primary_key)
* user_id (foreign_key)
* message_id (foreign_key)
* true_or_false (这个value 用来标识这条告警信息是否正确）


## device

* serial_number (primary_key)
* location （经纬度信息，可以考虑后续添加百度地图展示等）
* hint (中文提示信息，提示该设备的位置 如“n3北门”）