import pyautogui
import keyboard

import win32api ,win32con
import time

def click (x,y):
    #API DO WINDOS É MAIS RAPIDA
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# 0, 30
# 1358, 694

# 255, 85, 85

#olha a posição do mause é a cor.

#while True:    
#   pyautogui.displayMousePosition()





while keyboard.is_pressed('c')==False:

  sc = pyautogui.screenshot(region=(0,30,1358,694))# tira o print
  width,height = sc.size #
  
  for x in range(0, width,10):
    for y in range(0,height,10):

        r,g,b = sc.getpixel((x,y))
        
        if r == 255 and g == 19 and b == 19:
            # pyautogui.click(44 + x,185 + y)
            click(0 + x,30 + y)
            time.sleep(0.09)


#sc.save('Exemplo.png')





