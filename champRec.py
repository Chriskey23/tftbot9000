from os import pipe
from PIL import Image, ImageStat, ImageFilter, ImageShow
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib import index_tricks

def main():
    #Inital files
    championFileDirSets = [("rakan", ["./HoldTestImages/Rakan1Star1.jpg", "./HoldTestImages/Rakan1Star2.jpg", "./HoldTestImages/Rakan1Star3.jpg"]), 
    ("lucian", ["./HoldTestImages/Lucian1Star1.jpg", "./HoldTestImages/Lucian1Star2.jpg", "./HoldTestImages/Lucian1Star3.jpg"]),
    ("olaf", ["./HoldTestImages/Olaf1Star1.jpg", "./HoldTestImages/Olaf1Star2.jpg", "./HoldTestImages/Olaf1Star3.jpg"]), 
    ("syndra", ["./HoldTestImages/Syndra1Star1.jpg", "./HoldTestImages/Syndra1Star2.jpg", "./HoldTestImages/Syndra1Star3.jpg"]),
    ("draven", ["./HoldTestImages/Draven1Star1.jpg", "./HoldTestImages/Draven1Star2.jpg", "./HoldTestImages/Draven1Star3.jpg"]), 
    ("missfortune", ["./HoldTestImages/MissFortune1Star1.jpg", "./HoldTestImages/MissFortune1Star2.jpg", "./HoldTestImages/MissFortune1Star3.jpg"]), 
    ("dianna", ["./HoldTestImages/Dianna1Star1.jpg", "./HoldTestImages/Dianna1Star2.jpg", "./HoldTestImages/Dianna1Star3.jpg"])]
    
    testFileSet =  [("rakan", "./HoldTestImages/RakanTest1.jpg"), 
    ("lucian", "./HoldTestImages/LucianTest1.jpg"), 
    ("olaf", "./HoldTestImages/OlafTest1.jpg"), 
    ("missfortune", "./HoldTestImages/MissFortuneTest1.jpg"), 
    ("dianna", "./HoldTestImages/DiannaTest1.jpg"),
    ("dianna", "./HoldTestImages/DiannaTest2.jpg")]
    
    #Get images
    championImgSet = []
    for i in championFileDirSets:
        holdImgs = []
        for j in i[1]:
            holdImgs.append(Image.open(j))
        championImgSet.append( (i[0], holdImgs))
    testImgSet = []
    for i in testFileSet:
        testImgSet.append( (i[0], Image.open(i[1])))
    

    #Get Stats
    championStatSet = []
    for i in championImgSet:
        holdStats = []
        for j in i[1]:
            holdStats.append(pipeLine(j))
        championStatSet.append( (i[0], holdStats)) 
    testStatSet = []
    for i in testImgSet:
        testStatSet.append((i[0], pipeLine(i[1])))


    #Using our temp compare function and checking if we got right one    
    setOfMins = []
    for i in testStatSet:
        holdMin = None
        print("Test  Champion = " + i[0])
        for j in championStatSet:
            print("VS " + j[0] + " = ", end="")
            #hold = sum(compareFunction(i[1], j[1]))
            hold = compareFunction(i[1], j[1])
            print(hold)
            if holdMin == None:
                holdMin = (j[0],hold)
            elif holdMin[1] > hold:
                holdMin = (j[0],hold)
        #Store the results
        setOfMins.append( (i[0], holdMin[0], holdMin[1]))

    #Printing results
    for i in setOfMins:
        print(i) 

    '''
    for i in championStatSet:
        print(i[0])
        for j in i[1]:
            print(j.rms)
    '''
    #Testing and getting a binary mask!
    testImg  = championImgSet[0][1][0]

    #Couldn't figure out how to mkae black image with the numpy.zeroes 
    #So here is some absolutly amazing method of doing it and
    #in no way is it glued together crap, nope, definetly not 
    blackImg = np.array(testImg)
    tmp = blackImg[:,:,2] != 0
    blackImg[tmp] = 0
    blackImg = Image.fromarray(blackImg)
    
    imgMask = testCreateMask(testImg)#.convert("RGB")
    imgMask = imgMask.convert('L')

    #maskedResult = Image.composite(testImg,blackImg, mask=imgMask)
    maskedStats = ImageStat.Stat(testImg,mask=imgMask)
    normalImg = createAndApplyMask(testImg)
    normalStats = ImageStat.Stat(normalImg)
    print(maskedStats.mean)
    print(normalStats.mean)

    #print( list(a-b for (a,b) in zip(championStatSet[0][1][0].var,testStatSet[0][1].var)))

    #Lets create some plots to get a feel for the data.



def compareFunction(testStats, champSetStats):
    #[ stats1, stats2, stats3]
    #stats
    total = None
    total2 = None
    temp = [0,0,0]
    for i in champSetStats:
        a = i.rms
        b = testStats.rms
        temp[0] = (a[0]-b[0])**2
        temp[1] = (a[1]-b[1])**2
        temp[2] = (a[2]-b[2])**2
        if total == None:
            total = sum(temp)
        elif total > sum(temp):
            total2 = total
            total = sum(temp)
        elif total2 == None:
            total2 = sum(temp)
        elif total2 > sum(temp):
            total2 = sum(temp)
    total += total2
    return total
'''
def compareFunction(testStats, champSetStats):
    #[ stats1, stats2, stats3]
    #stats
    total = None
    temp = [0,0,0]
    for i in champSetStats:
        a = i.mean
        b = testStats.mean
        temp[0] += (a[0]-b[0])**2
        temp[1] += (a[1]-b[1])**2
        temp[2] += (a[2]-b[2])**2
    
    temp[0] = temp[0]/3
    temp[1] = temp[1]/3
    temp[2] = temp[2]/3
    return sum(temp)
'''
def pipeLine(img):
    imgMask = createAndApplyMask(img)
    stats = ImageStat.Stat(img, mask=imgMask)
    #checkFunc(stats)
    return stats

def createAndApplyMask(img):
    mask = img.filter(ImageFilter.FIND_EDGES)
    mask = mask.filter(ImageFilter.GaussianBlur(radius=3))

    maskArr = np.array(mask)
    
    maskArr = maskArr[:,:,2]<35

    mask = np.zeros(shape=maskArr.shape)
    mask[np.invert(maskArr)] = 255

    mask = Image.fromarray(mask)
    mask = mask.convert('L')
    return mask
    


def testCreateMask(img):
    mask = img.filter(ImageFilter.FIND_EDGES)
    mask = mask.filter(ImageFilter.BoxBlur(radius=5))

    maskArr = np.array(mask)
    
    maskArr = maskArr[:,:,2]<35

    mask = np.zeros(shape=maskArr.shape)
    mask[np.invert(maskArr)] = 255

    mask = Image.fromarray(mask)

    return mask


def checkFunc(x):
    print("Root Mean Square =", end=" ")
    print(x.rms)
    print("Variance =", end=" ")
    print(x.var)
    print("Sum", end=" ")
    print(x.sum)

if __name__ == "__main__":
    main()

