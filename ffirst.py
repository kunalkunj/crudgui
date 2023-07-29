from tkinter import *
root = Tk()

thetable=Label(root,text="Welcom To New Generation")
thetable.pack()


frame = Frame(root)
button1 = Button(frame,text="Button1")
# button2 = Button(frame,text="Button2")
# button3 = Button(frame,text="Button3")

button1.pack(side=LEFT)
# button2.pack(side=RIGHT)
# button3.pack(side=BOTTOM)

frame.pack(side=BOTTOM)

frame2 = Frame(root)
button4 = Button(frame2,text="Button4")
button4.pack(side=RIGHT)
frame2.pack()


frame3 = Frame(root)
button5 = Button(frame3,text="Button4")
button5.pack(side=BOTTOM)
frame3.pack()


frame4 = Frame(root)
button6 = Button(frame4,text="Button4")
button6.pack(side=TOP)
frame4.pack()





root.mainloop()