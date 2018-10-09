from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import data_store
import utilities



class EntryView:
    def __init__(self,master):
        utilities.initialize_gobals()
        utilities.data_global_scope['rootGlobalMaster'] = master
        self.master = master
        self.init_window()
    
    def init_window(self):
        frame1 = Frame(self.master)
        frame1.pack(fill=X)
        midFrame = Frame(self.master)
        midFrame.pack(fill=BOTH, expand=True)
        btFrame = Frame(self.master)
        btFrame.pack(fill=BOTH, expand=True)
        sideFrame = Frame(midFrame, width=600 )
        # Testing GUI
        sideFrame.config(borderwidth=1, relief='solid')
        sideFrame.pack(side=LEFT, fill=Y)
        logoFrame = Frame(midFrame)
        # Testing GUI
        logoFrame.config(borderwidth=1, relief='solid')
        logoFrame.pack(side=LEFT,fill=BOTH, expand=True)
        titleLable = Label(frame1,text='The Upper Myanmar Photographics Society', font=('Arial', 24,'bold'), pady=20)
        titleLable.pack(fill=BOTH, expand=True)
        s = ttk.Style()
        s.configure('TButton',padx=25)
        # Generating buttons at side frame
        ttk.Button(sideFrame,text='Create a competition',command=self.create_competition).pack(padx=40, pady=10, anchor='s')
        ttk.Button(sideFrame,text='History').pack(padx=40, pady=10, anchor='s')
        ttk.Button(sideFrame,text='Setting').pack(padx=40, pady=10, anchor='s')
        ttk.Button(sideFrame,text='About us').pack(padx=40, pady=10, anchor='s')
        # logo = PhotoImage(file="logo.gif")
        logo =PhotoImage(file="logo_1.png")
        logoLabel = Label(logoFrame,image=logo)
        logoLabel.image=logo
        logoLabel.pack()
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
        nameLabel= Label(tframe,text="Name of Tournament", font=('aria' ,16),pady=15)
        nameLabel.grid(row=0,column=0)
        nameEntry= Entry(tframe, font=('aria' ,12))
        nameEntry.grid(row=0,column=1)

        n_o_pLabel= Label(tframe,text="Number of Photo", font=('aria' ,16),pady=15)
        n_o_pLabel.grid(row=1,column=0)
        n_o_pEntry= Entry( tframe, font=('aria' ,12))
        n_o_pEntry.grid(row=1,column=1)

        n_o_jLabel= Label(tframe,text="Number of Judge", font=('aria' ,16),pady=15)
        n_o_jLabel.grid(row=2,column=0)
        menu_variable = StringVar()
        menu_variable.set('5') 
        n_o_jMenu = OptionMenu(tframe, menu_variable, '3', '5', '7')
        n_o_jMenu.grid(row=2,column=1)

        next_button=ttk.Button(bframe,text='Next',command=(lambda : self.initialize_stages(subRoot, [nameEntry.get(),n_o_pEntry.get(),menu_variable.get()])))
        next_button.grid(row=0,column=0,padx=20,pady=20)
        cancel_button=ttk.Button(bframe,text='Cancel',command=subRoot.destroy)
        cancel_button.grid(row=0,column=1,padx=20,pady=20)
    
    def initialize_stages( self, subroot, args_array):
        try:
            utilities.data_global_scope['tournament_name'] = str(args_array[0])
            utilities.data_global_scope['no_of_photos'] = int(args_array[1])
            utilities.data_global_scope['no_of_judges'] = int(args_array[2])
            print(args_array)
            data_store.StageChain()
            subroot.destroy()
        except ValueError:
            messagebox.showerror("Error","Photo and judge number must be integer.")

def main():
    root = Tk()
    root.title('Entry View')
    # root.geometry('1600x800+0+0')  
    root.attributes('-fullscreen',True)
    entryView = EntryView(root)
    root.mainloop()

if __name__ == '__main__':
    main()
