import tkinter as tk
from tkinter import messagebox as tkm
import random
log_in=tk.Tk()
log_in.title('比大小')
log_in.geometry('500x400')
def pd():
    try:
        player1_get=int(player1_input.get())
        player2_get=random.randint(0,5)
        if player1_get<=5 and player2_get<=5:
            if player1_get>player2_get:
                tkm.showinfo(title=None,message='你赢了。')
            elif player2_get>player1_get:
                tkm.showinfo(title=None, message='我赢了。')
            else:
                tkm.showinfo(title=None, message='平局。')
        else:
            tkm.showwarning(title=None,message='输入大小：0~5。')
    except ValueError:
        tkm.showwarning(title=None,message="InputError!")


yh = tk.Label(log_in,text='比大小',font=('黑体',50)).pack()
player1 = tk.Label(log_in,text='Input1',font=('黑体',30)).pack()
player1_input=tk.Entry(log_in,font=('黑体',30),show='·')
player1_input.pack()



yes = tk.Button(log_in,text='确定',font=('黑体',20),command=pd).pack()
log_in.mainloop()
