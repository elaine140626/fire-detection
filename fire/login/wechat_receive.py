import xml.etree.ElementTree as ET


def parse_xml(data):
    if len(data) == 0:
        return None
    xmlData = ET.fromstring(data)
    msg_type = xmlData.find('MsgType').text
    print(msg_type)
    print(xmlData)
    print(data)

    if msg_type == "text":
        return TextMsg(xmlData)
    elif msg_type == "image":
        return ImageMsg(xmlData)
    elif msg_type == "event":
        return EventMsg(xmlData)


class Msg(object):
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find("ToUserName").text
        self.FromUserName = xmlData.find("FromUserName").text
        self.CreateTime = xmlData.find("CreateTime").text
        self.MsgType = xmlData.find("MsgType").text


class TextMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.Content = xmlData.find('Content').text


class ImageMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.PicUrl = xmlData.find('PicUrl').text
        self.MediaId = xmlData.find('MediaId').text

class EventMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.EventKey = xmlData.find('EventKey').text
        self.Event = xmlData.find('Event').text
