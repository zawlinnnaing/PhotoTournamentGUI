from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Results for voted photos")
root.geometry('1600x800')

# Initializing window
topFrame = Frame(root)
topFrame.pack(fill=X,pady=30)
bottomFrame = Frame(root)
bottomFrame.pack()

#Adding widgets to topFrame
title = ttk.Label(topFrame,text="#title", font=('Arial',24,'bold'), background='white')
title.pack(side=LEFT,expand=True,fill=X)

printLogo = PhotoImage(file='print.png').subsample(30,30)
printButton = ttk.Button(topFrame,text="Print", image=printLogo, compound=LEFT)
printButton.pack(side=LEFT, padx=10)

banLogo = PhotoImage(file='ban.png').subsample(15,15)
banButton = ttk.Button(topFrame,text="Ban a photo", image=banLogo, compound=LEFT)
banButton.pack(side=LEFT, padx=10)

skipButton = ttk.Button(topFrame,text= "Skip")
skipButton.pack(side=LEFT, padx=10)

gradedMark = ttk.Label(topFrame,text='Graded Mark')
gradedMark.pack(side=LEFT, padx=10)

# Adding widgets to bottom frame
for i in range(6):
    if(i == 5):
            ttk.Label(bottomFrame,text='Total', anchor='center', borderwidth=3, relief='solid').grid(row = 0, column=i,ipadx=80,ipady=20)
            break
    ttk.Label(bottomFrame,text = 'Judge#'+ str(i+1), anchor='center', borderwidth=3, relief='solid').grid(row = 0, column=i,ipadx=80,ipady=20)
    
rows = 10
columns = 6
for i in range(1,rows):
    for j in range(columns):
            ttk.Label(bottomFrame,text = str(j+i), anchor='center', borderwidth=3, relief='solid').grid(row = i, column=j,sticky = 'nsew', ipady=20)


root.mainloop()