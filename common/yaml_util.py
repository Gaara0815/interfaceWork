import os
from common.logger import Logger
import yaml


class YamlUtil:
    #读取yaml文件
    def read_backup_yaml(self,key):
        with open(os.getcwd()+'/backup.yaml',mode='r',encoding='utf-8') as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
            return value[key]

    #写入yaml文件 mode='a'追加， mode='w'替换
    def write_backup_yaml(self,data):
        logger = Logger(__name__)
        with open(os.getcwd()+'/backup.yaml',mode='a',encoding='utf-8') as f:
            yaml.dump(data=data,stream=f,allow_unicode=True)
            # logger.logger.debug('写入成功:%s',str(data))

    #清除yaml文件
    def clear_backup_yaml(self):
        with open(os.getcwd()+'/backup.yaml',mode='w',encoding='utf-8') as f:
            f.truncate()


#读取yaml文件
    def read_testApi_yaml(yaml_name):
        with open(os.getcwd()+'/case/'+yaml_name,mode='r',encoding='utf-8') as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
            return value