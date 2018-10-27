from tkinter import *
from tkinter import ttk
import data_store as data_store
import utilities
import numpy as np
import individual_step as individual_step


class Steps():

    def __init__(self, dataFrame, current_photo_indices):
        # Frame.__init__(self,master)
        utilities.clear_screen(utilities.data_global_scope['rootGlobalMaster'])
        self.checkButtonList = list()
        # self.master = master
        self.current_photo_indices = current_photo_indices
        self.creatingStringVarList(len(self.current_photo_indices))
        self.master = utilities.data_global_scope['rootGlobalMaster']
        self.dataFrame = dataFrame
        self.init_window(self.master)

    def init_window(self, master):
        # Initializing window
        topFrame = Frame(master)
        topFrame.pack(fill=X, pady=30)
        bottomFrame = Frame(master)
        bottomFrame.pack()

        # Adding widgets to topFrame
        title = ttk.Label(topFrame, text="#title", font=(
            'Arial', 24, 'bold'), background='white')
        title.pack(side=LEFT, expand=True, fill=X)

        printLogo = PhotoImage(file='print.png').subsample(30, 30)
        printButton = ttk.Button(
            topFrame, text="Print", image=printLogo, compound=LEFT, command=self.printFunc)
        printButton.pack(side=LEFT, padx=10)

        banLogo = PhotoImage(file='ban.png').subsample(15, 15)
        banButton = ttk.Button(topFrame, text="Ban a photo",
                               image=banLogo, compound=LEFT, command=self.banPhotoFunc)
        banButton.pack(side=LEFT, padx=10)

        skipButton = ttk.Button(topFrame, text="Skip")
        skipButton.pack(side=LEFT, padx=10)

        reviewButton = ttk.Button(
            topFrame, text='Review a photo', command=self.reviewPhotoFunc)
        reviewButton.pack(side=LEFT, padx=10)

        gradedMark = ttk.Label(topFrame, text='Graded Mark')
        gradedMark.pack(side=LEFT, padx=10)

        # Adding widgets to bottom frame
        columns = len(self.dataFrame.columns)
        # Creating header for table
        for i in range(columns):
            ttk.Label(bottomFrame, text=self.dataFrame.columns[i], anchor='center', borderwidth=3, relief='solid').grid(
                row=0, column=i, ipadx=40, ipady=20)

        ttk.Label(bottomFrame, text='Check for banning or reviewing photos').grid(
            row=0, column=columns+1, ipadx=20, ipady=20)
        # Creating table cells
        rows = len(self.current_photo_indices)
        for i in range(rows):
            ttk.Checkbutton(bottomFrame, onvalue=str(
                self.current_photo_indices[i]), offvalue=NONE, variable=self.checkButtonList[i]).grid(row=i+1, column=columns+1)
            for j in range(columns):
                ttk.Label(bottomFrame, text=str(self.dataFrame.iloc[i, j]), anchor='center', borderwidth=3, relief='solid').grid(
                    row=i+1, column=j, sticky='nsew', ipady=20)

    # Event Handling sectionx
    def printFunc(self):
        pass

    def banPhotoFunc(self):
        banPhotoList = list()
        for x in self.checkButtonList:
            if x is not '' or not NONE:
                banPhotoList.append(x.get())
        stage = data_store.Stage
        stage.banPhotoDataframe(stage,banPhotoList)

    def creatingStringVarList(self, noOfPhotos):
        for x in range(noOfPhotos):
            x = StringVar()
            self.checkButtonList.append(x)

    def reviewPhotoFunc(self):
        reviewPhotoList = list()
        for x in self.checkButtonList:
            if x.get() is not '' or not NONE:
                reviewPhotoList.append(x.get())
            x.set(NONE)
        print(reviewPhotoList)
# Testing purpose
