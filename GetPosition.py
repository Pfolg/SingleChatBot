# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   GetPosition |User    Pfolg
# 2024/7/14   20:54
import time

import pyautogui

"""
一个用来获取屏幕某个位置坐标的程序
"""
time.sleep(5)  # 5秒后获取，可更改
location = pyautogui.position()
print(*location)
