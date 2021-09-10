def main():
    #Start Game

    #Accept Que

    #Get game window & Wait for loading screen to end

    #Check initial settings are propper.


    #Game AI Loop
    gameIsRunning = True
    while(gameIsRunning):
        #We probably only make decision in planning stage
        #Check and set timer, then check till fighting is done
        #Timer interupts AI and then starts it again when planning starts
        gameState = getCurrentGameState()

        #If game ends or something goes wrong, return false! 
        gameIsRunning = makeNextDecision(gameState)
    
