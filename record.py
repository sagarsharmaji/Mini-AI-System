from tkinter import *
from tkinter import messagebox
import sounddevice as sound
from scipy.io.wavfile import write
import time
import ctrl
import S_to_T

root = Tk()
root.geometry("700x700+300+70")
root.resizable(False,False)
root.title("SOUND/MUSIC INPUT WINDOW")

def Record():
    freq = 44100
    dur = int(duration.get())
    recording = sound.rec(dur*freq,samplerate=freq,channels=2)

    try:
        temp = int(duration.get())
    except:
        print("Please Enter the Right Value!")

    while temp>0:
        root.update()
        time.sleep(1)
        temp-=1

        if(temp==0):
            messagebox.showinfo("Time Countdown","Time's UP")
        Label(text=f"{str(temp)}",font="TrebuchetMS 20",width=5,fg="black",background="white").place(x=307,y=600)

    sound.wait()
    write("rec.wav",freq,recording)

photo = PhotoImage(file="mic.png")
myimage = Label(image=photo)
myimage.pack(padx=4,pady=7)

#name
Label(text="SOUND RECORDER",font="TrebuchetMS 30 bold",fg="black").pack(pady=20)

#entry_box
duration = StringVar()
entry = Entry(root,textvariable=duration,font="TrebuchetMS 20",width=10).pack(pady=10)
Label(text="Enter Time in Seconds",font="TrebuchetMS 10",fg="black").pack()

#button
record = Button(root,font="TrebuchetMS 15",text="Record",bg="#111111",fg="white",border=0,command=Record).pack(pady=30)
play = Button(root,font="TrebuchetMS 15",text="Activate AI",bg="#111111",fg="white",border=0,command=S_to_T.Play).place(x=25, y=100)
volume_ctrl = Button(root,font="TrebuchetMS 15",text="Volume",bg="#111111",fg="white",border=0,command=ctrl.Ctrl).place(x=580, y=100)
#play = Button(root,font="TrebuchetMS 15",text="Play Recorded Audio",bg="#111111",fg="white",border=0,command=Play('rec.mp3')).pack(side=TOP,pady=30)
root.mainloop()