import os
from common.logger import Logger
import yaml


class YamlUtil:
    #读取yaml文件
    def read_backup_yaml(self):
        with open(os.getcwd()+'/backup.yaml',mode='r',encoding='utf-8') as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
            return value

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
#清除temp文件夹里面文件
    def del_file(self):
        path_data = os.getcwd()+'/temp'
        print(path_data)
        for i in os.listdir(path_data):  # os.listdir(path_data)#返回一个列表，里面是当前目录下面的所有东西的相对路径
            file_data = path_data + "\\" + i  # 当前文件夹的下面的所有东西的绝对路径
            if os.path.isfile(file_data) == True:  # os.path.isfile判断是否为文件,如果是文件,就删除.如果是文件夹.递归给del_file.
                os.remove(file_data)
            else:
                del_file(file_data)


