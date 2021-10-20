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
        #Check for phase and handle transition
        screen = pyautogui.screenshot()
        if gameState.phase is "carousel":
            carouselCheck = ctr.tempateMatchList(screen.crop(), idSet.carouselPair, )
            if not(ctr.templateMatchList):
                #Empty list therefor not match therefor planning stage
                gameState = ctr.handleCarousel(gameState, idSet)
        elif gameState.phase is "planning":
            res = ctr.checkPixel(idSet.planWarnColor, idSet.planWarnPos, screen)
            if not(res) and gameState.planFlag:
                gameState.phase = "setup"
            elif res and not(gameState.planFlag):
                gameState.planFlag = True   
        elif gameState.phase is "setup":
            if ctr.checkPixel(idSet.fightColor, idSet.fightColPos, screen):
                gameState.phase = "fighting"
        elif gameState.phase is "fighting":
            if not(ctr.checkPixel(idSet.fightColor, idSet.fightColPos, screen)):
                gameState = ctr.fightTransition(gameState, screen)
        else:
            raise Exception("Error: Not one of possible phases!")

        #Give ai currentgame state and let it make decision
        gameState = ai.makeNextDecision(gameState)
