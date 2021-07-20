preposition frequency counter
============================

install requirements:
---------------------
works on python3

pip3 install -r requirements.txt

help
----
~/prepos_frequency$ python frequency_counter.py -h
usage: frequency_counter.py [-h] [--output_type {xlsx,csv}]
                            [--output_name [OUTPUT_NAME]]
                            [--output_dir OUTPUT_DIR]
                            prep_file inputs_folder

preposition frequency counter

positional arguments:
  prep_file             preposition filename
  inputs_folder         folder contains csv files to read

optional arguments:
  -h, --help            show this help message and exit
  --output_type {xlsx,csv}
                        outpufile file type
  --output_name [OUTPUT_NAME]
                        output filename
  --output_dir OUTPUT_DIR
                        make seperate csv files for each input


sample run
------

with default parameters:
-----------

~/prepos_frequency$ python frequency_counter.py Prepositions_list..txt originaltextfile/
dataframe created:
results written to result.xlsx

to get the consolidated output as csv:
----------

~/prepos_frequency$ python frequency_counter.py Prepositions_list..txt originaltextfile/ --output_type csv --output_name 'consolidate_result.csv'
dataframe created:
results written to consolidate_result.csv
~/prepos_frequency$ head -5 consolidate_result.csv
,1.1.pdf.txt,1.2.pdf.txt,10_1.pdf.txt,10_2.pdf.txt,2.1.pdf.txt,2.2.pdf.txt,3.1.pdf.txt,3.2.pdf.txt,4.1.pdf.txt,4.2.pdf.txt,5.1.pdf.txt,5.2.pdf.txt,6.1.pdf.txt,6.2.pdf.txt,7.1.pdf.txt,7.2.pdf.txt,8_1.pdf.txt,8_2.pdf.txt,9_1.pdf.txt,9_2.pdf.txt,English_plus_1.pdf.txt,plus_2_english.pdf.txt
﻿about,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
above,0,0,15,5,3,1,3,3,1,4,8,3,3,3,14,10,10,7,9,11,23,13
according to,0,0,3,1,0,0,0,0,0,0,0,0,3,2,1,0,4,1,1,2,5,4
across,0,0,4,3,1,0,4,0,1,1,3,5,4,1,5,5,6,2,4,5,9,11 

to get seperate csv files for each input file (just add --output_dir parameter)
-----------

~/prepos_frequency$ python frequency_counter.py Prepositions_list..txt originaltextfile/ --output_type csv --output_name 'consolidate_result.csv' --output_dir outputs/
dataframe created:
1.1.pdf.txt.csv written
1.2.pdf.txt.csv written
10_1.pdf.txt.csv written
10_2.pdf.txt.csv written
2.1.pdf.txt.csv written
2.2.pdf.txt.csv written
3.1.pdf.txt.csv written
3.2.pdf.txt.csv written
4.1.pdf.txt.csv written
4.2.pdf.txt.csv written
5.1.pdf.txt.csv written
5.2.pdf.txt.csv written
6.1.pdf.txt.csv written
6.2.pdf.txt.csv written
7.1.pdf.txt.csv written
7.2.pdf.txt.csv written
8_1.pdf.txt.csv written
8_2.pdf.txt.csv written
9_1.pdf.txt.csv written
9_2.pdf.txt.csv written
English_plus_1.pdf.txt.csv written
plus_2_english.pdf.txt.csv written
results written to consolidate_result.csv
