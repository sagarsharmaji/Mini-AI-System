import tkinter as tk
from tkinter import *
import S_to_T
import ctrl

root = Tk()
root.geometry("700x650") 
root.resizable(False,False)
root.title("AI MainFrame")

T = Text(root, height = 5, width = 52)

Label(text="MINI AI SYSTEM",font="TrebuchetMS 25 bold",fg="black").pack(pady=20)

label= Label(root, text= "SELECT BELOW ICON", font= ('Trebuchet 13 underline'))
label.pack()

mic = PhotoImage(file="mic2.png")
control = PhotoImage(file="ctrl.png")

sp_rec = Button(root,image=mic,borderwidth=1,cursor="hand2",font="TrebuchetMS 15",text="mic Recognition",bg="#000000",fg="black",border=0,command=S_to_T.Play).place(x=85, y=120)
Label(text="Speech Recognition",font="TrebuchetMS 10 bold",fg="black").place(x=70, y=240)
volume_ctrl = Button(root,image=control,borderwidth=1,cursor="hand2",font="TrebuchetMS 15",text="Volume",bg="#000000",fg="black",border=0,command=ctrl.Ctrl).place(x=520, y=120)
Label(text="Volume Control",font="TrebuchetMS 10 bold",fg="black").place(x=520, y=240)

Label(text="INSTRUCTIONS",font="TrebuchetMS 20 bold",fg="black").pack(pady=200)
Label(text="1] Click on MIC image to Activate Speech Recognition Feature",font="TrebuchetMS 10 bold",fg="red").place(x=100, y=380)
Label(text="• Say \"Play\" to Play Recorded Audio",font="TrebuchetMS 10 bold",fg="red").place(x=100, y=400)
Label(text="• Say \"Weather\" to get Weather Update",font="TrebuchetMS 10 bold",fg="red").place(x=100, y=420)
Label(text="• Say \"Volume\" to control Volume using Hand Gestures",font="TrebuchetMS 10 bold",fg="red").place(x=100, y=440)
Label(text="2] To Exit and Close UI Say \"CLOSE GUI\"",font="TrebuchetMS 10 bold",fg="red").place(x=100, y=480)

root.mainloop()