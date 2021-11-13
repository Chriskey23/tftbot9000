#Controller
#Functions to control the game

import pyautogui
import pydirectinput
import cv2 as cv
import os

'''
def initAndCheckProperSettings():
    #Checks that the game is in proper resolution
    #and that the coloring is correct
'''

def buyExp():
    pydirectinput.press('f')
    #Update exp and level

def rerollShop():
    pydirectinput.press('d')
    #Get shop info

#Input everything to keep it funcitonal
#Should I update and return the states too?
def buyXPosition(pos, gameState):
    #check that we can afford it, and then update bench as well.
    #Update shop position
    pydirectinput.moveTo(pos)
    pydirectinput.dragTo(pos[0]+15, pos[1]+15, 0.12, button="left")

    #Confirm that this occured?
    #IE Screenshot and identify champ?

def pickXArmoryPosition(pos, gameState):
    pydirectinput.moveTo(pos)
    pydirectinput.dragTo(pos[0]+15, pos[1]+15, 0.12, button="left")
    #Update Bench



def dragXPosToYPos(xCord, yCord, boardState, benchState):
    pydirectinput.moveTo(xCord[0], xCord[1])
    pyautogui.dragTo(yCord[0], yCord[1],0.12 ,button="left")#,pyautogui.easeInQuad, button="left", )
    
def sellXPos(xCord, boardState, benchState, currentGold):
    pyautogui.moveTo(xCord[0], xCord[1])
    pydirectinput.press('e')

def toggleHealthBars():
    pydirectinput.press('c')


class champObject():
    def __init__(self, name, items, starpower):
        self.name = name
        self.items = items
        self.starpower = starpower


class gameState():
    def __init__(self):
        self.board = ([None]*7)*4
        self.bench = [None] * 9
        self.hp = 100
        #self.opponentHp
        self.gold = 0
        self.itemBench = [None]*10
        self.stage = (0,0)
        self.level = 1
        self.stateOfStage = "carosel"
        self.setupFlag
        self.playerPosition 
    

