import requests
import json

class RequestsUtil:
    session = requests.session()

    def send_request(self,name,method,url,data,**kwargs):
        method = str(method).lower()#改成小写字母
        if method == 'get':
            try:
                # req = RequestsUtil.session.request(method, url=url, params=data, headers=head,**kwargs)
                req = RequestsUtil.session.request(method, url=url, params=data, **kwargs)
            except Exception as e:
                self.logger.get_log().info('用例请求返回失败，{}'.format(e))

        else:
            data=json.dumps(data)
            try:
                req = RequestsUtil.session.request(method, url=url, data=data,  **kwargs)
                # req = RequestsUtil.session.request(method, url=url, data=data, headers=head, **kwargs)
            except Exception as e:
                self.logger.get_log().info('用例请求返回失败，{}'.format(e))
        reqTime = req.elapsed.total_seconds()  # 请求消耗时间
        self.logger.get_log().info(name+'接口响应时间为:%s秒', reqTime)  # 输出接口响应内容
        return req.text