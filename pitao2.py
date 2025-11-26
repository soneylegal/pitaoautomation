import pyautogui
import time
import webbrowser

pyautogui.FAILSAFE = True

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(2)  # Give user time to switch to the target window
webbrowser.open("https://www.wikipedia.org")
time.sleep(1)
pyautogui.typewrite('Python programming language', interval=0.1)
pyautogui.press('enter')
time.sleep(1)  # Wait for the page to load
img = pyautogui.screenshot()
img.save('wikipedia_python.png')