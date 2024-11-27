import logging
import sys, os
import pytest




def get_project_path():
    current_path = os.getcwd()
    while True:
        if 'pytest.ini' in os.listdir(current_path):
            return current_path
        current_path = os.path.dirname(current_path)


# 将项目根目录加入到sys.path中，否则提示windowsUI模块找不到
sys.path.append(get_project_path())

from windows_ui.utils.utils_app import *
from windows_ui.utils.utils_data import *


logger = logging.getLogger(__file__)

# 读取excel数据
@pytest.fixture(scope="session", autouse=True)
def global_session_data():
    """全局共享的 session 级别 fixture"""
    print("\n前置：给测试函数设置一个session")
    logger.info("读取excel数据")
    # 读取业务数据
    user_dict, login_list, song_list = read_pc_data_excel()
    # 启动应用
    logger.info("启动应用")
    install_path=user_dict['installPath']
    app = start_pc_app(install_path)

    yield user_dict, login_list, song_list,app
    # 返回多个参数，本质是 tuple,通过下标按需回去对于的参数例如 global_session_data[1]是login_list
    print("\n后置：清理环境、退出应用")
    # 清理代码可以在这里添加
    kill_pc_app(app)