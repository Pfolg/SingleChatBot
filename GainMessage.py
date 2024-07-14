# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   GainMessage |User    Pfolg
# 2024/7/13   9:46
import time
import pyautogui
import pyperclip


# 获取消息
def GainMessage(messageX, messageY):
    pyautogui.moveTo(messageX, messageY, duration=1)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")
    pyautogui.click()  # 这里点一下是为了好看，有可能会出bug
    time.sleep(0.5)

    oldMessage = pyperclip.paste()
    # print(message, type(message))
    return oldMessage


# 分析消息
def analyseLog(QQname: str, x=932, y=495):
    message = GainMessage(x, y)
    listMessage = message.split("\n")

    cleaned_chat_logs = [log.rstrip('\r\t\n') for log in listMessage]
    log = []
    for item in cleaned_chat_logs:
        if item != '':
            log.append(item)
        else:
            pass
    newMsg = log[-1]
    if newMsg[:len(QQname) + 1] == f"@{QQname}":  # 如果有人@，就获取信息
        information = newMsg[len(QQname) + 1:]
        return information
    else:
        return 0


if __name__ == '__main__':
    pass
