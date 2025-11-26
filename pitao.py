import pyautogui
pyautogui.moveTo(100, 100, duration=1)
pyautogui.click()
pyautogui.write('Hello, World!', interval=0.1)
pyautogui.press('enter')
pyautogui.moveTo(200, 200, duration=1)