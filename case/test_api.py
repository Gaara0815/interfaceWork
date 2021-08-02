import pytest
from common.yaml_util import YamlUtil
from common.RequestsUtil import RequestsUtil
from common.logger import Logger
import json
import ast
import traceback

class TestApi:
    def setup_class(self):
        self.logger = Logger(__name__)
        self.baseurl = 'http://115.236.35.106:9000'
        # self.baseurl ='https://72ad.topjoytec.com'


    # 函数级结束
    def teardown_class(self):
        pass


    @pytest.mark.parametrize('caseinfo',YamlUtil.read_testApi_yaml('testApi.yaml'))
    def test_api1(self,caseinfo):
        method = caseinfo['request']['method']
        url = self.baseurl+caseinfo['request']['url']
        data = caseinfo['request']['data']
        head = caseinfo['request']['head']
        name = caseinfo['name']
        self.logger.get_log().info(name + '开始测试')
        result = RequestsUtil.send_request(self,name,method,url,data,headers=head)
        result = json.loads(result)
        self.logger.get_log().info(name+'用例返回结果为:%s', result)  # 输出接口响应内容
        code = result['code']
        if(code==0):
            token = result['data']['token']
            YamlUtil.write_backup_yaml(self, {'token': token})
            uid = result['data']['uid']
            YamlUtil.write_backup_yaml(self, {'uid': uid})
        validate = caseinfo['validate']['code']
        assert validate in result.values()
        self.logger.get_log().info(name+'测试完成')


    @pytest.mark.parametrize('caseinfo', YamlUtil.read_testApi_yaml('getTest.yaml'))
    def test_api2(self, caseinfo):
        method = caseinfo['request']['method']
        url = self.baseurl + caseinfo['request']['url']
        data = caseinfo['request']['data']
        head = caseinfo['request']['head']
        backupData =  YamlUtil.read_backup_yaml(self)
        token = backupData['token']
        head['ACCESS_TOKEN'] = token
        name = caseinfo['name']
        self.logger.get_log().info(name + '开始测试')
        result = RequestsUtil.send_request(self, name, method, url, data, headers=head)
        result = json.loads(result)
        self.logger.get_log().info(name + '用例返回结果为:%s', result)  # 输出接口响应内容
        code = result['code']
        validate = caseinfo['validate']['code']
        assert validate in result.values()
        self.logger.get_log().info(name + '测试完成')

    # if __name__ == '__main__':
#     pytest.main(['-vs','test_api.py'])