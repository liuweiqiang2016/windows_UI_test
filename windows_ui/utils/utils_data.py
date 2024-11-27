import os
import pandas as pd
from windows_ui.model.case_model import CaseModel

# 获取项目根目录
def get_project_path():
    current_path = os.getcwd()
    while True:
        if 'pytest.ini' in os.listdir(current_path):
            return current_path
        current_path = os.path.dirname(current_path)

'''===============================================PC端专用方法=================================================='''
# 读取excel数据
def read_pc_data_excel():
    # 获取当前文件目录的父目录 ！注意是父目录路径
    # print(os.path.abspath('..'))
    # excel文件路径
    fpath = os.path.join(get_project_path(), 'windows_ui', 'data', 'windows_test_case.xlsx')
    # 读取业务数据
    user_data = pd.read_excel(fpath, sheet_name='业务数据')
    user_dict = {}
    # 循环读取列字段名和字段值，并将这两列将转换为方便使用的dict
    n = 0
    while n < user_data.shape[0]:
        key = user_data['字段名'][n]
        value = user_data['字段值'][n]
        user_dict[key] = value
        n = (n + 1)
    # print(user_dict)
    # 读取登录用例
    login_list = read_pc_sheet_data(fpath, '登录')
    # 读取歌曲用例
    song_list = read_pc_sheet_data(fpath, '歌曲')
    return user_dict, login_list, song_list

# 读取 sheet数据
def read_pc_sheet_data(fpath, sheet_name):
    sheet_data = pd.read_excel(fpath, sheet_name=sheet_name)
    list_data = []
    # 循环读取列表，并将这些列表转换为用例对象list
    n = 0
    while n < sheet_data.shape[0]:
        title = sheet_data['测试用例'][n]
        des = sheet_data['测试步骤'][n]
        case_id = sheet_data['用例编号'][n]
        key_word = sheet_data['校验文本'][n]
        list_data.append(CaseModel(title, des, case_id, key_word))
        n = (n + 1)
    return list_data



if __name__ == '__main__':
    pass
