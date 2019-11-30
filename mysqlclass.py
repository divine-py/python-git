#coding=utf-8

# 读取配置文件信息，连接MySQL数据库进行数据库操作
import pymysql
import sys
from config import db_config
class DBHelper_my():
    # 构造函数,初始化数据库连接
    def __init__(self):
        self.conn = None
        self.cur = None

    def connectiondatabase(self):
        print(db_config['host'],db_config['username'],db_config['password'],db_config['database'],db_config['charset'])
        try:
            self.conn = pymysql.connect(db_config['host'],db_config['username'],db_config['password'],db_config['database'],charset=db_config['charset'])
        except:
            return False
        self.cur = self.conn.cursor()
        return True



    # 关闭数据库
    def closedatabase(self):
        # 如果数据打开，则关闭；否则没有操作
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
        return True

    # 执行数据库的sq语句,主要用来做插入操作
    def execute(self,sql):
        self.connectiondatabase()
        try:
            if self.conn and self.cur:
                # 正常逻辑，执行sql，提交操作
                self.cur.execute(sql)
                self.conn.commit()
        except Exception as e:
            print(e)
            return False
        return True
 
    # 用来查询表数据
    def select(self,sql):
        self.connectiondatabase()
        self.cur.execute(sql)
        result = self.cur.fetchall()
        print(result)
        return result
    
    
    

