import turtle
import csv
import tkinter

oblici=["frame_0.gif","frame_0.gif","frame_1.gif","frame_1.gif","frame_2.gif","frame_2.gif","frame_3.gif","frame_3.gif","frame_4.gif","frame_4.gif"]
j=0

def setup():
    screen=turtle.Screen()
    screen.setup(1200,646)
    screen.setworldcoordinates(-105,5,-20,45)
    screen.title("Hurricane Tracker")
    canvas=screen.getcanvas()
    mapa=tkinter.PhotoImage(file="mapa1.gif")
    canvas.create_image(-855,-420,image=mapa)

    hurricane=turtle.Turtle()

    screen.register_shape("frame_0.gif")
    screen.register_shape("frame_1.gif")
    screen.register_shape("frame_2.gif")
    screen.register_shape("frame_3.gif")
    screen.register_shape("frame_4.gif")

    hurricane.shape("frame_0.gif")
    return (screen,hurricane,mapa)

    

def menjaj_oblik(hurricane):
    global oblici
    global j
    if (j>8):
        j=j//8
    hurricane.shape(oblici[j])
    j=j+1


def ucitaj_csv(fajl):
    latitude=[]
    longitude=[]
    speed=[]
    with open(fajl,"r") as csvfile:
        reader=csv.reader(csvfile,delimiter='\t')
        next(reader)
        for row in reader:
            latitude.append(row[2])
            longitude.append(row[3])
            speed.append(row[4])
    return (latitude,longitude,speed)

def odredi_kategoriju(hurricane,brzina):
    if (brzina<=38):
        hurricane.pensize(1)
        hurricane.pencolor("#00ccff")
        hurricane.speed(1)
    elif (brzina<=73):
        hurricane.pensize(2)
        hurricane.pencolor("#1a8cff")
        hurricane.speed(2)
    elif (brzina<=95):
        hurricane.pensize(3)
        hurricane.pencolor("#ffff99")
        hurricane.speed(3)
    elif(brzina<=110):
        hurricane.pensize(4)
        hurricane.pencolor("#ffff4d")
        hurricane.speed(4)
    elif(brzina<=129):
        hurricane.pensize(5)
        hurricane.pencolor("#ff9933")
        hurricane.speed(5)
    elif(brzina<=156):
        hurricane.pensize(6)
        hurricane.pencolor("#ff6600")
        hurricane.speed(6)
    else:
        hurricane.pensize(7)
        hurricane.pencolor("#ff471a")  
        hurricane.speed(7)


def crtaj(hurricane,latitude,longitude,speed):
    n=len(latitude)
    hurricane.hideturtle()
    hurricane.penup()
    xstart=float(longitude[0])
    ystart=float(latitude[0])
    hurricane.setx(xstart)
    hurricane.sety(ystart)
    brzina=int(speed[0])
    odredi_kategoriju(hurricane,brzina)
    hurricane.showturtle()
    hurricane.pendown()
    for i in range(1,n):
        menjaj_oblik(hurricane)
        x=float(longitude[i])
        y=float(latitude[i])
        brzina=float(speed[i])
        odredi_kategoriju(hurricane,brzina)
        hurricane.setx(x)
        hurricane.sety(y)


def obradi_uragan(imefajla):
    (screen,hurricane,mapa)=setup()
    (latitude,longitude,speed)=ucitaj_csv(imefajla)
    crtaj(hurricane,latitude,longitude,speed)
    screen.mainloop()


if __name__=="__main__":
    broj=int(input("Godina 2005. je imala najaktivniju sezonu uragana ikada zabeleženu u Atlantskom okeanu. Od 27 oluja, rekordnih 15 je dobilo status uragana, a čak njih 4 je dostiglo kategoriju 5, što je najviši rang na skali.\nOluje su izazvale skoro 4000 smrtnih ishoda i materijalnu štetu od 171 milijardi dolara.\nOvde su date animacije za 5 najjačih uragana te godine.\nOdaberite uragan:\nDennis - 1\nEmily - 2\nKatrina - 3\nRita - 4\nWilma - 5\n"))
    if (broj==1):
        obradi_uragan("dennis.csv")
    elif (broj==2):
        obradi_uragan("emily.csv")
    elif (broj==3):
        obradi_uragan("katrina.csv")
    elif (broj==4):
        obradi_uragan("rita.csv")
    elif (broj==5):
        obradi_uragan("wilma.csv")
    else:
        print("Greska.\n")



