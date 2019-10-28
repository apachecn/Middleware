#!/usr/bin/python
# coding:utf-8
# -------------------------------------------------------------------------------
# Name: 爬取微博的数据
# Purpose: 找出相近的词
# Author:  jiangzhonglian
# Create_time :  2018年9月14日
# Update_time:   2018年9月14日
# Content:
# Copyright:   (c) jiangzhonglian 2018
# Licence:   <do yourself>
# -------------------------------------------------------------------------------
from pymysql import *


class MySQL:
    def __init__(self,
                 database,
                 host="127.0.0.1",
                 user="xxx",
                 password="xxx",
                 port=3306,
                 charset="utf8"):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database
        self.charset = charset

    # 数据库连接方法:
    def open(self):
        self.db = connect(
            host=self.host,
            user=self.user,
            password=self.password,
            port=self.port,
            database=self.database,
            charset=self.charset)
        # 游标对象
        self.cur = self.db.cursor()

    # 数据库关闭方法:
    def close(self):
        self.cur.close()
        self.db.close()

    # 数据库执行操作方法:
    def execute(self, sql, L=[]):
        try:
            self.open()
            self.cur.execute("%s;" % sql, L)
            self.db.commit()
            print("ok")
            msg = "success"
        except Exception as e:
            # 错误回滚
            self.db.rollback()
            print("Failed", e)
            msg = "fail"
        finally:
            self.close()
        # 返回统一状态
        return msg


    # 数据库查询所有操作方法:
    def execute_all(self, sql, L=[]):
        try:
            self.open()
            self.cur.execute("%s;" % sql, L)
            self.cur.fetchall()
            print("ok")
            msg = "success"
        except Exception as e:
            # 错误回滚
            self.db.rollback()
            print("Failed", e)
            msg = "fail"
        finally:
            self.close()
        # 返回统一状态
        return msg