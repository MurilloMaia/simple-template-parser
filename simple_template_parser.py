#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json
import csv
import codecs
import argparse
import textwrap

from string import Template

READ = 'r'
WRITE = 'w+'
DIV = '-----------------------------------'
output = None

def main():
    parser = argparse.ArgumentParser(
        prog='',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
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
            KEY\tKEY2
            VALUE_KEY\tVALUE_KEY2
            OTHER_VALUE_KEY\tOTHER_VALUE_KEY2
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

        ''')
        )

    parser.add_argument('-t', '--template', help='template file to process, with keys to replace the value', required=True)
    parser.add_argument('-te', '--template-encoding', help='template file encoding, default=UTF-8', default='UTF-8')
    parser.add_argument('-d', '--data', help='data file to process, with a json array', required=True)
    parser.add_argument('-de', '--data-encoding', help='data file encoding, default=UTF-8', default='UTF-8')
    parser.add_argument('-dt', '--data-type', help='data file type, defaul=json', default='json')
    parser.add_argument('-dtcsvd', '--data-type-csv-delimiter', help='csv data type delimiter, default=\\t', default='\t')
    parser.add_argument('-iter', '--iterate', help='When iterate over data file, needs to press a key to continue', action='store_true')
    parser.add_argument('-o', '--output', help='path to output file, prints the output only in the file')
    parser.add_argument('-oe', '--output-encoding', help='output file encoding, default=UTF-8', default='UTF-8')
    parser.add_argument('-ofp', '--output-file-pattern', help='output file pattern, will generate many files as entries. Outputs on path and parse the pattern with data tags')

    args = parser.parse_args()
    
    template = Template(codecs.open(args.template, READ, args.template_encoding).read())

    data = parseData(args)

    output = None

    if args.output and not args.output_file_pattern:
        output = codecs.open(args.output, WRITE, args.output_encoding)

    for p in data:
        if args.output_file_pattern:
            filename = Template(args.output_file_pattern).substitute(**p)
            if args.output:
                path = ''.join([args.output,'/'])
            else:
                path = './'
            output = codecs.open(''.join([path, filename]), WRITE, args.output_encoding)
            
        write(output, process_template(template, **p), args.iterate)

def parseData(args):
    parsers = {
        "json" : parseJson,
        "csv" : parseCsv
    }
    with codecs.open(args.data, READ, args.data_encoding) as file:
        return parsers[args.data_type](args, file)

def parseJson(args, file):
    return json.load(file)

def parseCsv(args, file):
    reader = csv.DictReader(file, delimiter=args.data_type_csv_delimiter)
    data = []        
    for row in reader:
        temp = {}
        for fieldname in reader.fieldnames:
            temp[fieldname] = row[fieldname]

        data.append(temp)

    return data

def write(output, parsed_content, iterate):
    if output:
        output.write(parsed_content)
        output.write('\n')

    else:
        print parsed_content

    if iterate:
        print 'press any key to continue.'
        raw_input();

def printSuccess():
    print Template(textwrap.dedent('''\

        ${DIV}
        Output generated with success!!!
        ${DIV}

    ''')).substitute({'DIV':DIV})

def process_template(template, **kwargs):
    return template.substitute(kwargs)

if __name__ == "__main__":
    main()