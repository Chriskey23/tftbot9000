import pyautogui
import time
#import controller


def main():
    #learning how pyautogui works
    shopCoordinates = [(689, 850), (828, 850), (970, 850), (1115, 850), (1250, 850)]
    benchCoordinates = [(570, 690), (650, 690), (735, 690), (825, 690), (910, 690),
(990, 690), (1075, 690), (1165, 690), (1250, 690)]
    itemBenchCoordinates = [(480, 680), (510, 655), (490, 635), (520, 615), (502, 594), 
(508, 565), (558, 614), (543, 590), (550, 565), (585, 590)]
    boardCoordinats = [(690, 615), (780, 615), (870, 615), (960, 615), (1050, 615), 
(1140, 615), (1230, 615), (650, 560), (740, 560), (830, 560), (920, 560), (1010, 560),
(1100 ,560), (1190, 569), (700, 510), (790, 510), (875, 510), (960, 510), (1050, 510),
(1130, 510), (1220, 510), (675, 460), (750, 460), (840, 460), (920, 460), (1000, 460),
(1080, 460), (1160, 460)]

'''
shopCoordinates = [(689, 850), (828, 850), (970, 850), (1115, 850), (1250, 850)]
benchCoordinates = [(570, 690), (650, 690), (735, 690), (825, 690), (910, 690),
(990, 690), (1075, 690), (1165, 690), (1250, 690)]
itemBenchCoordinates = [(480, 680), (510, 655), (490, 635), (520, 615), (502, 594), 
(508, 565), (558, 614), (543, 590), (550, 565), (585, 590)]
boardCoordinats = [(690, 615), (780, 615), (870, 615), (960, 615), (1050, 615), 
(1140, 615), (1230, 615), (650, 560), (740, 560), (830, 560), (920, 560), (1010, 560),
(1100 ,560), (1190, 569), (700, 510), (790, 510), (875, 510), (960, 510), (1050, 510),
(1130, 510), (1220, 510), (675, 460), (750, 460), (840, 460), (920, 460), (1000, 460),
(1080, 460), (1160, 460)]


    pyautogui.moveTo(400, 400)
    pyautogui.click()
    im1 = pyautogui.screenshot(region=(875, 386,400, 300))

    print(type(im1))
    im1.show()
    time.wait(20)
    
    screenWidth, screenHeight = pyautogui.size()
    print(str(screenWidth) + " " + str(screenHeight))

    #Testing moving and clicking
    print(pyautogui.position())
    pyautogui.moveTo(737, 685)
    pyautogui.click()

    pyautogui.moveTo(1080, 848)
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')
    
    pyautogui.moveTo(737, 685)
    pyautogui.click()
    pyautogui.dragTo(1242, 705,button='left', duration=1)
    pyautogui.dragTo(737, 685, button='left', duration=0.5)

    pyautogui.moveTo(1080, 848)
    pyautogui.drag(0,-100,button='left', duration=0.2)

    pyautogui.moveTo(1082, 322)
    pyautogui.click(button='right')

    pyautogui.moveTo(534,833)
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')

    pyautogui.click(534,833, clicks=2, button='left')
    pyautogui.moveTo(500,600)
    pyautogui.click(button="left")
    '''
    #737,685
    #1242 705


if __name__ == "__main__":
    main()