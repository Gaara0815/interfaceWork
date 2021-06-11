import pytest
from common.yaml_util import YamlUtil
from common.RequestsUtil import RequestsUtil
from common.logger import Logger
import json
import ast

class TestApi:
    def setup_class(self):
        self.logger = Logger(__name__)
        self.baseurl = 'http://115.236.35.106:9000'


    # 函数级结束
    def teardown_class(self):
        pass


    @pytest.mark.parametrize('caseinfo',YamlUtil.read_testApi_yaml('testApi.yaml'))
    def test_api1(self,caseinfo):
        method = caseinfo['request']['method']
        url = self.baseurl+caseinfo['request']['url']
        data = caseinfo['request']['data']
        name = caseinfo['name']
        self.logger.get_log().debug(name + '开始测试')
        result = RequestsUtil.send_request(self,name,method,url,data)
        result = json.loads(result)
        self.logger.get_log().debug(name+'用例返回结果为:%s', result)  # 输出接口响应内容
        code = result['code']
        if(code==0):
            token = result['data']['token']
            YamlUtil.write_backup_yaml(self, {'token': token})
        validate = caseinfo['validate']['code']
        assert validate in result.values()
        self.logger.get_log().debug(name+'测试完成')


    @pytest.mark.parametrize('caseinfo', YamlUtil.read_testApi_yaml('testApi.yaml'))
    def test_api2(self, caseinfo):
        method = caseinfo['request']['method']
        url = self.baseurl + caseinfo['request']['url']
        data = caseinfo['request']['data']
        name = caseinfo['name']
        self.logger.get_log().debug(name + '开始测试')
        result = RequestsUtil.send_request(self, name, method, url, data)
        result = json.loads(result)
        self.logger.get_log().debug(name + '用例返回结果为:%s', result)  # 输出接口响应内容
        code = result['code']
        if (code == 0):
            token = result['data']['token']
            YamlUtil.write_backup_yaml(self, {'token': token})
        validate = caseinfo['validate']['code']
        assert validate in result.values()
        self.logger.get_log().debug(name + '测试完成')

    # if __name__ == '__main__':
#     pytest.main(['-vs','test_api.py'])