import turtle
import csv
import tkinter

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

oblici=["frame_0.gif","frame_0.gif","frame_1.gif","frame_1.gif","frame_2.gif","frame_2.gif","frame_3.gif","frame_3.gif","frame_4.gif","frame_4.gif"]
j=0

def menjaj_oblik():
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

def odredi_kategoriju(brzina):
    if (brzina<=38):
        hurricane.pensize(1)
        hurricane.pencolor("#00ccff")
        #speed?
    elif (brzina<=73):
        hurricane.pensize(2)
        hurricane.pencolor("#1a8cff")
    elif (brzina<=95):
        hurricane.pensize(3)
        hurricane.pencolor("#ffff99")
    elif(brzina<=110):
        hurricane.pensize(4)
        hurricane.pencolor("#ffff4d")
    elif(brzina<=129):
        hurricane.pensize(5)
        hurricane.pencolor("#ff9933")
    elif(brzina<=156):
        hurricane.pensize(6)
        hurricane.pencolor("#ff6600")
    else:
        hurricane.pensize(7)
        hurricane.pencolor("#ff471a")  


def crtaj(latitude,longitude,speed):
    n=len(latitude)
    hurricane.hideturtle()
    hurricane.penup()
    xstart=float(longitude[0])
    ystart=float(latitude[0])
    hurricane.setx(xstart)
    hurricane.sety(ystart)
    brzina=int(speed[0])
    odredi_kategoriju(brzina)
    hurricane.showturtle()
    hurricane.pendown()
    for i in range(1,n):
        menjaj_oblik()
        x=float(longitude[i])
        y=float(latitude[i])
        brzina=float(speed[i])
        odredi_kategoriju(brzina)
        hurricane.setx(x)
        hurricane.sety(y)


def obradi_uragan(imefajla):
    (latitude,longitude,speed)=ucitaj_csv(imefajla)
    crtaj(latitude,longitude,speed)

obradi_uragan("rita.csv")


screen.mainloop()
