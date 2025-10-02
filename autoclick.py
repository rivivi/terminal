import pyautogui
import time
import keyboard  # install with: pip install keyboard

print("AutoClicker will start in 3 seconds. Press 'q' to quit.")
time.sleep(3)

# Interval between clicks (seconds)
delay = 0.1  

while True:
    if keyboard.is_pressed('q'):  # Stop if 'q' is pressed
        print("AutoClicker stopped.")
        break
    pyautogui.click()
    time.sleep(delay)
