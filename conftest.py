import pytest
from common.yaml_util import YamlUtil
from common.logger import Logger

# autouse自动运行
@pytest.fixture(scope='session',autouse=True)
def clear_yaml():
    logger = Logger(__name__)
    YamlUtil().clear_backup_yaml()
    logger.get_log().debug('清除成功')

