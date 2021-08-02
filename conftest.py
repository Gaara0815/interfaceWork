import pytest
from common.yaml_util import YamlUtil
from common.logger import Logger
import os
# autouse自动运行
@pytest.fixture(scope='session',autouse=True)
def clear_yaml():
    os.remove(os.getcwd() + '/logs/' + 'out.log')
    logger = Logger(__name__)
    YamlUtil().clear_backup_yaml()
    YamlUtil().del_file()
    logger.get_log().info('清除成功')

