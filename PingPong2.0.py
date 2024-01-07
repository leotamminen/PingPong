
# Ping pong peli - versio 2.0

# musta tausta valkoisilla ohjekteilla ja "pallo" on laatikko.
# Huom äänitiedoston "bounce.wav" kanssa saattaa olla ongelmia.
# Pitäisi olla samassa hakemistossa itse .py tiedoston kanssa.
# Toisena pallon vauhti kohdasta pallo

import turtle
import winsound

ikkuna = turtle.Screen()
ikkuna.title("PingPong2.0")
ikkuna.bgcolor("#000000")
ikkuna.setup(width=800, height=600)
ikkuna.tracer(0)

# Scoreboardi arvot alussa 0
maali_1 = 0
maali_2 = 0

# Maila 1 (vasen)
maila1 = turtle.Turtle()
maila1.speed(0)
maila1.shape("square")
maila1.color("#ffffff")
maila1.shapesize(stretch_wid=5, stretch_len=1)
maila1.penup()
maila1.goto(-350, 0)

# Maila 2 (oikea)
maila2 = turtle.Turtle()
maila2.speed(0)
maila2.shape("square")
maila2.color("#ffffff")
maila2.shapesize(stretch_wid=5, stretch_len=1)
maila2.penup()
maila2.goto(350, 0)

# Pallo
pallo = turtle.Turtle()
pallo.speed(0)
pallo.shape("square")
pallo.shapesize(stretch_wid=2, stretch_len=2)
pallo.color("#ffffff")
pallo.penup()
pallo.goto(0, 0)
pallo.dx = 0.1        # <-- pallon vauhti
pallo.dy = 0.1        # <-- pallon vauhti

# Pen (vakio scorelle)
pen = turtle.Turtle()
pen.speed(0)
pen.color("#20C20E") # Scoreboardin väri
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Pelaaja 1: 0   Pelaaja 2: 0", align="center", font=("Courier", 24, "normal"))

# FUNKTIO määrittely:
 
def maila1_ylos():      # HUOM nämä kaikki on def komennon alla:
    y = maila1.ycor()   # Luodaan muuttuja y, joka kuvaa 
    y += 20             # maila1 y koord. lisätään 20 pixelillä. +=
    maila1.sety(y)      # maila1 y koord. asetetaan uuteen arvoon

def maila1_alas():      # (Tarkalleen sama homma, mutta alaspäin)
    y = maila1.ycor()
    y -= 20             # -= vähentää
    maila1.sety(y)

def maila2_ylos():
    y = maila2.ycor()
    y += 20
    maila2.sety(y)

def maila2_alas():
    y = maila2.ycor()
    y -= 20
    maila2.sety(y)

# Näppäin bindit

ikkuna.listen()                     # Ohjelma "kuuntelee" "näppäinsyötettä"
ikkuna.onkeypress(maila1_ylos, "w") # ja kun painetaan w niin suoritetaan
ikkuna.onkeypress(maila1_alas, "s") # ja alaspäin s

ikkuna.onkeypress(maila2_ylos, "Up")
ikkuna.onkeypress(maila2_alas, "Down")


# Main peli luuppi
while True:
    ikkuna.update()

    # Pallon liikkuminen 
    pallo.setx(pallo.xcor() + pallo.dx)
    pallo.sety(pallo.ycor() + pallo.dy)

    # Kun pallo osuu rajoihin (Border checking)
    if pallo.ycor() > 280:
        pallo.sety(280)    # Yläraja
        pallo.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if pallo.ycor() < -280:
        pallo.sety(-280)     # Alaraja
        pallo.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    if pallo.xcor() > 375:
        pallo.goto(0, 0)     # Oikea raja
        pallo.dx *= -1
        maali_1 += 1
        pen.clear()
        pen.write("Pelaaja 1: {}   Pelaaja 2: {}".format(maali_1, maali_2), align="center", font=("Courier", 24, "normal"))


    if pallo.xcor() < -375:
        pallo.goto(0, 0)     # Vasen raja
        pallo.dx *= -1
        maali_2 += 1
        pen.clear()
        pen.write("Pelaaja 1: {}   Pelaaja 2: {}".format(maali_1, maali_2), align="center", font=("Courier", 24, "normal"))


    # Pallo osuu mailaan
    # Maila 2 eli oikea
    if (pallo.xcor() > 320 and pallo.xcor() < 330) and (pallo.ycor() < maila2.ycor() + 60 and pallo.ycor() > maila2.ycor() - 60):
        pallo.setx(320)
        pallo.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Maila 1 eli vasen
    if (pallo.xcor() < -320 and pallo.xcor() > -330) and (pallo.ycor() < maila1.ycor() + 60 and pallo.ycor() > maila1.ycor() - 60):
        pallo.setx(-320)
        pallo.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)