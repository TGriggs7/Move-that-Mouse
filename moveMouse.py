import win32api
from win32api import GetSystemMetrics

import time
import math
import numpy as np

state_left = win32api.GetKeyState(0x01) # left click

SCREEN_WIDTH = GetSystemMetrics(0)
SCREEN_HEIGHT = GetSystemMetrics(1)

# left click stops the mouse movement
while(win32api.GetKeyState(0x01) == state_left):

    new_time = time.clock()

    # Lissajous Curve
    x = int(SCREEN_WIDTH/2 + 300 * math.sin(5 * new_time))
    y = int(SCREEN_HEIGHT/2 + 200 * math.cos(6 * new_time))
    
    win32api.SetCursorPos((x, y))

    time.sleep(.01)

    
    
    
    
    
    