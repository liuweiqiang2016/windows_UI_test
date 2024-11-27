
import time

from pywinauto import Application

def start_pc_app( install_path):
    app = Application(backend='uia').start(install_path)
    time.sleep(15)
    return app


# 连接已启动应用
def connect_pc_app(appName):
    # 连接到已启动的应用上，使用title匹配比path更好，由于多进程的原因，使用path无法匹配获取窗口，见https://github.com/pywinauto/pywinauto/issues/553
    # 应用必须在前台，否则找不到元素
    app = Application(backend='uia').connect(title=appName)
    return app

# 关闭应用
def kill_pc_app(app):
    app.kill()
    time.sleep(2)


