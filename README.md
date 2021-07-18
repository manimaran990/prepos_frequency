preposition frequency counter
============================

install requirements:
---------------------
works on python3

pip3 install -r requirements.txt

help
----

python frequency_counter.py -h

usage: frequency_counter.py [-h] [--output_name [OUTPUT_NAME]]
                            prep_file inputs_folder

preposition frequency counter

positional arguments:
  prep_file             preposition filename
  inputs_folder         folder contains csv files to read

optional arguments:
  -h, --help            show this help message and exit
  --output_name [OUTPUT_NAME]
                        output filename


sample run:
---------
(without optional parameter --output_name)

python frequency_counter.py Prepositions_list..txt inputs/
results written to result.xlsx

(with optinoal parameter)

python frequency_counter.py Prepositions_list..txt inputs/ --output_name 'new_result.xlsx'
results written to new_result.xlsx



word frequency csv maker
========================


~/prepos_frequency$ python freq_csv_maker.py -h
usage: freq_csv_maker.py [-h] [--casesensitive [CASESENSITIVE]]
                         [--output_name [OUTPUT_NAME]]
                         input_file

word frequency csv maker

positional arguments:
  input_file            input filename contains list of words

optional arguments:
  -h, --help            show this help message and exit
  --casesensitive [CASESENSITIVE]
                        case sensitive operation ?
  --output_name [OUTPUT_NAME]
                        output filename


usage:
======
for case-insensitive opeartion:
---------------------------- 
~/prepos_frequency$ python freq_csv_maker.py ambe1.txt --output_name 'no_case_sensitive.txt'
csv file generated! no_case_sensitive.txt

~/prepos_frequency$ grep -E '^kuru,' no_case_sensitive.txt
kuru,4

for case-sensitive opeartion: (just add --casesenstive switch in the argument)
----------------------------

~/prepos_frequency$ python freq_csv_maker.py ambe1.txt --casesensitive --output_name 'case_sensitive.txt'
csv file generated! case_sensitive.txt

~/prepos_frequency$ grep -iE '^kuru' case_sensitive.txt
kUrU,1
kUrUnYis,1
kUrUnYisutanY,1
kUrUvukku,1
kUrUvukkuk,1
kUru,1
kUrufkalY,1
kUruvil,1
kurU,1
kurUp,1
kurUppAka,1
kurUs,1
kurUt,1
kurUyis,1
kuru,1
kurukkalY,1
kurumArkalY,1
kurup,1
kuruvikUttE,1


count test:
=======
~/prepos_frequency$ wc -l ambe1.txt
32302 ambe1.txt
~/prepos_frequency$ wc -l case_sensitive.txt
32303 case_sensitive.txt
~/prepos_frequency$ wc -l no_case_sensitive.txt
31802 no_case_sensitive.txt