# from S_to_T import MyText, SpeakText

# def Play():
#     input_string = MyText.lower()

#     if "play" in input_string:
#         SpeakText("Playing your Recording....")
#         from playsound import playsound 
#         playsound('rec.mp3')
#     elif "stop" in input_string:
#         SpeakText("Stopped!!")
#     else:
#         SpeakText("Error in Opening File!")
# import tkinter

# master=tkinter.Tk()
# master.title("pack() method")
# master.geometry("450x350")

# button1=tkinter.Button(master, text="LEFT")
# button1.pack(side=tkinter.LEFT)

# button2=tkinter.Button(master, text="RIGHT")
# button2.pack(side=tkinter.RIGHT)

# button3=tkinter.Button(master, text="TOP")
# button3.pack(side=tkinter.TOP)

# button4=tkinter.Button(master, text="BOTTOM")
# button4.pack(side=tkinter.BOTTOM)

# master.mainloop()

import tkinter

master=tkinter.Tk()
master.title("place() method")
master.geometry("450x350")

button1=tkinter.Button(master, text="button1")
button1.place(x=25, y=100)

button2=tkinter.Button(master, text="button2")
button2.place(x=100, y=25)

button3=tkinter.Button(master, text="button3")
button3.place(x=175, y=100)

master.mainloop()