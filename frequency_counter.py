import pandas as pd
import numpy as np
import glob
import os
import logging
import argparse

#logging config
logging.basicConfig(filename='error.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

class Frequency_counter(object):
	''' class to count the frequency of preposisitions '''
	def __init__(self, prep_file, inputs_path, output_fname):
		self.prep_file = prep_file
		self.inputs_path = inputs_path
		self.output_fname = output_fname

	def get_prepos_list(self):
		''' get the list of preposition read from prepositions file '''
		try:
			prep_list = []
			if not os.path.exists(self.prep_file):
				raise Exception(f"{preposition_file} file not found")
			else:
				with open(self.prep_file, 'r') as f:
					for line in f.readlines(): #skip first three lines
							prep_list.append(line.strip().lower())
				return prep_list
		except Exception as e:
			print(str(e))
			logging.error(str(e))

	def generate_report(self):
		''' generate report file '''
		try:
				#create preposition df
				prep_list = self.get_prepos_list()
				prep_df = pd.DataFrame(prep_list, columns=['word'])
				# read all the csv files from the directory and check for availability
				if not os.path.isdir(self.inputs_path):
						raise Exception(f"field is empty or {self.inputs_path} is not a directory")
				else:
						csv_inputs = glob.glob(f'{self.inputs_path}/*.csv')
						for inp_file in csv_inputs:
								#read it as df
								file_name = os.path.basename(inp_file)
								tmp_df = pd.read_csv(inp_file)
								tmp_df = tmp_df.groupby(tmp_df['word'].str.lower()).sum()
								tmp_df_dict = tmp_df.to_dict()['count']
								prep_df[file_name] = prep_df.apply(lambda x: tmp_df_dict[x['word']] if x['word'] in tmp_df_dict.keys() else 0, axis=1)
						
						#write to excel file
						prep_df.set_index('word', inplace=True)
						prep_df.to_excel(self.output_fname)
						print(f"results written to {self.output_fname}")
		except Exception as e:
				print(str(e))
				logging.error(f"exception in {file_name}: exception {e}")

if __name__ == '__main__':
		parser = argparse.ArgumentParser(description='preposition frequency counter')
		parser.add_argument('prep_file', type=str, help='preposition filename')
		parser.add_argument('inputs_folder', type=str, help='folder contains csv files to read')
		parser.add_argument('--output_name', action='store', type=str, default='result.xlsx', nargs='?', help='output filename')

		args= parser.parse_args()
		fc = Frequency_counter(args.prep_file, args.inputs_folder, args.output_name)
		fc.generate_report()