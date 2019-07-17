import time
import login.wechat_receive as receive
import re
import login.models as models


class Msg(object):
    def __init__(self):
        pass

    def send(self):
        return "success"


class TextMsg(Msg):
    def __init__(self, toUserName, fromUserName, content):
        Msg.__init__(self)
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content

    def send(self):
        XmlForm = """<xml><ToUserName><![CDATA[{ToUserName}]]></ToUserName><FromUserName><![CDATA[{FromUserName}]]></FromUserName><CreateTime>{CreateTime}</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[{Content}]]></Content></xml>"""
        return XmlForm.format(**self.__dict)


class ImageMsg(Msg):
    def __init__(self, toUserName, fromUserName, mediaId):
        Msg.__init__(self)
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = mediaId

    def send(self):
        XmlForm = """<xml>
            <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
            <FromUserName><![CDATA[FromUserName}]]></FromUserName>
            <CreateTime>{CreateTime}</CreateTime>
            <MsgType><![CDATA[image]]></MsgType>
            <Image>
            <MediaId><![CDATA[{MediaId}]]></MediaId>
            </Image>
            </xml>
            """
        return XmlForm.format(**self.__dict)


def DealWithEventMsg(rec_msg: receive.EventMsg):
    if rec_msg.EventKey == "BIND_ACCOUNT":
        return TextMsg(rec_msg.FromUserName, rec_msg.ToUserName,
                       "输入\"bind 用户名 密码\"来绑定账户\n如用户名为： 123 密码为：456\n那么输入\"bind 123 456\"(不带引号)")
    else:
        return TextMsg(rec_msg.FromUserName, rec_msg.ToUserName, "这个功能还莫得开发")


def DealWithTextMsg(rec_msg: receive.TextMsg):
    content = rec_msg.Content
    print(content)
    print(content[:4])

    ret = ""
    if content[:4] == "bind":
        str_arr = content[4:].strip().split(' ')
        print(str_arr)
        if len(str_arr) != 2:
            ret = "除content外，有两个字符串"
        else:
            if models.User.objects.filter(name=str_arr[0]).exists():
                user = models.User.objects.get(name=str_arr[0])
                ret = user.password
                user.wechat_id = rec_msg.FromUserName
                user.save()
                user = models.User.objects.get(name=str_arr[0])
                ret = user.wechat_id
            else:
                ret = "用户不存在，请重新检查后输入"

    else:
        ret = "无法识别该操作:)"

    return TextMsg(rec_msg.FromUserName, rec_msg.ToUserName, ret)
