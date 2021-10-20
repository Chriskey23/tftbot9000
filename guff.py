import pyautogui
import pydirectinput
import time
import controller
import PIL
from matplotlib.pyplot import imshow
import numpy as np

shopCoordinates = [(689, 850), (828, 850), (970, 850), (1115, 850), (1250, 850)]
benchCoordinates = [(570, 690), (650, 690), (735, 690), (825, 690), (910, 690),
(990, 690), (1075, 690), (1165, 690), (1250, 690)]
itemBenchCoordinates = [(480, 680), (510, 655), (490, 635), (520, 615), (502, 594), 
(508, 565), (558, 614), (543, 590), (550, 565), (585, 590)]
boardCoordinats = [(690, 615), (780, 615), (870, 615), (960, 615), (1050, 615), 
(1140, 615), (1230, 615), (650, 560), (740, 560), (830, 560), (920, 560), (1010, 560),
(1100 ,560), (1190, 560), (700, 510), (790, 510), (875, 510), (960, 510), (1050, 510),
(1130, 510), (1220, 510), (675, 460), (750, 460), (840, 460), (920, 460), (1000, 460),
(1080, 460), (1160, 460)]
boardGrid = [[(690, 615), (780, 615), (870, 615), (960, 615), (1050, 615), 
(1140, 615), (1230, 615)],[(650, 560), (740, 560), (830, 560), (920, 560), (1010, 560),
(1100 ,560), (1190, 560)],[(700, 510), (790, 510), (875, 510), (960, 510), (1050, 510),
(1130, 510), (1220, 510)],[(675, 460), (750, 460), (840, 460), (920, 460), (1000, 460),
(1080, 460), (1160, 460)]]


def main():
    #learning how pyautogui works
    shopCoordinates = [(689, 850), (828, 850), (970, 850), (1115, 850), (1250, 850)]
    benchCoordinates = [(570, 690), (650, 690), (735, 690), (825, 690), (910, 690),
(990, 690), (1075, 690), (1165, 690), (1250, 690)]
    itemBenchCoordinates = [(480, 680), (510, 655), (490, 635), (520, 615), (502, 594), 
(508, 565), (558, 614), (543, 590), (550, 565), (585, 590)]
    boardCoordinates = [(690, 615), (780, 615), (870, 615), (960, 615), (1050, 615), 
(1140, 615), (1230, 615), (650, 560), (740, 560), (830, 560), (920, 560), (1010, 560),
(1100 ,560), (1190, 560), (700, 510), (790, 510), (875, 510), (960, 510), (1050, 510),
(1130, 510), (1220, 510), (675, 460), (750, 460), (840, 460), (920, 460), (1000, 460),
(1080, 460), (1160, 460)] 
    boardGrid = [[(690, 615), (780, 615), (870, 615), (960, 615), (1050, 615), 
(1140, 615), (1230, 615)],[(650, 560), (740, 560), (830, 560), (920, 560), (1010, 560),
(1100 ,560), (1190, 560)],[(700, 510), (790, 510), (875, 510), (960, 510), (1050, 510),
(1130, 510), (1220, 510)],[(675, 460), (750, 460), (840, 460), (920, 460), (1000, 460),
(1080, 460), (1160, 460)]]

    #Selects and gets game window to be primary!
    pydirectinput.moveTo(400, 400)
    pydirectinput.mouseDown(button="left")
    pydirectinput.mouseUp(button="left")
    
    winSizeList = [("./HoldTestImages/2045Test/",[20,45]) , ("./HoldTestImages/2545Test/",[25,45]), 
    ("./HoldTestImages/1540Test/",[15,40])]
    champion = ["dianna", benchCoordinates[0]]
    positionList = [boardGrid[0][2], boardGrid[2][1], boardGrid[3][5], boardGrid[1][6]]


    getTestData(champion, positionList, winSizeList)


def saveImgWindow(img, name, window):
    img = img.crop(window)
    img.save(name, "JPEG")

def getTestData(champion, positionList, winSizeList):
    count = 0

    #Take photo of initial baord position
    _,imNoHealthBars = takeScreenShots()
    for j in winSizeList:
        imgName = j[0]+champion[0]+str(count)+".jpg"
        window = (champion[1][0] - j[1][0], champion[1][1]-j[1][1], champion[1][0]+j[1][0], champion[1][1]+j[1][1])
        tmp = imNoHealthBars.crop(window)
        tmp.save(imgName, "JPEG")
    count += 1
    
    for i in positionList:
        controller.dragXPosToYPos(champion[1], i, None, None)
        champion[1]=i
        pydirectinput.moveTo(430, 600)
        _,imNoHealthBars = takeScreenShots()
        for j in winSizeList:
            imgName = j[0] + champion[0] + str(count) +".jpg"
            window = (champion[1][0] - j[1][0], champion[1][1]-j[1][1], champion[1][0]+j[1][0], champion[1][1]+j[1][1])
            tmp = imNoHealthBars.crop(window)
            tmp.save(imgName, "JPEG")
        count += 1
        

    
def takeScreenShots():
    imHealthBars = pyautogui.screenshot(region=(320,145,1280,763))
    pydirectinput.press('c')
    imNoHealthBars = pyautogui.screenshot()
    pydirectinput.press('c')
    return imHealthBars, imNoHealthBars

if __name__ == "__main__":
    main()