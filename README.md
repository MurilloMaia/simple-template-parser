# [simple-template-parser](simple_template_parser.py)

### This template parser replace tags on template with provided data and generate multi-outputs.

```
./simple_template_parser.py -h
usage:  [-h] -t TEMPLATE [-te TEMPLATE_ENCODING] -d DATA [-de DATA_ENCODING]
        [-dt DATA_TYPE] [-dtcsvd DATA_TYPE_CSV_DELIMITER] [-iter] [-o OUTPUT]
        [-oe OUTPUT_ENCODING] [-ofp OUTPUT_FILE_PATTERN]

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
```


## [Template](samples/template-sample.txt)
[samples/template-sample.txt](samples/template-sample.txt)
```
${KEY}
some stuffs here
${OTHER_KEY}

```

## [JSON](samples/data-sample.json)
[samples/data-samples.json](samples/data-sample.json)
```
[
    {
        "KEY": "VALUE",
        "OTHER_KEY": "VALUE_OTHER_KEY"
    },
    {
        "KEY": "OTHER_VALUE",
        "OTHER_KEY": "OTHER_VALUE_OTHER_KEY"
    }
]

```

## [CSV](samples/data-sample.csv)
[samples/data-samples.csv](samples/data-sample.csv)
```
KEY	OTHER_KEY
VALUE_KEY	VALUE_OTHER_KEY
OTHER_VALUE_KEY	OTHER_VALUE_OTHER_KEY

```

## [Expected output](samples/output-samples.txt)

[samples/output-samples.txt](samples/output-samples.txt)

```
VALUE_KEY
some stuffs here
VALUE_OTHER_KEY

OTHER_VALUE_KEY
some stuffs here
OTHER_VALUE_OTHER_KEY

```


## Example

#### 1 - JSON
```
./simple_template_parser.py -t samples/template-sample.txt -d samples/data-sample.json
```
#### 2 - CSV
```
./simple_template_parser.py -t samples/template-sample.txt -d samples/data-sample.csv -dt csv
```
#### 3 - JSON WITH OUTPUT
```
    ./simple_template_parser.py -t samples/template-sample.txt -d samples/data-sample.json -o samples/output-samples.txt
```

#### In this example the command will create a file with all entries.

##### 3.1 - Output file:
[samples/output-samples.txt](samples/output-samples.txt)

##### 3.2 - Content file:
```
VALUE_KEY
some stuffs here
VALUE_OTHER_KEY

OTHER_VALUE_KEY
some stuffs here
OTHER_VALUE_OTHER_KEY

```

#### 4 - JSON WITH OUTPUT FILE PATTERN
```
./simple_template_parser.py -t samples/template-sample.txt -d samples/data-sample.json -o samples/ -ofp 'output-samples-${KEY}.txt'
```
#### In this example the command will create a file for each entry on the ouput file path, replacing the pattern with data keys.

#### 4.1 - Files:

##### 4.1.1 - Output file:
[samples/output-samples-VALUE.txt](samples/output-samples-VALUE.txt)

##### 4.1.2 - Content file:
```
VALUE_KEY
some stuffs here
VALUE_OTHER_KEY

```

##### 4.2.1 - Output file:
[samples/output-samples-OTHER_VALUE.txt]([samples/output-samples-OTHER_VALUE.txt)

##### 4.2.2 - Content file:
```
OTHER_VALUE_KEY
some stuffs here
OTHER_VALUE_OTHER_KEY

```