import logging
import sys, os
import time

import allure
import pytest

def get_project_path():
    current_path = os.getcwd()
    while True:
        if 'pytest.ini' in os.listdir(current_path):
            return current_path
        current_path = os.path.dirname(current_path)


# 将项目根目录加入到sys.path中，否则提示windowsUI模块找不到
sys.path.append(get_project_path())

from windows_ui.utils.utils_page import *
from windows_ui.page.home_page import HomePage

# 用例执行过程中记录日志
logger = logging.getLogger(__file__)

# 运行用例并生成allure报告
# pytest -s -q --alluredir=./result --clean-alluredir
# 打开报告
# allure serve ./result
# 参阅：https://www.cnblogs.com/uncleyong/p/17958199
class TestLogin:
    user_dict = {}
    login_list = []
    app=None

    @pytest.fixture(autouse=True)
    def init_data(self, global_session_data):
        # 每个测试方法执行前，初始化数据
        self.user_dict = global_session_data[0]
        self.login_list = global_session_data[1]
        self.app=global_session_data[3]

    @pytest.fixture()
    def login01_fixture(self):
        logger.info("login01前置操作")
        yield
        logger.info("login01后置操作")

    # 执行登录
    def test_login01(self, login01_fixture):
        logger.info("test_login01开始执行======")
        # 设置日志描述
        allure.dynamic.title(self.login_list[0].title)
        allure.dynamic.description(self.login_list[0].des)
        # 获取相关业务数据
        phone_num=self.user_dict['phoneNum']
        pass_word=self.user_dict['passWord']
        # 执行登录操作
        home_page = HomePage(self.app)
        home_page.click_login(phone_num,pass_word)
        # 获取页面文本
        page_txt = get_pc_page_txt(self.app)
        # 校验文本
        logger.info("校验页面是否包含文本:" + self.login_list[0].key_word)
        # print(self.login_list[0].key_word)
        assert self.login_list[0].key_word in page_txt
        logger.info("test_login01执行完成======")

    @pytest.fixture()
    def login02_fixture(self):
        logger.info("login02前置操作")
        yield
        logger.info("login02后置操作")

    # 退出登录
    def test_login02(self,login02_fixture):
        logger.info("test_login02开始执行======")
        allure.dynamic.title(self.login_list[1].title)
        allure.dynamic.description(self.login_list[1].des)
        # 获取相关业务数据
        nick_name = self.user_dict['nickName']
        # 执行退出操作
        home_page = HomePage(self.app)
        home_page.click_logout(nick_name)
        # 获取页面文本
        page_txt = get_pc_page_txt(self.app)
        # 校验文本
        logger.info("校验页面是否包含文本:" + self.login_list[1].key_word)
        # print(self.login_list[0].key_word)
        assert self.login_list[1].key_word in page_txt
        logger.info("test_login02执行完成======")

