# tftbot9000
TFTBot to play Teamfight Tactics  
Uses pyautogui to control TFT and play automatically  
Not working, just going to restart. Partially shelved while working on other stuff, will return.

Plan for next attempt:
Object detection + Image recognition, maybe yolo?
Then with all objects identified, feed it to some ai. 

For ai, needs to be something quick to adapt to patches.
Likely one part evaluating board state, and another part evaluating next decition.
So one part can learn how to play the game while other just learns what a strong board look likes.
Then we can feed in past results from top ranked players into strong board ai for quicker adaptation to the meta.
These are just napkin notes for now.
