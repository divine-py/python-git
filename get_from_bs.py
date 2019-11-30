import re
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
import random
from config import headers_li
from mysqlclass import DBHelper_my
from pymsclass import DBHelper_ms
coders=['gb2312','gbk','utf-8']
class get_info():
    def __init__(self):
        self.url=None
        self.rep=None#"p.'gdg'>td"
        self.tag=None
        self.attr=None#dic
        self.filename=None
        self.content=None
        self.sqms=None#sqserver的执行语句
        self.sqmy=None
        self.filepath=None
        self.down_url=None
    def change_ip(self):
        pass
    def delete_cookies(self):
        pass
    def link_page(self,url):
        self.url=url
        head=random.choice(headers_li)
        try:
            response = requests.get(self.url, headers=head, timeout=10)
            for j in coders:
                try:
                    response.encoding=j
                    response.text.encode(j)
                    return response.text
                    break
                except:
                    print( "编码库中的格式不匹配,请检查")
                    continue
        except:
            print( "请求失败,请检查地址是否有效")
    def read_file(self,f_p):
        self.filepath=f_p
        try:
            with open(self.filepath,'r') as f:
                content=f.read()
            return content
        except Exception as e:
            print(e)
            return False
                   
    def bs_find(self,ta,att):
        self.tag=ta
        self.attr=att       
        try:
            htm=self.link_page(self.url)
            con=self.read_file(self.filepath)
            if htm:
                soup=BeautifulSoup(htm,'lxml')
                l_f=soup.find_all(name=self.tag,attrs=self.attr)
                return l_f
            else:
                soup=BeautifulSoup(con,'lxml')
                l_f=soup.find_all(name=self.tag,attrs=self.attr)
                return l_f
                
        except Exception as e:
            print(e)
            return False
         
    def bs_select(self,rep):
        self.rep=rep
        try:
            htm=self.link_page(self.url)
            con=self.read_file(self.filepath)
            if htm:
                soup=BeautifulSoup(htm,'lxml')
                l_s=soup.select(self.rep)
                return l_s
            else:
                soup=BeautifulSoup(con,'lxml')
                l_s=soup.select(self.rep)
                return l_s                
        except Exception as e:
            print(e)
            return False
    def write_to_files(self,nn,cont):#nn为文件名,cont为str类型，一般从bs_select或bs_find遍历
        self.filename=nn
        self.content=cont
        try:
            with open(self.filename, 'a', encoding='utf-8') as f:
                f.write(self.content)
                return True
        except Exception as e:
            print(e)
            return False
    def write_to_mysql(self,sql):
        self.sqmy=sql
        ob1=DBHelper_my()
        ob1.connectiondatabase()
        ob1.execute(self.sqmy)
        ob1.closedatabase()
    def write_to_mssql(self,sql):
        self.sqms=sql
        ob1=DBHelper_ms()
        ob1.connectiondatabase()
        ob1.execute(self.sqms)
        ob1.closedatabase()
    def down_load(self,url,sub_path):#sub_path为文件保存路径
        self.sub=sub_path
        self.down_url=url
        head=random.choice(headers_li)
        try:
            r= requests.get(self.down_url,headers=head, timeout=10)  #创建响应对象
            tem=self.down_url.rpartition('/')
            path = re.sub(tem[0]+tem[1],self.sub,self.down_url)#保存到本地的路径
            # 通过re模块的搜索和替换功能，生成下载文档的保存地址
            path = re.sub('\n','',path)  #删除path末尾的换行符'\n'
            with open(path,"wb") as f:  
                f.write(r.content)  #将响应对象的内容写下来
        except Exception as e:
            print(e)
            return False
        return True

    