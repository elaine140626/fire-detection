import time
import login.wechat_receive as receive


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
    if content[:4] == "bind":
        return TextMsg(rec_msg.FromUserName, rec_msg.ToUserName, "bind")
    else:
        return TextMsg(rec_msg.FromUserName, rec_msg.ToUserName, "not bind")
