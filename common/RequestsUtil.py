import requests
import json

class RequestsUtil:
    session = requests.session()

    def send_request(self,method,url,data,**kwargs):
        method = str(method).lower()#改成小写字母
        if method == 'get':
            req = RequestsUtil.session.request(method, url=url, params=data, **kwargs)
        else:
            data=json.dumps(data)
            req = RequestsUtil.session.request(method,url=url,data=data,**kwargs)
        return req.text