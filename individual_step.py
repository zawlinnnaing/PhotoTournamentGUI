from tkinter import *
import entry_view
import utilities 
import step

class individual_step():
    def __init__(self, stage_instance, stage_no, photo_indices):
        utilities.clear_screen(utilities.data_global_scope['rootGlobalMaster'])
        self.master = utilities.data_global_scope['rootGlobalMaster']
        self.no_of_judges = utilities.data_global_scope['no_of_judges']
        self.tournament_name = utilities.data_global_scope['tournament_name']
        self.stage_instance = stage_instance
        self.stage_no = stage_no
        self.photo_indices = photo_indices
        # self.no_of_photos = entry_view.data_global_scope['no_of_photos']  
        
        self.judge_vote_holders = list()
        self.transversed_photo = 0
        self.vote_holder_vars = list()
        for i in range(self.no_of_judges):
            self.vote_holder_vars.append(StringVar())
        self.total = StringVar()
        self.initializeUI(self.master)
        print('hello')


    def initializeUI(self,master):
    #base frames
        self.tframe = Frame(master)
        self.tframe.grid(row = 0, column = 0, rowspan = 1)
        self.mframe= Frame(master)
        self.mframe.grid(row = 1, column = 0, rowspan = 3)
        self.bframe= Frame(master)
        self.bframe.grid(row = 4, column = 0, rowspan = 1)
    #top frame for step number ... etc 
        
        self.title = Label(self.tframe, font = ('ariel',15), text = "Step "+str(self.stage_no), relief = 'ridge')
        self.title.grid(row = 0, column = 0, padx = 120, pady = 10)
        self.title = Label(self.tframe, font = ('ariel',15), text = "Mandalay Hill Contest", relief = 'ridge')
        self.title.grid(row = 0, column = 1, padx = 120, pady = 10)
        self.title = Label(self.tframe,font=('ariel',15),text="Photo Number "+str(self.photo_indices.size),relief='ridge')
        self.title.grid(row = 0, column = 3,padx = 120, pady = 10)

        #mid frame for Labels to fit voting results
        for i in range(self.no_of_judges):
            self.judge_vote_holders.append(Label(self.mframe, font = ('ariel',80,'bold'), padx = 50, pady = 80, textvariable = self.vote_holder_vars[i], relief = 'solid'))
            self.judge_vote_holders[i].bind("<Key>", self.key)
            self.judge_vote_holders[i].focus_set
            self.judge_vote_holders[i].grid(row = 0, column = i)

            self.l6 = Label(self.mframe, font = ('ariel',80,'bold'), padx = 50, pady = 80, textvariable = self.total, relief = 'solid', bg = 'yellow')
            self.l6.bind("<Key>", self.key)
            self.l6.focus_set() 
            self.l6.grid(row = 1, column = 4)

    #bottom frame for buttons      
        self.b1 = Button(self.bframe, text = "Pause")
        self.b1.grid(row = 0, column = 0, padx = 120, pady = 10)
        
        self.b2 = Button(self.bframe, text = "Continue", command = self.continue_callable)
        self.b2.grid(row = 0, column = 1, padx = 120, pady = 10)

# key binding 
    def key(self, event):
        if(event.char == 'q' or event.char == 'Q'):
            self.vote_holder_vars[0].set(1)      
        if(event.char == 'w' or event.char == 'W'):
            self.vote_holder_vars[0].set(0)
        if(event.char == 'e' or event.char == 'E'):
            self.vote_holder_vars[1].set(1)       
        if(event.char == 'r' or event.char == 'R'):
            self.vote_holder_vars[1].set(0)
        if(event.char == 'a' or event.char == 'A'):
            self.vote_holder_vars[2].set(1)       
        if(event.char == 's' or event.char == 'S'):
            self.vote_holder_vars[2].set(0)
        if(event.char == 'd' or event.char == 'D'):
            self.vote_holder_vars[3].set(1)       
        if(event.char == 'f' or event.char == 'F'):
            self.vote_holder_vars[3].set(0)
        if(event.char == 't' or event.char == 'T'):
            self.vote_holder_vars[4].set(1)       
        if(event.char == 'y' or event.char == 'Y'):
            self.vote_holder_vars[5].set(0)
                
        # if(self.t1.get()!="" and self.t2.get()!="" and self.t3.get()!="" and self.t4.get()!="" and self.t5.get()!=""):
        #     self.sum.set(eval(self.t1.get()+"+"+self.t2.get()+"+"+self.t3.get()+"+"+self.t4.get()+"+"+self.t5.get())) 
        # Calculating sum
        sum = 0
        for i in self.vote_holder_vars:
            sum += int(i.get())
        self.total.set(str(sum))
        if(self.total.get()<='2'):
            self.l6.config(bg = "red")
        else:
            self.l6.config(bg = "green")
        
    def continue_callable(self):
        value = list()
        for i in self.vote_holder_vars:
            value.append(int(i.get()))
            i.set('')
        value.append(int(self.total.get()))
        self.total.set('')
        self.l6.config(bg = 'yellow')  
        self.stage_instance.feed_update( self.photo_indices[self.transversed_photo], value)
        try:
            self.photo_indices[self.transversed_photo+1]
        except Exception:
            step.Steps(self.stage_instance.getDataFrame(),self.photo_indices)
        pass
        self.transversed_photo = self.transversed_photo+1





