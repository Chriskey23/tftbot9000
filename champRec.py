from PIL import Image, ImageStat, ImageFilter, ImageShow

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

    rakanStats = list(map(ImageStat.Stat, rakan))
    syndraStats= list(map(ImageStat.Stat, syndra))
    lucianStats = list(map(ImageStat.Stat, lucian))
    #test = ImageStat.Stat(rakan[0])
    print("RAKAN")
    for i in rakanStats:
        checkFunc(i)
    print("SYNDRA")
    for i in syndraStats:
        checkFunc(i)
    print("LUCIAN")
    for i in lucianStats:
        checkFunc(i)

    
    test = rakan[2].filter(ImageFilter.CONTOUR)
    test2 = ImageStat.Stat(test)
    print("TEST")
    checkFunc(test2)
    test.save("./testImg.jpg", "JPEG")
    #print(type(rakan[0]))
def checkFunc(x):
    print(x.rms)

if __name__ == "__main__":
    main()