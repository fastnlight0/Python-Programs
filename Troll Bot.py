import pyautogui, time, os
pyautogui.PAUSE = 0.0
Sherk = open("/Users/zanesinno/Documents/Troll/Spambot/Shrek.txt", 'r')
response = input("Hit enter to start\n")
if response == (""):
    os.write(1, b"STARTING IN 3\n")
    time.sleep(1)
    os.write(1, b"STARTING IN 2\n")
    time.sleep(1)
    os.write(1, b"STARTING IN 1\n")
    time.sleep(1)
    os.write(1, b"STARTING!\n")
    for word in Sherk:
       pyautogui.write(word)
       pyautogui.press('enter')
