import turtle
import csv
import tkinter

screen=turtle.Screen()
screen.setup(1200,646) #velicina ekrana postavljena na velicinu slike
screen.setworldcoordinates(-105,5,-20,45)  #podesen koordinatni sistem
screen.title("Hurricane Katrina")
#screen.bgpic("mapa1.gif")
canvas=screen.getcanvas()
#canvas.itemconfig(screen.bgpic)
mapa=tkinter.PhotoImage(file="mapa1.gif")
canvas.create_image(-855,-420,image=mapa)

hurricane=turtle.Turtle()
#screen.register_shape("icon.gif")
#hurricane.shape("icon.gif")

screen.register_shape("frame_0.gif")
screen.register_shape("frame_1.gif")
screen.register_shape("frame_2.gif")
screen.register_shape("frame_3.gif")
screen.register_shape("frame_4.gif")

hurricane.shape("frame_0.gif")

oblici=["frame_0.gif","frame_1.gif","frame_2.gif","frame_3.gif","frame_4.gif"]
j=0

def menjaj_oblik():
    global j
    if (j>4):
        j=j//4
    hurricane.shape(oblici[j])
    j=j+1


latitude=[]
longitude=[]
speed=[]

def ucitaj_csv(fajl):
    with open(fajl,"r") as csvfile:
        reader=csv.reader(csvfile,delimiter='\t')
        next(reader) #preskace se header
        for row in reader:
            latitude.append(row[2])
            longitude.append(row[3])
            speed.append(row[4])


ucitaj_csv("katrina.csv")
#print(longitude)

n=len(latitude)

hurricane.hideturtle()
hurricane.penup()
xstart=float(longitude[0])
ystart=float(latitude[0])
#print(xstart,ystart)
hurricane.setx(xstart)
hurricane.sety(ystart)
brzina=float(speed[0])
#hurricane.speed(brzina)

hurricane.showturtle()
hurricane.pendown()
hurricane.color("red")
hurricane.pensize(3)
for i in range(1,n):
    menjaj_oblik()
    x=float(longitude[i])
    y=float(latitude[i])
    brzina=float(speed[i])
    hurricane.setx(x)
    hurricane.sety(y)
    #hurricane.speed(brzina)



screen.mainloop()
