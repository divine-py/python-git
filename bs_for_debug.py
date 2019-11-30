from get_from_bs import get_info
import threading
file1='./index_f.html'
file2='./tongxun.html'

bs1=get_info()
bs2=get_info()
tag='div'
att={'class':'content'}
rep="a[href]"
# li=bs1.bs_find(tag, att)
# li=bs1.bs_select(rep)
# htm=bs1.link_page(url)
htm1=bs1.read_file(file1)
li=bs1.bs_find(tag, att)
l=bs1.bs_select(rep)
htm2=bs2
print(l)
threading.Thread(target=read_server, args=(s, )).start()