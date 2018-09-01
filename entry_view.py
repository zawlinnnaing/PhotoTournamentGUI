from tkinter import *

class EntryView:
    def __init__(self,master=None):
        self.master = master
        self.init_window()
    
    def init_window(self):
        logoImage = PhotoImage(file='ban.png')
        mainCanvas = Canvas(self.master)
        mainCanvas.pack(expand=True, fill=BOTH)

        mainCanvas.create_image(100,100, image=logoImage,anchor= NW)




root = Tk()
root.title('Entry View')
root.geometry('1600x800+0+0')
entryView = EntryView(root)
root.mainloop()