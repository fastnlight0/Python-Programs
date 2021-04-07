import pyautogui, os, keyboard, sys
response = input("Type what you want to spam\n")
count = input("How many times do you want to write this (leave empty for infinite)\n")
while True:
    if keyboard.is_pressed('s'):
        break
os.write(1, b"STARTING!\n")
pyautogui.PAUSE = 0.0
if count == "":
    while True:
        pyautogui.write(response)
        pyautogui.press('enter')
        if keyboard.is_pressed('c'):
            os.write(1, b"KILLED!\n")
            sys.exit()
else:
    for i in range(int(count)):
        pyautogui.write(response)
        pyautogui.press('enter')
        if keyboard.is_pressed('c'):
            os.write(1, b"KILLED!\n")
            sys.exit()
    os.write(1, b"DONE!\n")
    sys.exit()
