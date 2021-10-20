import pyautogui
import pydirectinput
import controller
import time
from PIL import Image, ImageChops

def main():
    while(True):
        time.sleep(2)
        print(pydirectinput.position())
    

if __name__ == "__main__":
    main()