import pytest
from common.yaml_util import YamlUtil
from common.RequestsUtil import RequestsUtil
from common.logger import Logger
import json

class TestApi:

    @pytest.mark.parametrize('caseinfo',YamlUtil.read_testApi_yaml('testApi.yaml'))
    def test_api(self,caseinfo):
        self.logger = Logger(__name__)
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        data = caseinfo['request']['data']
        result = RequestsUtil.send_request(self,method,url,data)
        result = json.loads(result)
        self.logger.get_log().debug( '接口的返回结果为:%s', result)  # 输出接口响应内容
        # print(result)

# if __name__ == '__main__':
#     pytest.main(['-vs','test_api.py'])