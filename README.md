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