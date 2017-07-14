# simple-template-parser

./simple_template_parser.py -h
usage:  [-h] -t TEMPLATE [-te TEMPLATE_ENCODING] -d DATA [-de DATA_ENCODING]
        [-dt DATA_TYPE] [-dtcsvd DATA_TYPE_CSV_DELIMITER] [-iter] [-o OUTPUT]
        [-oe OUTPUT_ENCODING] [-ofp OUTPUT_FILE_PATTERN]

Script that parse a template file and generate the output with data of data file.

Template format:
-----------------------------------
${KEY}
some stuffs here
${OTHER_KEY}

-----------------------------------

JSON file format:
-----------------------------------
[
    {"KEY": "VALUE"},
    {"KEY": "OTHER_VALUE"}
]
-----------------------------------

CSV file format:
-----------------------------------
KEY KEY2
VALUE_KEY VALUE_KEY2
OTHER_VALUE_KEY OTHER_VALUE_KEY2
-----------------------------------

Expected outputs:
-----------------------------------
VALUE_KEY
some stuffs here
VALUE_OTHER_KEY

OTHER_VALUE_KEY
some stuffs here
OTHER_VALUE_OTHER_KEY

-----------------------------------

Command Samples:

    JSON
    ./simple_template_parser.py -t samples/template-sample.txt -d samples/data-sample.json

    -----------------------------------

    CSV
    ./simple_template_parser.py -t samples/template-sample.txt -d samples/data-sample.csv -dt csv

    -----------------------------------

    WITH OUTPUT
    ./simple_template_parser.py -t samples/template-sample.txt -d samples/data-sample.json -o samples/output-samples.txt

    # IN THIS EXAMPLE THE COMMAND WILL CREATE A FILE WITH ALL ENTRIES

    # FILE:
    #   samples/output-samples.txt
    # CONTENT:
    #   VALUE
    #   some stuffs here
    #   VALUE_OTHER_KEY
    #   
    #   OTHER_VALUE
    #   some stuffs here
    #   OTHER_VALUE_OTHER_KEY
    #   

    -----------------------------------

    WITH OUTPUT FILE PATTERN
    ./simple_template_parser.py -t samples/template-sample.txt -d samples/data-sample.json -o samples/ -ofp 'output-samples-${KEY}.txt'

    # IN THIS EXAMPLE THE COMMAND WILL CREATE A FILE FOR EACH ENTRY

    # FILE:
    #   samples/output-samples-VALUE.txt
    # CONTENT:
    #   VALUE
    #   some stuffs here
    #   VALUE_OTHER_KEY
    #

    # FILE:
    #   samples/output-samples-OTHER_VALUE.txt
    # CONTENT:
    #   OTHER_VALUE
    #   some stuffs here
    #   OTHER_VALUE_OTHER_KEY
    #

    -----------------------------------

optional arguments:
  -h, --help            show this help message and exit
  -t TEMPLATE, --template TEMPLATE
                        template file to process, with keys to replace the
                        value
  -te TEMPLATE_ENCODING, --template-encoding TEMPLATE_ENCODING
                        template file encoding, default=UTF-8
  -d DATA, --data DATA  data file to process, with a json array
  -de DATA_ENCODING, --data-encoding DATA_ENCODING
                        data file encoding, default=UTF-8
  -dt DATA_TYPE, --data-type DATA_TYPE
                        data file type, defaul=json
  -dtcsvd DATA_TYPE_CSV_DELIMITER, --data-type-csv-delimiter DATA_TYPE_CSV_DELIMITER
                        csv data type delimiter, default=\t
  -iter, --iterate      When iterate over data file, needs to press a key to
                        continue
  -o OUTPUT, --output OUTPUT
                        path to output file, prints the output only in the
                        file
  -oe OUTPUT_ENCODING, --output-encoding OUTPUT_ENCODING
                        output file encoding, default=UTF-8
  -ofp OUTPUT_FILE_PATTERN, --output-file-pattern OUTPUT_FILE_PATTERN
                        output file pattern, will generate many files as
                        entries. Outputs on path and parse the pattern with
                        data tags
