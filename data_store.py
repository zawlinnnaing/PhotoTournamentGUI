import pandas as pd
import numpy as np
import tkinter as tk
import step_one as step


class StageChain:
	def __init__(self):
		self.current_stage = 1
		self.stages = np.array([])
		root = tk.Tk()
		root.geometry("1600x800+0+0")
		root.title("Photo Voting")
		s1 = step.Step_One(root, self.current_stage)
		root.mainloop()

	def stage_proceed(self, data):
		np.append(self.stages, data)


class Stage:
	def __init__(self):
		index = np.arange(1,51)
		columns = ['Judge1', 'Judge2', 'Judge3', 'Total']
		self.data = pd.DataFrame(index=index, columns=columns)
		self.review = np.array()

	def feed(self, photo_id, value):
		self.update(photo_id, value)

	def update(self, idx, value):
		self.data.loc[idx] = value


if __name__ == '__main__':
	stage_chain = StageChain()
