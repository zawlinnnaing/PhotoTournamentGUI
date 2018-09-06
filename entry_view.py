from tkinter import *
from tkinter import ttk


class EntryView:
    def __init__(self,master=None):
<<<<<<< HEAD
=======

        btLabel=Label(btFrame,text='bla bla bla bla bla ....')
        btLabel.pack(side=RIGHT)

        #pop Up Box

    def create_competition(self):
            subRoot=Tk()
            subRoot.geometry("500x250+0+0")
            subRoot.title("Create a competition")

            tframe=Frame(subRoot)
            tframe.pack()

            bframe=Frame(subRoot)
            bframe.pack()

            nameLabel= Label(tframe,text="Name of Tournament", font=( 'aria' ,16),pady=15)
            nameLabel.grid(row=0,column=0)
            nameEntry= Entry(tframe, font=( 'aria' ,12))
            nameEntry.grid(row=0,column=1)

            n_o_pLabel= Label(tframe,text="Number of Photo", font=( 'aria' ,16),pady=15)
            n_o_pLabel.grid(row=1,column=0)
            n_o_pEntry= Entry(tframe, font=( 'aria' ,12))
            n_o_pEntry.grid(row=1,column=1)

            n_o_jLabel= Label(tframe,text="Number of Judge", font=( 'aria' ,16),pady=15)
            n_o_jLabel.grid(row=2,column=0)
            variable = StringVar(tframe)
            variable.set("5")
            n_o_jMenu = OptionMenu(tframe, variable, "3", "5", "7")
            n_o_jMenu.grid(row=2,column=1)

            next_button=ttk.Button(bframe,text='Next')
            next_button.grid(row=0,column=0,padx=20,pady=20)
            cancel_button=ttk.Button(bframe,text='Cancel',command=subRoot.destroy)
            cancel_button.grid(row=0,column=1,padx=20,pady=20)


root = Tk()
root.title('Entry View')
# root.geometry('1600x800+0+0')  
root.attributes('-fullscreen',True)
entryView = EntryView(root)
root.mainloop()
>>>>>>> 8b5ee3d44e08b3ac5856141ec893a7112d70c64d
