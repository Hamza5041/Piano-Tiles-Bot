import time
import win32api, win32con
import keyboard
import pyautogui
import numpy as np
from PIL import ImageGrab
import cv2

rgb = 0 #0 for red, 1 for green, 2 for blue
num_tiles = 4
screen_width, screen_height = pyautogui.size()

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


def detect_black_tiles(screen, tolerance=10):
    """
           Detects the tiles based on their colors in a portion of the screen.
           Returns the positions (`x`, `y`) of the black tiles.
    """
    # initialize the upper and lower bounds
    lowerBound = np.array([0,0,0])
    upperBound = np.array([tolerance, tolerance, tolerance]) # upper bound will be the range which it will accept tile colors. So within a value of 10 from 0(pure black)
    mask = cv2.inRange(screen, lowerBound, upperBound) # mask for color range
    positions = np.where(mask == 255) # get positions of black tiles
    # zip the x and y position of the tile and return
    return list(zip(positions[1], positions[0]))


def get_column_positions(num_tiles, screen_width):
    """
    Dynamically calculates the position of the tiles on x0-axis in case screen resolution changes.
    """
    spacing = screen_width // (num_tiles + 1)
    positions = []
    for i in range (1, num_tiles + 1):
        positions.append(i * spacing)
    return positions


def click(x, y):
    pyautogui.click(x, y)



def color_checker(x,y, rgb_channel=0, threshold=10):
    pixelColor = pyautogui.pixel(x, y)[rgb_channel] # get the specific value
    # return true, if the color is within the threshold (10)
    return pixelColor <= threshold



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
