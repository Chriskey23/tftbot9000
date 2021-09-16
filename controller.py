#Controller
#Functions to control the game

import pyautogui
import pydirectinput
'''
Letssay the game wants to move items from x to y
to use item x on slot y
drag(posX, posY)
We could just be given item and 
Should we just make it

I guess we could give all the controls even though
our bot wouldn't be using it all but maybe in the future?
But how deep should they be?
Should we just have it input by position or by a unit type?
I think just position should be fine and have the bot handle 
the whole thing?

!!!Resolution of game window + resolution of monitor/display
Will
'''

###!!!Resolution fo game window + resolution of montior/display
###Effect where things will be. Will implement hardcoded for now
#Potential solution is identifying common elements and getting
#the rest of the positions later.
'''
def initAndCheckProperSettings():
    #Checks that the game is in proper resolution
    #and that the coloring is correct
'''


def buyExp():
    pydirectinput.press('f')

def rerollShop():
    pydirectinput.press('d')

#Input everything to keep it funcitonal
#Should I update and return the states too?
def buyXPosition(pos,shopCoordinates, shopState, benchState, boardState, currentGold):
    pydirectinput.moveTo(pos)
    pydirectinput.dragTo(pos[0]+15, pos[1]+15, 0.12, button="left")




def dragXPosToYPos(xCord, yCord, boardState, benchState):
    pydirectinput.moveTo(xCord[0], xCord[1])
    pyautogui.dragTo(yCord[0], yCord[1],0.12,pyautogui.easeInQuad, button="left", )
    

def sellXPos(xCord, boardState, benchState, currentGold):
    pyautogui.moveTo(xCord[0], xCord[1])
    pydirectinput.press('e')

def toggleHealthBars():
    pydirectinput.press('c')


'''
def getGameState():
    #Going to assume healthbars are on, will add a check funciton in the future.
    imHealthBars = pyautogui.screenshot(region=())
    pyautogui.press('c')
    imNoHealthBars = pyautogui.screenshot(region=())
    pyautogui.press('c')

    #Will need to check things like carosel, armour, stage

    boardChampions,benchChampions = getBoardState(imNoHealthBars)
    shopState = getBenchState(imHealthBars)

    #Returns itemBench as well as updating items for all units with items
    itemBench, boardChampions = getItemState(itemBench, boardChampions, )

    playerState = getPlayerState()



    return (boardChampions,benchChampions,itemBench,shopState,playerState,gameStage)
'''
#We want to try and make it functional!
#Can I evn make the control funcitons funcitonal?
#I guess we could just have it carry out the operations
#Whether they complete or not.
#How costly is get gamestate going to be?
#If it refreshes after each action
#Then it could be expensive.
#What we can do is only update where required.
#So refreshing shop just checks that region.
#So we begin round with stage, then after movement
#We change, and then there is a verify if needed.