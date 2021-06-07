import time
import random
from faker import Faker
import pymysql
import os
#设置代理
os.environ['http_proxy'] = 'http://127.0.0.1:8888'
os.environ['https_proxy'] = 'https://127.0.0.1:8888'

def sleep(n_secs):
    time.sleep(n_secs)

def setup_case(name):
    print('测试用例[%s]开始执行~'%name)

def teardown_case(name):
    print('测试用例[%s]执行结束~'%name)

def setup_step(name):
    print('测试步骤[%s]开始执行~'%name)

def teardown_step(name):
    print('测试步骤[%s]执行结束'%name)

# 生成随机数函数
def get_Randrom():
    return ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m',
                                  'l','k','j','i','h','g','f','e','d','c','b','a'], 9))

# 参数化实现重复执行
def get_random_params(min,max,count=3):
    random_list = []
    for i in  range(count):
        random_list.append(random.randint(min,max))
        return random_list

# print(get_random_params(10,20))

def get_random_name(count=1):
    f=Faker(locale='zh_CN')
    name_list = []
    for i in range(0,count):
        name_list.append(f.name())
    return name_list[0]
# print(get_random_name())

#通过连接mysql数据库实现参数化

# #创建连接数据库
# conn = pymysql.connect(host='',port='3306',user='',password='',database='')
# #创建游标，查询数据默认元组类型，此处设置字典类型
# cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
# #执行mysql，并返查询结果
# cur.execute("select * from search_word")
# #fetchone()获取一行数据，fetchall()获取所有数据，返回一个二维的列表
# print(cur.fetchone())
# print(cur.fetchall())
# #关闭游标
# cur.close()
# #关闭数据库连接
# conn.close()

#
def to_iso8859(str):
    return str.encode("utf-8").decode("iso8859-1")

#
def to_utf_8(str):
    return  str.encode("iso8859-1").decode("utf-8")

#乱码处理
if __name__ == '__main__':
    print(to_iso8859('阳光正好'))
    str = 'é³åæ­£å¥½'
    print(to_utf_8(str))





