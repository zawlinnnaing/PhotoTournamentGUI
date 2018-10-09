from tkinter import *
from tkinter import ttk

class Steps(Frame):x

    def __init__(self,master=NONE):
        # Frame.__init__(self,master)
        self.banPhotoList = list()
        self.checkButtonList = list()
        self.creatingStringVarList(10)
        self.master = master
        self.init_window(master)

    def init_window(self,master):
        # Initializing window
        topFrame = Frame(master)
        topFrame.pack(fill=X,pady=30)
        bottomFrame = Frame(master)
        bottomFrame.pack()

        #Adding widgets to topFrame
        title = ttk.Label(topFrame,text="#title", font=('Arial',24,'bold'), background='white')
        title.pack(side=LEFT,expand=True,fill=X)

        printLogo = PhotoImage(file='print.png').subsample(30,30)
        printButton = ttk.Button(topFrame,text="Print", image=printLogo, compound=LEFT,command=self.printFunc)
        printButton.pack(side=LEFT, padx=10)

        banLogo = PhotoImage(file='ban.png').subsample(15,15)
        banButton = ttk.Button(topFrame,text="Ban a photo", image=banLogo, compound=LEFT, command=self.banPhotoFunc)
        banButton.pack(side=LEFT, padx=10)

        skipButton = ttk.Button(topFrame,text= "Skip")
        skipButton.pack(side=LEFT, padx=10)

        reviewButton = ttk.Button(topFrame,text='Review a photo', command=self.reviewPhotoFunc)
        reviewButton.pack(side=LEFT, padx=10)

        gradedMark = ttk.Label(topFrame,text='Graded Mark')
        gradedMark.pack(side=LEFT, padx=10)

        # Adding widgets to bottom frame
        columns = 6
        # Creating header for table
        for i in range(columns):
            if(i == 5):
                    ttk.Label(bottomFrame,text='Total', anchor='center', borderwidth=3, relief='solid').grid(row = 0, column=i,ipadx=40,ipady=20)
                    break
            ttk.Label(bottomFrame,text = 'Judge#'+ str(i+1), anchor='center', borderwidth=3, relief='solid').grid(row = 0, column=i,ipadx=40,ipady=20)

        ttk.Label(bottomFrame,text='Check for banning or reviewing photos').grid(row=0,column=columns+1,ipadx=40,ipady=20)

        # Creating table cells
        rows = 10
        for i in range(1,rows):
            ttk.Checkbutton(bottomFrame,onvalue=str(i),offvalue=NONE,variable=self.checkButtonList[i]).grid(row=i, column=columns+1)
            for j in range(columns):
                    ttk.Label(bottomFrame,text = str(j+i), anchor='center', borderwidth=3, relief='solid').grid(row = i, column=j,sticky = 'nsew', ipady=20)
                    # ttk.Checkbutton(bottomFrame,)

    # Event Handling sectionx
    def printFunc(self):
        pass

    def banPhotoFunc(self):
        for x in self.checkButtonList:
            print (' '+ x.get())
            x.set(NONE)

    def creatingStringVarList (self,noOfPhotos):
        for x in range(noOfPhotos):
            x = StringVar()
            self.checkButtonList.append(x)
    
    def reviewPhotoFunc(self):
        for x in self.checkButtonList:
            print (' '+ x.get())
            x.set(NONE)

root =Tk()
root.title('Result for voted photos')
# root.geometry('1600x800+0+0')
root.attributes('-fullscreen',True)
app = Steps(root)
root.mainloop()
