import pyautogui, time, os, keyboard, sys
count = input("How many times do you want to paste (leave empty for infinite)\n")
pyautogui.PAUSE = 0.0
while True:
    if keyboard.is_pressed('s'):
        break
os.write(1, b"STARTING!\n")
if count == "":
    while True:
        # Windows users: replace 'command' with ctrl
        pyautogui.hotkey('command', 'v')
        pyautogui.press('enter')
else:
    for i in range(int(count)):
        # Windows users: replace 'command' with ctrl
        pyautogui.hotkey('command', 'v')
        pyautogui.press('enter')
    os.write(1, b"DONE!\n")
    sys.exit()
