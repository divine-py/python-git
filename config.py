
# 写一个配置文件，便于维护程序配置信息
db_config = {
    'host':'localhost',
    'port':3306,
    'username':'root',
    'password':'123',
    'database':'test',
    'charset':'utf8'
}

db_config1 = {
    'host':'localhost',
    'port':1433,
    'username':'sa',
    'password':'123',
    'database':'sales',
    'charset':'utf8'
}

header1 = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Ubuntu Chromium/44.0.2403.89 '
                             'Chrome/44.0.2403.89 '
                             'Safari/537.36'}
header2={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) ' 
                        'AppleWebKit/535.1 (KHTML, like Gecko) ' 
                        'Chrome/14.0.835.163 ' 
                        'Safari/535.1'}
header3={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) ' 
                        'Gecko/20100101 Firefox/6.0 '}
header4={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) ' 
                        'AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 '
                        'Safari/534.50 '}
header5={'User-Agent':'Opera/9.80 (Windows NT 6.1; U; zh-cn) ' 
                        'Presto/2.9.168 Version/11.50 '}
header6={'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E'}
header7={'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}
header8={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; ) ' 
                        'AppleWebKit/534.12 (KHTML, like Gecko) ' 
                        'Maxthon/3.0 Safari/534.12 '}

headers_li=[header1,header2,header3,header4,header5,header6,header7,header8]