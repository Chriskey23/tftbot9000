import controller as ctr
import ai

import pyautogui

def main():
    #Start Game

    #Accept Que

    #Get game window & Wait for loading screen to end

    #Check initial settings are propper.

    #Object Setup
    gameState = ctr.contrgameStateObj()
    idSet = ctr.idenfityCollection()

    gameIsRunning = False
    #Game loop
    while(gameIsRunning):
        #Grab screen
        screen = pyautogui.screenshot()
        #Screenstate funciton identifies the objects on the screen
        screenState = getScreenState()
        #Ai funciton handles the options
        gameIsRunning = aiChoice(screenState)

