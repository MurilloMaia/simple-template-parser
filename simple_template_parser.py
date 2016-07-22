#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json
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
            -----------------------------------


            File format:
            -----------------------------------
            [
                {"KEY": "VALUE"},
                {"KEY": "OTHER_VALUE"}
            ]
            -----------------------------------


            Expected outputs:
            -----------------------------------
            VALUE
            -----------------------------------
            OTHER_VALUE
            -----------------------------------

        ''')
        )

    parser.add_argument('-t', '--template', help='template file to process, with keys to replace the value', required=True)
    parser.add_argument('-te', '--template-encoding', help='template file encoding', default='UTF-8')
    parser.add_argument('-d', '--data', help='data file to process, with a json array', required=True)
    parser.add_argument('-de', '--data-encoding', help='data file encoding', default='UTF-8')
    parser.add_argument('-iter', '--iterate', help='When iterate over data file, needs to press a key to continue', action='store_true')
    parser.add_argument('-o', '--output', help='path to output file')
    parser.add_argument('-oe', '--output-encoding', help='output file encoding', default='UTF-8')

    args = parser.parse_args()
    
    template = Template(codecs.open(args.template, READ, args.template_encoding).read())

    with codecs.open(args.data, READ, args.data_encoding) as f:
        data = json.load(f)

    if args.output:
        global output
        output = codecs.open(args.output, WRITE, args.output_encoding)

    for p in data:
        write(process_template(template, **p), args.iterate)

    printSuccess()

def write(parsed_content, iterate):
    if output:
        output.write(DIV)
        output.write('\n')
        output.write(parsed_content)
        output.write('\n')

    else:
        print DIV
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
