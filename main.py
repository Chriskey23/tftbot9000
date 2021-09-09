def main():
    #Start Game

    #Accept Que

    #Get game window & Wait for loading screen to end

    #Check initial settings are propper.


    #Game AI Loop
    gameIsRunning = True
    while(gameIsRunning):
        gameState = getCurrentGameState()

        #If game ends or something goes wrong, return false! 
        gameIsRunning = makeNextDecision()
    
