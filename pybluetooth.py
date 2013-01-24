import sys, threading, time
import serial
from weibo import APIClient


def com_serial():
    se = serial.Serial("com9",38400, timeout=1)
    print se.isOpen()
    data = ""
    try:
        while True:
            while se.inWaiting() > 0:
                s = se.read(1)
                if s == '=':
                    data = data[::-1]
                    weight = float(data)
                    if weight > 0:
                        print weight
                    data = ""
                else:
                    data += s
    except:
        se.close()


def weibo_connect():
    app_key = "2247462658"
    app_secret = "c59e5be3c8e4ca8878421a6afda66f45"
    call_back_url = "https://api.weibo2.com/oauth2/default.html"
    access_token = "9c567e50a7726eef5d8c9f18ef872c9a"

    client = APIClient(app_key=app_key, app_secret=app_secret)
   # url = client.get_authorize_url()
    #print url
    r = client.request_access_token(access_token)
    client.set_access_token(r.access_token, r.expires_in)
    print client.post.statuses__update(status=u'test')

if __name__ == "__main__":
    weibo_connect()