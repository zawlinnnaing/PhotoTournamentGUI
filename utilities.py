def clear_screen(ui_root):
	print(ui_root)
	pack_children = ui_root.pack_slaves()
	grid_children = ui_root.grid_slaves()
	for i in pack_children:
		i.pack_forget()
	for i in grid_children:
		i.grid_remove()

def initialize_gobals():
	global data_global_scope
	data_global_scope = {
        'tournament_name' : '',
        'no_of_judges' : 0,
        'no_of_photos' : 0,
        'rootGlobalMaster' : None
    }