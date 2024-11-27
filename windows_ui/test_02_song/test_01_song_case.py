import logging
import os
import sys
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

from windows_ui.page.home_page import HomePage
from windows_ui.utils.utils_page import *

# 用例执行过程中记录日志
logger = logging.getLogger(__file__)


class TestSong:
    user_dict = {}
    song_list = []
    app=None


    @pytest.fixture(autouse=True)
    def init_data(self, global_session_data):
        # 每个测试方法执行前，初始化数据
        self.user_dict = global_session_data[0]
        self.song_list = global_session_data[2]
        self.app = global_session_data[3]

    # 搜索歌曲
    def test_song01(self):
        logger.info("test_song01开始执行======")
        # 设置日志描述
        allure.dynamic.title(self.song_list[0].title)
        allure.dynamic.description(self.song_list[0].des)
        # 获取相关业务数据
        song_name = self.user_dict['songName']
        # 执行登录操作
        home_page = HomePage(self.app)
        home_page.search_song(song_name)
        # 获取页面文本
        page_txt = get_pc_page_txt(self.app)
        # 校验文本
        logger.info("校验页面是否包含文本:" + self.song_list[0].key_word)
        assert self.song_list[0].key_word in page_txt
        logger.info("test_song01执行完成======")

