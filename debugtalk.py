
import time
import requests

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


def get_username():
    pass