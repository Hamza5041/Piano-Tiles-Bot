import random
import time
import win32api, win32con
import keyboard
import pyautogui
import math

rgb = 0 #0 for red, 1 for green, 2 for blue
screen_width, screen_height = pyautogui.size()
game_left_proportion = 0.35    # 35% from the left (adjust if needed)
game_right_proportion = 0.65 # 65% from the left (adjust if needed)
mouse_displacement = 50  # Displacement from the center of the tile to click

# Calculate the exact boundaries of the playable area
game_left = (screen_width * game_left_proportion)//1
game_right = (screen_width * game_right_proportion)//1
game_width = game_right - game_left

# Calculate tile x-positions dynamically based on the gameplay width
tile_columns = 4  # Total number of columns in the game
tile_width = game_width / tile_columns  # Width of one column
array_of_xPosition = [
    int(game_left + (tile_width * i) + (tile_width / 2)) for i in range(tile_columns)
]

# Calculate the y-position dynamically (using a fixed proportion for height)
detection_y_coord = int(screen_height * 0.47)  # Adjust based on where tiles fall (e.g., 80% of height)


def move_mouse(x, y):
    x = random.randint(x - mouse_displacement, x + mouse_displacement)
    y = random.randint(y, y + mouse_displacement) #doing subtraction place the mouse too far up
    currentX, currentY = win32api.GetCursorPos()

    #cal distance square root((x2-x1)^2 + (y2-y1)^2)
    distance = ((x - currentX)**2 + (y - currentY)**2)**0.5
    # number of times the mouse will move which is steps
    steps = min(max(int(distance / 10), 60), 120)
    # Calculate the time for the entire movement
    sleep_time = random.uniform(0.005, 0.015) / steps
    
    for i in range(1, steps + 1):
        # Use easing function for more natural movement
        progress = i / steps
        naturalify = math.sin(progress * math.pi / 2) #adding a sin function to make it more natural, slows down towards the end
        
        next_x = int(currentX + (x - currentX) * naturalify)
        next_y = int(currentY + (y - currentY) * naturalify)
        
        win32api.SetCursorPos((next_x, next_y))
        time.sleep(sleep_time)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)



def color_checker(x,y):
    # if pyautogui.pixel(x, y)[2] > 27 and pyautogui.pixel(x, y)[2] < 98 and pyautogui.pixel(x, y)[1] > 15 and pyautogui.pixel(x, y)[1] < 52 and pyautogui.pixel(x, y)[0] > 4 and pyautogui.pixel(x, y)[0] < 18:
    if pyautogui.pixel(x, y)[rgb] == 0:
        return True
    return False


def hold_left_click(x, y):
    move_mouse(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    while color_checker (x,y):
        time.sleep(0.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)



def piano_ai():
    while not keyboard.is_pressed('q'):  # Run until 'q' is pressed
        for detection_x_coord in array_of_xPosition:
            # Check the color of the tile at this position
            if color_checker(detection_x_coord, detection_y_coord):
                hold_left_click(detection_x_coord, detection_y_coord)
                # time.sleep(random.uniform(0.001, 0.003))
                break  # Break after clicking to prevent multiple clicks in one loop

        # if random.random() < 0.02:
        #     time.sleep(0.005)
        # doubt check Exit if 'q' is pressed
        if keyboard.is_pressed('q'):
            break


#run the code, press any of a,s,d,f to start and q to stop
keyboard.add_hotkey('a', piano_ai)
keyboard.add_hotkey('s', piano_ai)
keyboard.add_hotkey('d', piano_ai)
keyboard.add_hotkey('f', piano_ai)
keyboard.wait('q')
