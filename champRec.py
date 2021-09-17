from os import pipe
from PIL import Image, ImageStat, ImageFilter, ImageShow
import numpy as np
def main():
    rakan = [Image.open("./HoldTestImages/Rakan1Star1.jpg"), 
    Image.open("./HoldTestImages/Rakan1Star2.jpg"), 
    Image.open("./HoldTestImages/Rakan1Star3.jpg")] 
    lucian = [Image.open("./HoldTestImages/Lucian1Star1.jpg"), 
    Image.open("./HoldTestImages/Lucian1Star2.jpg")]
    olaf = [Image.open("./HoldTestImages/Olaf1Star1.jpg"),
     Image.open("./HoldTestImages/Olaf1Star2.jpg")]
    syndra = [Image.open("./HoldTestImages/Syndra1Star1.jpg"),
    Image.open("./HoldTestImages/Syndra1Star2.jpg"),
    Image.open("./HoldTestImages/Syndra1Star3.jpg")]
    draven = [Image.open("./HoldTestImages/Draven1Star1.jpg"),
    Image.open("./HoldTestImages/Draven1Star2.jpg")]
    missfortune = [Image.open("./HoldTestImages/MissFortune1Star1.jpg"),
    Image.open("./HoldTestImages/MissFortune1Star2.jpg")]
    dianna = [Image.open("./HoldTestImages/Dianna1Star1.jpg"),
    Image.open("./HoldTestImages/Dianna1Star2.jpg"),
    Image.open("./HoldTestImages/Dianna1Star3.jpg")]

    print("RAKAN")
    rakanStats = list(map(pipeLine, rakan))
    print("SYNDRA")
    syndraStats= list(map(pipeLine, syndra))
    print("LUCIAN")
    lucianStats = list(map(pipeLine, lucian))
    print("DRAVEN")
    dravenStats = list(map(pipeLine, draven))
    print("MISSFORTUNE")
    missfortuneStats = list(map(pipeLine, missfortune))
    test = createAndApplyMask(olaf[0])
    test.save("./testIMG.jpg", "JPEG")

def pipeLine(img):
    img = createAndApplyMask(img)
    stats = ImageStat.Stat(img)
    checkFunc(stats)
    return img

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
    print(x.rms)

if __name__ == "__main__":
    main()