import pyautogui


def main():
    #learning how pyautogui works
    screenWidth, screenHeight = pyautogui.size()
    print(str(screenWidth) + " " + str(screenHeight))

    #Testing moving and clicking
    print(pyautogui.position())
    
    pyautogui.moveTo(737, 685)
    pyautogui.click()
    pyautogui.dragTo(1242, 705,button='left', duration=1)
    pyautogui.dragTo(737, 685, button='left', duration=0.5)

    pyautogui.moveTo(1080, 848)
    pyautogui.drag(0,-100,button='left', duration=0.2)

    pyautogui.moveTo(1082, 322)
    pyautogui.click(button='right')
    #737,685
    #1242 705


if __name__ == "__main__":
    main()