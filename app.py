import os
from flask import Flask, render_template
import pyautogui
import threading

app = Flask(__name__)

# Set the interval (in seconds) at which to move the mouse cursor
interval_seconds = 5  # Change this as needed

# Flag to indicate whether to keep the screen awake
keep_screen_awake = False

def keep_awake():
    global keep_screen_awake
    while keep_screen_awake:
        pyautogui.moveRel(1, 1)
        pyautogui.moveRel(-1, -1)
        pyautogui.sleep(interval_seconds)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    global keep_screen_awake
    if not keep_screen_awake:
        keep_screen_awake = True
        threading.Thread(target=keep_awake).start()
    return "Screen awake mode is enabled."

@app.route('/stop')
def stop():
    global keep_screen_awake
    keep_screen_awake = False
    return "Screen awake mode is disabled."

if __name__ == '__main__':
    app.run()
