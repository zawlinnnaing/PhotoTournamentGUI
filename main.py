import tinker as tk
import step_one as step

class main():
	def __init__(self):
		self.no_of_photo = 10
		self.stage = 3
		self.no_of_judge = 3
		self.current_stage = 1
		self.initialize_all_instances()

	def initialize_all_instances(self):
		root = tk.Tk()
		root.geometry("1600x800+0+0")
		root.title("Photo Voting")
		s1 = step.Step_One(root, self.current_stage, self.no_of_photo, self.no_of_judge)
		root.mainloop()


if __name__ == '__main__':
    main()
