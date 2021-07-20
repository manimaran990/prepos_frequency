import pandas as pd
import numpy as np
import glob
import os
import logging
import argparse
import re, regex, mmap

#logging config
logging.basicConfig(filename='error.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')

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
				raise Exception(f"{self.prep_file} file not found")
			else:
				with open(self.prep_file, 'r', encoding='utf-8-sig') as f:
					for line in f.readlines(): #skip first three lines
							prep_list.append(line.strip())
				return prep_list
		except Exception as e:
			print(str(e))
			logging.error(str(e))

	def csv_for_eachfile(self, data_df, file_list, outputdir):
		try:
			for file in file_list:
				fname = os.path.basename(file)
				tdf = pd.DataFrame(data_df[fname])
				tdf.reset_index(inplace=True)
				tdf.columns = ['word', 'count']
				tdf.set_index('word', inplace=True)
				tdf.to_csv(os.path.join(outputdir, fname+".csv"))
				print(f"{fname}.csv written")
				logging.info(f"{fname}.csv written")
		except Exception as e:
			print(str(e))
			logging.error(f"error occured {e}")


	def generate_report(self, type, outputdir):
		''' generate report file '''
		try:
				#create preposition list
				prep_list = self.get_prepos_list()

				data_dict = {} #data dictionary to hold all the data
				# read all the csv files from the directory and check for availability
				if not os.path.isdir(self.inputs_path):
						raise Exception(f"field is empty or {self.inputs_path} is not a directory")
				else:
						csv_inputs = glob.glob(f'{self.inputs_path}/*.txt')
						for prep in prep_list:
							data_dict[prep] = {} #add dictionary with preposition as key 
							for inp_file in csv_inputs:
									#read it as df
									with open(inp_file, 'r+') as f:
										data = mmap.mmap(f.fileno(), 0).read().decode('utf-8') # to read large file
										data_dict[prep][os.path.basename(inp_file)] = len(regex.findall(rf'\b{prep}\b', data, re.UNICODE))

						df = pd.DataFrame(data_dict).transpose() #create df and transpose the df
						prep_df = df[sorted(df.columns)] #sort by columns
						print("dataframe created: ")
						print(prep_df.head())

						#check whether you want csv for each file or not
						if outputdir is not None: # if it's not none
							#if output directory not found create one
							if not os.path.exists(outputdir):
								print(f"creating directory {outputdir}")
								os.mkdir(outputdir)
							self.csv_for_eachfile(prep_df, csv_inputs, outputdir)

						#write consolidated report
						if type == 'xlsx':
							prep_df.to_excel(self.output_fname)
						else: # if it is csv
							self.output_fname = 'result.csv' if self.output_fname == 'result.xlsx' else self.output_fname
							prep_df.to_csv(self.output_fname)
						print(f"results written to {self.output_fname}")
		except Exception as e:
				print(str(e))
				logging.error(f"{e}")

if __name__ == '__main__':
		parser = argparse.ArgumentParser(description='preposition frequency counter')
		parser.add_argument('prep_file', type=str, help='preposition filename')
		parser.add_argument('inputs_folder', type=str, help='folder contains csv files to read')
		parser.add_argument('--output_type', type=str, choices=['xlsx', 'csv'], default='xlsx', help="outpufile file type")
		parser.add_argument('--output_name', action='store', type=str, default='result.xlsx', nargs='?', help='output filename')
		parser.add_argument('--output_dir', action='store', type=str, help="make seperate csv files for each input")

		args= parser.parse_args()
		fc = Frequency_counter(args.prep_file, args.inputs_folder, args.output_name)
		fc.generate_report(args.output_type, args.output_dir)