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

        titleLable = Label(frame1,text='#title', font=('Arial', 24,'bold'), pady=20)
        titleLable.pack(fill=BOTH, expand=True)

        # Generating buttons at side frame
        for i in range (4):
            ttk.Button(sideFrame,text='Button no :'+ str(i)).pack(padx=40, pady=20, anchor='s')

root = Tk()
root.title('Entry View')
root.geometry('1600x800+0+0')
entryView = EntryView(root)
root.mainloop()