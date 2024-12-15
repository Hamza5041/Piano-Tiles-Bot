import time
import win32api, win32con
import keyboard
import pyautogui

height = 400
rgb = 0 #0 for red, 1 for green, 2 for blue

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def color_checker(x,y):
    # if pyautogui.pixel(x, y)[2] > 27 and pyautogui.pixel(x, y)[2] < 98 and pyautogui.pixel(x, y)[1] > 15 and pyautogui.pixel(x, y)[1] < 52 and pyautogui.pixel(x, y)[0] > 4 and pyautogui.pixel(x, y)[0] < 18:
    if pyautogui.pixel(x, y)[rgb] == 0:
        return True
    return False

def hold_left_click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    while color_checker (x,y):
        time.sleep(0.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def piano_ai():
    while not keyboard.is_pressed('q'):
        if color_checker(600, height):
            click(600, height)
        elif color_checker(760, height):
            click(760, height)
        elif color_checker(920, height):
            click(920, height)
        elif color_checker(1080, height):
            click(1080, height)

        if keyboard.is_pressed('q') == True:
            break

        # if color_checker(600, height):
        #     hold_left_click(600, height)
        # elif color_checker(760, height):
        #     hold_left_click(760, height)
        # elif color_checker(920, height):
        #     hold_left_click(920, height)
        # elif color_checker(1080, height):
        #     hold_left_click(1080, height)

keyboard.add_hotkey('a', piano_ai)
keyboard.add_hotkey('s', piano_ai)
keyboard.add_hotkey('d', piano_ai)
keyboard.add_hotkey('f', piano_ai)
keyboard.wait('q')
