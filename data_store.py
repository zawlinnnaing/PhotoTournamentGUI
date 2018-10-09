import pandas as pd
import numpy as np
import tkinter as tk
import entry_view
import utilities
from individual_step import individual_step 

class StageChain:
	def __init__(self):
		self.current_stage = 1
		self.no_of_judges = utilities.data_global_scope['no_of_judges']
		self.current_photo_count = utilities.data_global_scope['no_of_photos']
		self.stages = np.array([])
		self.stage_initialize()

	def stage_initialize(self):
		threshold = 0
		vote_protocol = 'boolean'
		if self.current_stage == 1:
			threshold = self.no_of_judges/2
			vote_protocol = 'boolean'
		elif self.current_stage == 2:
			threshold = 23 
			vote_protocol = '357'
		elif self.current_stage == 3: 
			threshold = 25; 
			vote_protocol = '357'
		elif self.current_stage == 4:
			threshold = 27
			vote_protocol = '357'
		Stage(self.current_stage, self.no_of_judges, self.current_photo_count)


class Stage:
	def __init__(self, stage_no, no_of_judges, current_photo_count):
		self.stage_no = stage_no
		self.no_of_judges = no_of_judges
		self.current_photo_count = current_photo_count
		self.data = self.create_dataframe()
		# self.review = np.array()
		self.current_photos_indices = np.array(self.data.index.tolist())
		print('stage initialized')
		individual_step( self, 1, self.current_photos_indices)

	def feed_update(self, photo_id, value):
		self.data.loc[photo_id] = value
	
	def create_dataframe(self):
		index = np.arange(1, self.current_photo_count)
		columns = list()
		for i in range(self.no_of_judges):
			columns.append('judge'+str(i+1))
		data = pd.DataFrame(index=index, columns=columns)	
		return data