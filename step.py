from tkinter import *
from tkinter import ttk

class Steps(Frame):

    def __init__(self,master=NONE):
        # Frame.__init__(self,master)
        self.master = master
        self.init_window(master)

    def init_window(self,master):
        frame1 = Frame(master)
        frame1.pack()

        title = ttk.Label(frame1,text= "#title",font=('Arial',24,'bold'),anchor='nw')
        title.pack()




root =Tk()
root.title('Result for voted photos')
root.geometry('1600x800')
app = Steps(root)
root.mainloop()
