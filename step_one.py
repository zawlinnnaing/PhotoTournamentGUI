from tkinter import *


class Step_One:
    
    

    def __init__(self,master):

# tracking variables
        self.t1=StringVar()
        self.t2=StringVar()
        self.t3=StringVar()
        self.t4=StringVar()
        self.t5=StringVar()
        self.sum=StringVar()
#base frames

        self.tframe= Frame(master)
        self.tframe.pack()
        self.mframe= Frame(master)
        self.mframe.pack()
        self.bframe= Frame(master)
        self.bframe.pack()
#top frame for step number ... etc 

        self.title=Label(self.tframe,font=('ariel',15),text="Step - 1",relief='ridge')
        self.title.grid(row=0,column=0,padx=120, pady=10)
        self.title=Label(self.tframe,font=('ariel',15),text="Mandalay Hill Contest",relief='ridge')
        self.title.grid(row=0,column=1,padx=120, pady=10)
        self.title=Label(self.tframe,font=('ariel',15),text="Photo Number- ",relief='ridge')
        self.title.grid(row=0,column=3,padx=120, pady=10)
#mid frame for Labels to fit voting results

        self.l1=Label(self.mframe,font=('ariel',80,'bold'),padx=180,pady=80,textvariable=self.t1,relief='solid')
        self.l1.bind("<Key>",self.key)
        self.l1.focus_set()
        self.l1.grid(row=0,column=0)
        
        self.l2=Label(self.mframe,font=('ariel',80,'bold'),padx=180,pady=80,textvariable=self.t2,relief='solid')
        self.l2.bind("<Key>",self.key)
        self.l2.focus_set()
        self.l2.grid(row=0,column=1)

        self.l3=Label(self.mframe,font=('ariel',80,'bold'),padx=180,pady=80,textvariable=self.t3,relief='solid')
        self.l3.bind("<Key>",self.key)
        self.l3.focus_set()
        self.l3.grid(row=0,column=2)

        self.l4=Label(self.mframe,font=('ariel',80,'bold'),padx=180,pady=80,textvariable=self.t4,relief='solid')
        self.l4.bind("<Key>",self.key)
        self.l4.focus_set()
        self.l4.grid(row=1,column=0)

        self.l5=Label(self.mframe,font=('ariel',80,'bold'),padx=180,pady=80,textvariable=self.t5,relief='solid')
        self.l5.bind("<Key>",self.key)
        self.l5.focus_set()
        self.l5.grid(row=1,column=1)

        self.l6=Label(self.mframe,font=('ariel',80,'bold'),padx=180,pady=80,textvariable=self.sum,relief='solid',bg='yellow')
        self.l6.bind("<Key>",self.key)
        self.l6.focus_set() 
        self.l6.grid(row=1,column=2)

#bottom frame for buttons      
        self.b1= Button(self.bframe,text="Pause")
        self.b1.grid(row=0,column=0,padx=120, pady=10)
        
        self.b2= Button(self.bframe,text="Continue")
        self.b2.grid(row=0,column=1,padx=120, pady=10)
# key binding 
    def key(self,event):     
        if(event.char=='q' or event.char=='Q'):
            self.t1.set(1)      
        if(event.char=='w' or event.char=='W'):
            self.t1.set(0)
        if(event.char=='e' or event.char=='E'):
            self.t2.set(1)       
        if(event.char=='r' or event.char=='R'):
            self.t2.set(0)
        if(event.char=='a' or event.char=='A'):
            self.t3.set(1)       
        if(event.char=='s' or event.char=='S'):
            self.t3.set(0)
        if(event.char=='d' or event.char=='D'):
            self.t4.set(1)       
        if(event.char=='f' or event.char=='F'):
            self.t4.set(0)
        if(event.char=='t' or event.char=='T'):
            self.t5.set(1)       
        if(event.char=='y' or event.char=='Y'):
            self.t5.set(0)
                
        if(self.t1.get()!="" and self.t2.get()!="" and self.t3.get()!="" and self.t4.get()!="" and self.t5.get()!=""):
            self.sum.set(eval(self.t1.get()+"+"+self.t2.get()+"+"+self.t3.get()+"+"+self.t4.get()+"+"+self.t5.get())) 

            if(self.sum.get()<='2'):
                self.l6.config(bg="red")
            else:
                self.l6.config(bg="green")
        
       

def main():
    root=Tk()
    root.geometry("1600x800+0+0")
    root.title("Photo Voting")
    s1=Step_One(root)
    root.mainloop()

if __name__ == '__main__':
    main()
