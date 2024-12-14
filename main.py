import time
import win32api, win32con
import keyboard
import pyautogui
import numpy as np
from PIL import ImageGrab
import cv2

rgb = 0 #0 for red, 1 for green, 2 for blue
num_tiles = 4


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



def get_height(region, tolerance=10):
    screen = capture_screen(region)

    # Define the RGB range for black tiles
    lower_bound = np.array([0, 0, 0])  # Pure black
    upper_bound = np.array([tolerance, tolerance, tolerance])  # Close to black

    # Scan y-coordinates row by row
    for y in range(region[1], region[3]):  # Loop through y range
        row = screen[y - region[1], :, :]  # Get the current row (subtract region start y)
        mask = cv2.inRange(row, lower_bound, upper_bound)  # Create a mask for the row
        if np.any(mask):  # If any black pixels are found in the row
            return y  # Return the y-coordinate of the first black tile

    return -1  # Return -1 if no black tiles are found


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
    screen_width, screen_height = pyautogui.size()
    columns = get_column_positions(num_tiles, screen_width)
    heightRegion = (0, 300, screen_width, 600)

    tileHeight = get_height(heightRegion)

    if tileHeight == -1:
        print("No black tiles found in region.")
        return

    # print the region where black tiles were found
    print(f"Tile height detected at: {tileHeight}")

    region = (0, tileHeight - 50, screen_width, tileHeight + 50)  # Screen capture region around the detected height

    print("Piano AI is running! Press 'q' to stop.")

    while not keyboard.is_pressed('q'):  # Stop the AI if 'q' is pressed
        # Capture a region of the screen where keys are expected to appear
        screen = capture_screen(region)

        # Loop through each column, check for tiles, and click if found
        for x in columns:
            tile_found = color_checker(x, tileHeight, rgb_channel=rgb)
            if tile_found:
                click(x, tileHeight)
        time.sleep(0.001)  # Add a small delay to prevent excessive CPU usage

    print("Piano AI stopped!")




