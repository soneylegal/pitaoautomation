import pyautogui
import time

pyautogui.FAILSAFE = True

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(2)

pyautogui.write('Clima hoje na minha cidade', interval=0.1)

pyautogui.press('enter')
time.sleep(1)
img = pyautogui.screenshot()
img.save('clima.png')