import logging
import time

from pywinauto import keyboard

# from utils.utils_app import *

# 用例执行过程中记录日志
logger = logging.getLogger(__file__)

class HomePage(object):

    def __init__(self, app):
        self.app = app
    # 点击未登录
    def click_login(self,phoneNum,passWord):
        topwd = self.app.top_window()
        chwd = topwd.child_window(control_type="Document")
        btn = chwd.child_window(title="未登录", control_type="Group")
        btn.click_input()
        time.sleep(2)
        other_login=topwd.child_window(title="选择其它登录模式", control_type="Hyperlink")
        other_login.click_input()
        time.sleep(2)
        # topwd.dump_tree()
        # 输入手机号
        edit_phone = topwd.child_window(title="请输入手机号", control_type="Edit")
        edit_phone.set_focus()
        edit_phone.click_input()
        edit_phone.type_keys(phoneNum)
        # 输入密码
        edit_pass_word = topwd.child_window(title="请输入密码", control_type="Edit")
        edit_pass_word.set_focus()
        edit_pass_word.click_input()
        edit_pass_word.type_keys(passWord)
        # 点击同意隐私协议
        cb = topwd.child_window(title="同意", control_type="CheckBox")
        cb.click_input()
        # 点击登录
        btn = topwd.child_window(title="登录", control_type="Button")
        btn.click_input()
        time.sleep(5)



    # 查询歌曲
    def search_song(self,name):
        topwd = self.app.top_window()
        # 查找子元素
        chwd = topwd.child_window(control_type="Document")
        edit_search = chwd.child_window(title="search", control_type="Image")
        edit_search.click_input()
        edit_search.type_keys(name)
        # 等待一段时间，确保搜索结果正常刷新
        time.sleep(3)
        # # 回车确认
        keyboard.send_keys('{ENTER}')
        time.sleep(3)

    # 点击退出
    def click_logout(self,nick_name):
        topwd = self.app.top_window()
        chwd = topwd.child_window(control_type="Document")
        # chwd.dump_tree()
        nick_name_txt=chwd.child_window(title=nick_name, control_type="Group")
        nick_name_txt.click_input()
        time.sleep(2)
        # topwd.dump_tree()
        btn_logout = chwd.child_window(title="退出登录", control_type="Text")
        btn_logout.click_input()
        time.sleep(5)


