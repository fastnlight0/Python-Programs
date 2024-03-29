# importing os, platform, time and threading
import os, platform, time, threading
# pynput.keyboard is used to watch events of
# keyboard for start and stop of auto-clicker
from pynput.keyboard import Listener, Key, Controller


# four variables are created to
# control the auto-clicker
delay = 0.03
button = 'v'
command = Key.ctrl
if platform.system() == "Darwin":
    # MacOS code
    command = Key.cmd
start_stop_key = Key(Key.f4)
stop_key = Key(Key.f3)

# threading.Thread is used
# to control clicks


class ClickMouse(threading.Thread):

    # delay and button is passed in class
    # to check execution of auto-clicker
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    # method to check and run loop until
    # it is true another loop will check
    # if it is set to true or not,
    # for mouse click it set to button
    # and delay.
    def run(self):
        keyboard = Controller()
        os.write(1, b"Program online!\n")
        while self.program_running:
            while self.running:
                with keyboard.pressed(command):
                    keyboard.press(self.button)
                    keyboard.release(self.button)
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                time.sleep(self.delay)
            time.sleep(0.1)


# instance of mouse controller is created
mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


# on_press method takes
# key as argument
def on_press(key):

    # start_stop_key will stop clicking
    # if running flag is set to true
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()

    # here exit method is called and when
    # key is pressed it terminates auto clicker
    elif key == stop_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
