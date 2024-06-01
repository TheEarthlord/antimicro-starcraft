from pynput import mouse
import time

def find_screen_dimensions():
    mouseController = mouse.Controller()
    original_coords = mouseController.position
    x = original_coords[0]
    y = original_coords[1]

    mouseController.move(1, 1)
    while x != mouseController.position[0] or y != mouseController.position[1]:
        x = mouseController.position[0]
        y = mouseController.position[1]
        mouseController.move(1, 1)
    final_coords = (mouseController.position[0] + 1, mouseController.position[1] + 1)
    mouseController.position = original_coords

    return final_coords


screen_setting = "stretchedscreen"
#screen_setting = "smallscreen"
if screen_setting == "stretchedscreen":
    #These stats may still be inaccurate.
    TOP_Y_RATIO = 0.78
    MID_Y_RATIO = 0.86
    BOT_Y_RATIO = 0.95
    LEFT_X_RATIO = 0.82
    CENT_X_RATIO = 0.89
    RIGHT_X_RATIO = 0.96
elif screen_setting == "smallscreen":
    TOP_Y_RATIO = 0.78
    MID_Y_RATIO = 0.86
    BOT_Y_RATIO = 0.95
    LEFT_X_RATIO = 0.73
    CENT_X_RATIO = 0.8
    RIGHT_X_RATIO = 0.84

mouseController = mouse.Controller()
#x_width, y_width = find_screen_dimensions()

# By experiment it appears that these are the
# dimensions inside pre-1.18 starcraft
x_width, y_width = 640, 480

current_pos = mouseController.position
mouseController.position = (x_width*CENT_X_RATIO, y_width*BOT_Y_RATIO)
time.sleep(0.001)
mouseController.press(mouse.Button.left)
mouseController.release(mouse.Button.left)
time.sleep(0.001)
mouseController.position = current_pos
