import pandas as pd
import numpy as np
import glob
import os
import logging
import argparse

#logging config
logging.basicConfig(filename='error.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')


class Word_freq_maker(object):
	def __init__(self, input_file, iscasesensitive, output_name):
		self.input_file = input_file
		self.iscasesensitive = iscasesensitive
		self.output_name = output_name

	def generate_freqcsv(self):
		try:
			df = pd.read_csv(self.input_file, header=None) #read input file
			df.columns = ['word'] #set word as header
			if not self.iscasesensitive:
			  tdf = pd.DataFrame(df.groupby(df['word'].str.lower()).agg(['count'])).reset_index()
			else:
			  tdf = pd.DataFrame(df.groupby(df['word']).size()).reset_index()
			tdf.columns = ['word', 'count']
			tdf.to_csv(self.output_name, index=False)
			print(f"csv file generated! {self.output_name}")
		except Exception as e:
			logging.error(f"error occured {e}")


if __name__ == '__main__':
		parser = argparse.ArgumentParser(description='word frequency csv maker')
		parser.add_argument('input_file', type=str, help='input filename contains list of words')
		parser.add_argument('--casesensitive', action='store', type=bool, const=True, default=False, nargs='?', help='case sensitive operation ?')
		parser.add_argument('--output_name', action='store', type=str, default='result.xlsx', nargs='?', help='output filename')

		args= parser.parse_args()
		fc = Word_freq_maker(args.input_file, args.casesensitive, args.output_name)
		fc.generate_freqcsv()