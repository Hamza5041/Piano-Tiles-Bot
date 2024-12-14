import time
import win32api, win32con
import keyboard
import pyautogui
import numpy as np
from PIL import ImageGrab
import cv2

height = 400
rgb = 0 #0 for red, 1 for green, 2 for blue


def capture_screen(region = None):
    """
    Capture a screenshot of the entire screen or a specific region and return it as a NumPy array.

    This function utilizes the `ImageGrab` module to capture the screen and converts the captured
    image into a NumPy array for further processing.

    :param region: A tuple defining the bounding box of the region to capture (left, top, right, bottom).
                   If None, the entire screen will be captured.
    :type region: tuple | None
    :return: A NumPy array representing the captured image.
    :rtype: numpy.ndarray
    """
    screen = ImageGrab.grab(bbox=region)
    return np.array(screen)


def detect_black_tiles(screen, rgb, tolerance=10):
    """
           Detects the tiles based on their colors in a portion of the screen.
           Returns the positions (`x`, `y`) of the black tiles.
    """
    # initialize the upper and lower bounds
    lowerBound = np.array([rgb - tolerance, rgb - tolerance, rgb - tolerance])
    upperBound = np.array([rgb + tolerance, rgb + tolerance, rgb + tolerance])
    mask = cv2.inRange(screen, lowerBound, upperBound) # mask for color range
    positions = np.where(mask == 255) # get positions of black tiles
    # zip the x and y position of the tile and return
    return zip(positions[1], positions[0])



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
        # if color_checker(600, height):
        #     click(600, height)
        # elif color_checker(760, height):
        #     click(760, height)q
        # elif color_checker(920, height):
        #     click(920, height)
        # elif color_checker(1080, height):
        #     click(1080, height)

        # if keyboard.is_pressed('q') == True:
        #     break

        if color_checker(600, height):
            hold_left_click(600, height)
        elif color_checker(760, height):
            hold_left_click(760, height)
        elif color_checker(920, height):
            hold_left_click(920, height)
        elif color_checker(1080, height):
            hold_left_click(1080, height)

keyboard.add_hotkey('a', piano_ai)
keyboard.add_hotkey('s', piano_ai)
keyboard.add_hotkey('d', piano_ai)
keyboard.add_hotkey('f', piano_ai)
keyboard.wait('q')
