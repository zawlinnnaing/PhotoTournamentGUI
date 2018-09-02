from tkinter import *
# from data_store import Stage

class Step_One():
    def __init__(self, master, stage, no_of_photo, no_of_judge):
        self.stage = stage
        self.no_of_photo = no_of_photo
        self.no_of_judge = no_of_judge
        self.judge_vote_holders = list()
        self.current_photo = 1
        self.vote_holder_vars = list()
        for i in range(no_of_judge):
            self.vote_holder_vars.append(StringVar())


        ## tracking variables

        # self.t1=StringVar()
        # self.t2=StringVar()
        # self.t3=StringVar()
        # self.t4=StringVar()
        # self.t5=StringVar()
        self.total=StringVar()
        self.initializeUI(master)


    def initializeUI(self,master):
    #base frames
        self.tframe= Frame(master)
        self.tframe.grid(row=0, column=0, rowspan=1)
        self.mframe= Frame(master)
        self.mframe.grid(row=1, column=0, rowspan=3)
        self.bframe= Frame(master)
        self.bframe.grid(row=4, column=0, rowspan=1)
    #top frame for step number ... etc 
        
        self.title=Label(self.tframe,font=('ariel',15),text="Step "+str(self.stage),relief='ridge')
        self.title.grid(row=0,column=0,padx=120, pady=10)
        self.title=Label(self.tframe,font=('ariel',15),text="Mandalay Hill Contest",relief='ridge')
        self.title.grid(row=0,column=1,padx=120, pady=10)
        self.title=Label(self.tframe,font=('ariel',15),text="Photo Number "+str(self.no_of_photo),relief='ridge')
        self.title.grid(row=0,column=3,padx=120, pady=10)

        #mid frame for Labels to fit voting results
        for i in range(self.no_of_judge):
            self.judge_vote_holders.append(Label(self.mframe,font=('ariel',80,'bold'),padx=50,pady=80,textvariable=self.vote_holder_vars[i],relief='solid'))
            self.judge_vote_holders[i].bind("<Key>", self.key)
            self.judge_vote_holders[i].focus_set
            self.judge_vote_holders[i].grid(row=0, column=i)





            # self.l1=Label(self.mframe,font=('ariel',80,'bold'),padx=50,pady=80,textvariable=self.t1,relief='solid')
            # self.l1.bind("<Key>",self.key)
            # self.l1.focus_set()
            # self.l1.grid(row=0,column=0)
            
            # self.l2=Label(self.mframe,font=('ariel',80,'bold'),padx=50,pady=80,textvariable=self.t2,relief='solid')
            # self.l2.bind("<Key>",self.key)
            # self.l2.focus_set()
            # self.l2.grid(row=0,column=1)

            # self.l3=Label(self.mframe,font=('ariel',80,'bold'),padx=50,pady=80,textvariable=self.t3,relief='solid')
            # self.l3.bind("<Key>",self.key)
            # self.l3.focus_set()
            # self.l3.grid(row=0,column=2)

            # self.l4=Label(self.mframe,font=('ariel',80,'bold'),padx=50,pady=80,textvariable=self.t4,relief='solid')
            # self.l4.bind("<Key>",self.key)
            # self.l4.focus_set()
            # self.l4.grid(row=0,column=3)

            # self.l5=Label(self.mframe,font=('ariel',80,'bold'),padx=50,pady=80,textvariable=self.t5,relief='solid')
            # self.l5.bind("<Key>",self.key)
            # self.l5.focus_set()
            # self.l5.grid(row=0,column=4)

            self.l6=Label(self.mframe,font=('ariel',80,'bold'),padx=50,pady=80,textvariable=self.total,relief='solid',bg='yellow')
            self.l6.bind("<Key>",self.key)
            self.l6.focus_set() 
            self.l6.grid(row=1,column=4)

    #bottom frame for buttons      
        self.b1= Button(self.bframe,text="Pause")
        self.b1.grid(row=0,column=0,padx=120, pady=10)
        
        self.b2= Button(self.bframe,text="Continue", command = self.continue_callable)
        self.b2.grid(row=0,column=1,padx=120, pady=10)

# key binding 
    def key(self,event):     
        if(event.char=='q' or event.char=='Q'):
            self.vote_holder_vars[0].set(1)      
        if(event.char=='w' or event.char=='W'):
            self.vote_holder_vars[0].set(0)
        if(event.char=='e' or event.char=='E'):
            self.vote_holder_vars[1].set(1)       
        if(event.char=='r' or event.char=='R'):
            self.vote_holder_vars[1].set(0)
        if(event.char=='a' or event.char=='A'):
            self.vote_holder_vars[2].set(1)       
        if(event.char=='s' or event.char=='S'):
            self.vote_holder_vars[2].set(0)
        if(event.char=='d' or event.char=='D'):
            self.vote_holder_vars[3].set(1)       
        if(event.char=='f' or event.char=='F'):
            self.vote_holder_vars[3].set(0)
        if(event.char=='t' or event.char=='T'):
            self.vote_holder_vars[4].set(1)       
        if(event.char=='y' or event.char=='Y'):
            self.vote_holder_vars[5].set(0)
                
        # if(self.t1.get()!="" and self.t2.get()!="" and self.t3.get()!="" and self.t4.get()!="" and self.t5.get()!=""):
        #     self.sum.set(eval(self.t1.get()+"+"+self.t2.get()+"+"+self.t3.get()+"+"+self.t4.get()+"+"+self.t5.get())) 

        sum = 0
        for i in self.vote_holder_vars:
            sum += int(i.get())
            self.total.set(str(sum))

            if(self.total.get()<='2'):
                self.l6.config(bg="red")
            else:
                self.l6.config(bg="green")
        
    def continue_callable(self):
        for i in self.vote_holder_vars:
            i.set('')
        # self.t1.set('')
        # self.t2.set('')
        # self.t3.set('')
        # self.t4.set('')
        # self.t5.set('')
        self.total.set('')
        self.l6.config(bg='yellow')
        # Stage().feed(self., )


def main():
    root=Tk()
    root.geometry("1600x800+0+0")
    root.title("Photo Voting")
    s1 = Step_One(root,1,50,3)
    root.mainloop()

if __name__ == '__main__':
    main()
