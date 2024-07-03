import pyautogui
import time

height = 1
pyautogui.write(str(height)+'\n')
for i in range(1, height + 1):
    line ="#"*i
    pyautogui.write(line + '\n')





