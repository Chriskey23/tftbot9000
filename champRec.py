from os import pipe
from PIL import Image, ImageStat, ImageFilter, ImageShow
import numpy as np
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
    
    
    #print("DIANNA")
    #diannaStats = list(map(pipeLine, dianna))
    for i in championStatSet:
        print(i[0])
        for j in i[1]:
            print(j.var)
    
    #test = createAndApplyMask(olaf[0])
    #test.save("./testIMG.jpg", "JPEG")

def pipeLine(img):
    img = createAndApplyMask(img)
    stats = ImageStat.Stat(img)
    #checkFunc(stats)
    return stats

def createAndApplyMask(img):
    mask = img.filter(ImageFilter.FIND_EDGES)
    mask = mask.filter(ImageFilter.GaussianBlur(radius=2))
    maskArr = np.array(mask)
    maskArr = maskArr[:,:,2]<45
    imgArr = np.array(img)
    imgArr[maskArr] = 0
    img = Image.fromarray((imgArr))
    return img

def checkFunc(x):
    print("Root Mean Square =", end=" ")
    print(x.rms)
    print("Variance =", end=" ")
    print(x.var)
    print("Sum", end=" ")
    print(x.sum)

if __name__ == "__main__":
    main()