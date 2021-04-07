import pyautogui, time, os, keyboard, sys
delay = input("How long to wait in between clicks?\n")
pyautogui.PAUSE = float(delay)
while True:
    if keyboard.is_pressed('s'):
        break
os.write(1, b"STARTING!\n")
while True:
    pyautogui.click()
    if keyboard.is_pressed('c'):
        os.write(1, b"STOPPEDf!\n")
        while True:
            if keyboard.is_pressed('s'):
                os.write(1, b"STARTING!\n")
                break
            elif keyboard.is_pressed('x'):
                os.write(1, b"KILLED!\n")
                sys.exit()
