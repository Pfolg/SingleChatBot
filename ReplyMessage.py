# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   ReplyMessage |User    Pfolg
# 2024/7/13   9:48
# 在聊天软件里回复消息
import time
import pyperclip
import pyautogui


def Reply(reply: str, sendX=865, sendY=735):
    pyautogui.moveTo(sendX, sendY, duration=1)
    time.sleep(1)
    pyautogui.click()

    pyperclip.copy(reply)
    time.sleep(0.5)

    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)

    pyautogui.hotkey("alt", "s")
    print("\n发送完毕!")


if __name__ == '__main__':
    pass
