import time
import win32api, win32con
import keyboard
import pyautogui

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def color_checker(x,y):
    # if pyautogui.pixel(x, y)[2] > 27 and pyautogui.pixel(x, y)[2] < 98 and pyautogui.pixel(x, y)[1] > 15 and pyautogui.pixel(x, y)[1] < 52 and pyautogui.pixel(x, y)[0] > 4 and pyautogui.pixel(x, y)[0] < 18:
    if pyautogui.pixel(x, y)[2] == 0:
        return True
    return False

while keyboard.is_pressed('q') == False:
    if color_checker(600, 400):
        click(600, 400)
    elif color_checker(760, 400):
        click(760, 400)
    elif color_checker(920, 400):
        click(920, 400)
    elif color_checker(1080, 400):
        click(1080, 400)