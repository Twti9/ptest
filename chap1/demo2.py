import tkinter
import time
import threading
from random import random
from tkinter import messagebox as tkMessageBox
class choujiang:
    def __init__(self):
        self.root=tkinter.Tk()
        self.root.title('LOwB版转盘')
        self.root.minsize(300,300)
        self.isloop=False
        self.newloop=False
        self.value=[]
        self.setwindow()
        self.root.mainloop()
    def setwindow(self):
        self.btn_start=tkinter.Button(self.root,text='start/stop',command=self.newtask)
        self.btn_start.place(x=125,y=125,width=70,height=70)

        self.btn1=tkinter.Button(self.root,text='1',bg='red')
        self.btn1.place(x=20,y=20,width=50,height=50)

        self.btn2 = tkinter.Button(self.root, text='2', bg='white')
        self.btn2.place(x=90, y=20, width=50, height=50)

        self.btn3 = tkinter.Button(self.root, text='3', bg='white')
        self.btn3.place(x=160, y=20, width=50, height=50)

        self.btn4 = tkinter.Button(self.root, text='3', bg='white')
        self.btn4.place(x=230, y=20, width=50, height=50)

        self.btn5 = tkinter.Button(self.root, text='3', bg='white')
        self.btn5.place(x=230, y=90, width=50, height=50)

        self.btn6 = tkinter.Button(self.root, text='2', bg='white')
        self.btn6.place(x=230, y=160, width=50, height=50)

        self.btn7 = tkinter.Button(self.root, text='1', bg='white')
        self.btn7.place(x=230, y=230, width=50, height=50)

        self.btn8 = tkinter.Button(self.root, text='3', bg='white')
        self.btn8.place(x=160, y=230, width=50, height=50)

        self.btn9 = tkinter.Button(self.root, text='2', bg='white')
        self.btn9.place(x=90, y=230, width=50, height=50)

        self.btn10 = tkinter.Button(self.root, text='3', bg='white')
        self.btn10.place(x=20, y=230, width=50, height=50)

        self.btn11 = tkinter.Button(self.root, text='1', bg='white')
        self.btn11.place(x=20, y=160, width=50, height=50)

        self.btn12 = tkinter.Button(self.root, text='3', bg='white')
        self.btn12.place(x=20, y=90, width=50, height=50)

        self.girlfriends=[self.btn1,self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,self.btn7,self.btn8,
                          self.btn9,self.btn10,self.btn11,self.btn12]
    def round(self):
        if self.isloop==True:
            return
        i=0
        while True:
            if self.newloop==True:
                self.newloop=False
                self.value=False
                self.value=self.girlfriends[i-1]['text']
                if self.value=='1':
                    tkMessageBox.showinfo('Winning Result','恭喜获得一等奖！')
                elif self.value=='2':
                    tkMessageBox.showinfo('Winning Result', '恭喜获得二等奖！')
                else:
                    tkMessageBox.showinfo('Winning Result', '恭喜获得三等奖！')
                return
            time.sleep(0.1)
            for x in self.girlfriends:
                x['bg']='white'
            self.girlfriends[i]['bg']='red'
            i+=1
            if i >=len(self.girlfriends):
                i=0
    def newtask(self):
        if self.isloop==False:
            t=threading.Thread(target=self.round)
            t.start()
            self.isloop=True
        elif self.isloop==True:
            self.isloop=False
            self.newloop=True
if __name__ == '__main__':
    c=choujiang()