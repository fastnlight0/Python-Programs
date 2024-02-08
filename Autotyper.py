
# importing time and threading
import os, sys, time, threading
# pynput.keyboard is used to watch events of
# keyboard for start and stop of auto-clicker
from pynput.keyboard import Listener, Key, Controller


def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning
            an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")


# four variables are created to
# control the auto-clicker
delay = 0.001
button = input("Text: ")
pressEnter = query_yes_no("Press enter after each click?")
start_stop_key = Key(Key.f4)
stop_key = Key(Key.f3)

# threading.Thread is used
# to control clicks


import sys



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
                keyboard.type(self.button)
                keyboard.press(Key.enter)
                if pressEnter:
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
