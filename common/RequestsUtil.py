import requests
import json

class RequestsUtil:
    session = requests.session()

    def send_request(self,name,method,url,data,**kwargs):
        method = str(method).lower()#改成小写字母
        if method == 'get':
            req = RequestsUtil.session.request(method, url=url, params=data, **kwargs)
        else:
            data=json.dumps(data)
            req = RequestsUtil.session.request(method,url=url,data=data,**kwargs)
        reqTime = req.elapsed.total_seconds()  # 请求消耗时间
        self.logger.get_log().debug(name+'接口响应时间为:%s秒', reqTime)  # 输出接口响应内容
        return req.text