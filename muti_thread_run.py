
import threading 
import time
from get_from_bs import get_info
import re
from bs4.element import Tag
class mythread1(threading.Thread):
    def __init__(self,threadname,url,tag,att):
        threading.Thread.__init__(self,name=threadname)
        self.url=url
        self.tag=tag
        self.att=att
    def run(self):
        ob1=get_info()
        ob1.read_file(self.url)
        li=ob1.bs_find(self.tag, self.att)
        for i in li:
            if type(i)==Tag:
                con=i.get_text()
                sql="insert into bs4 (con) values('%s') "%con
                ob1.write_to_mssql(sql)
# if __name__=="__main__":
#     ur1='./index_f.html'
#     ur2='./tongxun.html'
#     tag1='div'
#     att1={'class':'content'} 
#     tag2='li'
#     att2=None
#     bs1=mythread1('1111',ur1,tag1,att1)
#     bs1.start()
#     bs2=mythread1('2222',ur2,tag2,att2)
#     bs2.start()
#     
          
