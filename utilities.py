def clear_screen(ui_root):
	print(ui_root)
	children_list = ui_root.pack_slaves()
	for i in children_list:
		i.pack_forget()

def initialize_gobals():
	global data_global_scope
	data_global_scope = {
        'tournament_name' : '',
        'no_of_judges' : 0,
        'no_of_photos' : 0,
        'rootGlobalMaster' : None
    }