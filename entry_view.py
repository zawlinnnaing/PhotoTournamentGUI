from tkinter import *
from tkinter import ttk

class EntryView:
    def __init__(self,master=None):
        self.master = master
        self.init_window()
    
    def init_window(self):
        frame1 = Frame(self.master)
        frame1.pack(fill=X)

        bottomFrame = Frame(self.master)
        bottomFrame.pack(fill=BOTH, expand=True)

        sideFrame = Frame(bottomFrame, width=600 )
        
        # Testing GUI
        sideFrame.config(borderwidth=1, relief='solid')

        sideFrame.pack(side=LEFT, fill=Y)

        logoFrame = Frame(bottomFrame)
        # Testing GUI
        logoFrame.config(borderwidth=1, relief='solid')

        logoFrame.pack(side=LEFT,fill=BOTH, expand=True)

        titleLable = Label(frame1,text='The Upper Myanmar Photographics Society', font=('Arial', 24,'bold'), pady=20)
        titleLable.pack(fill=BOTH, expand=True)

        # Generating buttons at side frame
        ttk.Button(sideFrame,text='Create a competition').pack(padx=40, pady=20, anchor='s')
        ttk.Button(sideFrame,text='History').pack(padx=40, pady=20, anchor='s')
        ttk.Button(sideFrame,text='Setting').pack(padx=40, pady=20, anchor='s')
        ttk.Button(sideFrame,text='About us').pack(padx=40, pady=20, anchor='s')


        logo = PhotoImage(file="./logo.png")
        logoLabel = Label(logoFrame,image=logo)
        logoLabel.pack()

root = Tk()
root.title('Entry View')
# root.geometry('1600x800+0+0')
root.attributes('-fullscreen',True)
entryView = EntryView(root)
root.mainloop()