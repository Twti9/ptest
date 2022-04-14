#开发者：罗地观生
#开发时间：2021/8/27 8:49
import tkinter
root=tkinter.Tk()
label=tkinter.Label(root,text='Hello,GUI')
label.pack()
button1=tkinter.Button(root,text='Button1')
button1.pack(side=tkinter.LEFT)
button2=tkinter.Button(root,text='Button2')
button2.pack(side=tkinter.RIGHT)
root.mainloop()