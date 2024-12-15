import time
import win32api, win32con
import keyboard
import pyautogui

rgb = 0 #0 for red, 1 for green, 2 for blue
screen_width, screen_height = pyautogui.size()
game_left_proportion = 0.35  # 35% from the left (adjust if needed)
game_right_proportion = 0.65# 65% from the left (adjust if needed)

# Calculate the exact boundaries of the playable area
game_left = int(screen_width * game_left_proportion)
game_right = int(screen_width * game_right_proportion)
game_width = game_right - game_left

# Calculate tile x-positions dynamically based on the gameplay width
tile_columns = 4  # Total number of columns in the game
tile_width = game_width / tile_columns  # Width of one column
tile_x_positions = [
    int(game_left + (tile_width * i) + (tile_width / 2)) for i in range(tile_columns)
]

# Calculate the y-position dynamically (using a fixed proportion for height)
tile_y_position = int(screen_height * 0.8)  # Adjust based on where tiles fall (e.g., 80% of height)

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
    """
        Main AI logic to detect tiles and click on them dynamically.
        """
    while not keyboard.is_pressed('q'):  # Run until 'q' is pressed
        for tile_x in tile_x_positions:
            # Check the color of the tile at this position
            if color_checker(tile_x, tile_y_position):
                click(tile_x, tile_y_position)
                break  # Break after clicking to prevent multiple clicks in one loop

        # Exit if 'q' is pressed
        if keyboard.is_pressed('q'):
            break
    # while not keyboard.is_pressed('q'):
    #     if color_checker(600, height):
    #         click(600, height)
    #     elif color_checker(760, height):
    #         click(760, height)
    #     elif color_checker(920, height):
    #         click(920, height)
    #     elif color_checker(1080, height):
    #         click(1080, height)
    #
    #     if keyboard.is_pressed('q') == True:
    #         break

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
