# import random
# li=['agg','gasd','gag','egah','grhahh']
# ll=random.choice(li)
# print(type(ll))
# s="https://kar98.tech/download/dgeg.dd"
# t=s.rpartition('/')
# ss=t[0]+t[1]
# print(type(ss))
import threading 
import time
from get_from_bs import get_info
import re
ll=get_info()
url="http://www.win4000.com/wallpaper_big_162102.html"
cc=ll.link_page(url)
print(cc)
ss=".picBox li img"
cont=ll.bs_select(ss)
su_p="E:/get_file/"
for i in cont:
   ul=i['src']
   print(ul)
   sql="insert into img_tab(url) values('%s')"%ul
   ll.write_to_mssql(sql)
#    ll.down_load(ul, su_p)
    
# ll.down_load(lin2, ss_l)
