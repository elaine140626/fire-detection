import json
import login.models as models


class BaseJson(object):
    def __init__(self):
        self.data = {}

    def send(self):
        return json.dumps(self.data)


class User(BaseJson):
    def __init__(self, user: models.User):
        BaseJson.__init__(self)
        self.data['user_name'] = user.name
        self.data['layout'] = user.layout
        self.data['telephone'] = user.phone
        self.data['wechat_id'] = user.wechat_id
        self.data['email'] = user.email


class Message(BaseJson):

    def __init__(self, message: models.Message):
        BaseJson.__init__(self)
        self.data['image_url'] = message.img_url
        self.data['content'] = message.content
        self.data['serial_number'] = message.serial_number
        self.data['id'] = message.id
