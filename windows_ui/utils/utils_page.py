from pywinauto import mouse


# 获取页面文本
def get_pc_page_txt(app):
    topwd = app.top_window()
    chwd = topwd.child_window(control_type="Document")
    # 获取页面中所有文本
    text = chwd.window_text()
    return text

# 以控件中心为起点，滚动鼠标
# distance指定鼠标滚轮滑动，正数往上，负数往下
def mouse_scroll(control, distance):
    rect = control.rectangle()
    cx = int((rect.left + rect.right) / 2)
    cy = int((rect.top + rect.bottom) / 2)
    mouse.scroll(coords=(cx, cy), wheel_dist=distance)

