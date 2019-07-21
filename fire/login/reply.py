import time
import login.wechat_receive as receive
import login.models as models
import json,os
import requests

URL_PREF = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token="
HEADERS = {
    "Content-Type": "application/json"
}


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


class ImageTextMsg(Msg):
    def __init__(self, toUserName, fromUserName, articles, title, description, picUrl, url):
        Msg.__init__(self)
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Articles'] = articles
        self.__dict['Title'] = title
        self.__dict['Description'] = description
        self.__dict['PicUrl'] = picUrl
        self.__dict['Url'] = url

    def send(self):
        XmlForm = """<xml>
            <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
            <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
            <CreateTime>{CreateTime}</CreateTime>
            <MsgType><![CDATA[news]]></MsgType>
            <ArticleCount>1</ArticleCount>
            <Articles>
            <item>
            <Title><![CDATA[{Title}]]></Title>
            <Description><![CDATA[{Description}]]></Description>
            <PicUrl><![CDATA[{PicUrl}]]></PicUrl>
            <Url><![CDATA[{Url}]]></Url>
            </item>
            </Articles>
            </xml>
            """
        return XmlForm.format(**self.__dict)


def getUserId(rec_msg):
    if models.User.objects.filter(wechat_id=rec_msg.FromUserName).exists():
        return models.User.objects.get(wechat_id=rec_msg.FromUserName).id
    else:
        return ""


def DealWithEventMsg(rec_msg: receive.ClickEventMsg):
    if rec_msg.EventKey == "BIND_ACCOUNT":
        return TextMsg(rec_msg.FromUserName, rec_msg.ToUserName,
                       "输入\"bind 用户名 密码\"来绑定账户\n如用户名为： 123 密码为：456\n那么输入\"bind 123 456\"(不带引号)")
    elif rec_msg.EventKey == "UN_CHECK":
        theId = getUserId(rec_msg)
        if theId != "":
            user_message = models.User_Message.objects.values('message_id').filter(user_id=theId)
            user_message_list = [i['message_id'] for i in user_message]
            message_list = models.Message.objects.exclude(id__in=user_message_list)
            the_url = message_list[len(message_list) - 1].img_url
            return ImageTextMsg(rec_msg.FromUserName, rec_msg.ToUserName, "articles", "告警图片", "Description", the_url,
                                the_url)
        else:
            return TextMsg(rec_msg.FromUserName, rec_msg.ToUserName, "请先绑定用户")
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
                if str_arr[1] != user.password:
                    ret = "密码不正确，请检查后重新输入"
                else:
                    user.wechat_id = rec_msg.FromUserName
                    user.save()
                    ret = "成功绑定微信:)"
            else:
                ret = "用户不存在，请重新检查后输入"

    else:
        ret = "无法识别该操作:)"

    return TextMsg(rec_msg.FromUserName, rec_msg.ToUserName, ret)


def UserAdded(rec_msg: receive.SubScribeEventMsg):
    if models.WechatUser.objects.filter(open_id=rec_msg.FromUserName).exists():
        return
    models.WechatUser.objects.create(open_id=rec_msg.FromUserName)


def UserDeled(rec_msg: receive.UnsubscribeEventMsg):
    if models.WechatUser.objects.filter(open_id=rec_msg.FromUserName).exists():
        models.WechatUser.objects.filter(open_id=rec_msg.FromUserName).delete()


def GetToken():
    if os.path.exists("token"):
        f = open("./token", "r")
        token = f.readline()
        f.close()
        if token == "":
            return "a"
        else:
            return token
    else:
        return "a"


def send_message(to_user, img_url, serial_number, warning_date, warning_message, hint):
    url = URL_PREF + GetToken()
    print(url)
    data = GetData(to_user, img_url, serial_number, warning_date, warning_message, hint)
    result = requests.post(url, data.encode('utf-8'), headers=HEADERS)
    return result


def GetData(to_user, img_url, serinal_number, time, message, hint):
    js = '''
    {
               "touser":"''' + to_user + '''",
               "template_id":"4kQKcX7o1pZbJp99g0pdvacBt_ozbdv_JK58BpVK69s",
               "url":"''' + img_url + '''",
               "data":{
                       "serialnumber": {
                           "value":"''' + serinal_number + '''",
                           "color":"#173177"
                       },
                       "time":{
                           "value":"''' + time + ''''",
                           "color":"#173177"
                       },
                       "message": {
                           "value":"''' + message + '''",
                           "color":"#173177"
                       },
                       "hint": {
                           "value":"''' + hint + ''''",
                           "color":"#173177"
                       }
               }
           }
    '''
    return js


def ReGetToken():
    res = requests.get("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxea2334a522002dc8&secret=8bd4a32def3d70e81847249dc4a86806")
    ret = json.loads(res.content)
    print(ret)
    f = open("./token","w")
    f.writelines(ret['access_token'])
    f.close()


def WechatSend(to_user, img_url, serial_number, warning_date, warning_message, hint):
    result = send_message(to_user, img_url, serial_number, warning_date, warning_message, hint)
    cnt = 5
    while cnt >0:
        cnt -=1
        print(result.content)
        resd = json.loads(result.content.decode())
        print(resd['errcode'])
        if resd['errcode'] == 40001 or resd['errcode'] == 42001:
            ReGetToken()
            result = send_message(to_user, img_url, serial_number, warning_date, warning_message, hint)
        else:
            break

def WarningMessageToAll(img_url, serial_number, warning_date, warning_message, hint):
    open_ids = models.User.objects.all()
    for i in openIds:
        WechatSend(i.wechat_id, img_url, serial_number, warning_date, warning_message, hint)
