# [simple-template-parser](simple_template_parser.py)

### This template parser replace tags on template with provided data and generate multi-outputs.

```
./simple_template_parser.py -h
usage:  [-h] -d DATA [-de DATA_ENCODING] [-dt DATA_TYPE]
        [-dtcsvd DATA_TYPE_CSV_DELIMITER] [-t TEMPLATE]
        [-te TEMPLATE_ENCODING] [-tft TEMPLATE_FILE_TAG] [-o OUTPUT]
        [-oe OUTPUT_ENCODING] [-ofp OUTPUT_FILE_PATTERN] [-iter]

optional arguments:
  -h, --help            show this help message and exit
  -d DATA, --data DATA  data file to process, with a json array
  -de DATA_ENCODING, --data-encoding DATA_ENCODING
                        data file encoding, default=UTF-8
  -dt DATA_TYPE, --data-type DATA_TYPE
                        data file type, defaul=json
  -dtcsvd DATA_TYPE_CSV_DELIMITER, --data-type-csv-delimiter DATA_TYPE_CSV_DELIMITER
                        csv data type delimiter, default=,
  -t TEMPLATE, --template TEMPLATE
                        template file to process, with keys to replace the
                        value
  -te TEMPLATE_ENCODING, --template-encoding TEMPLATE_ENCODING
                        template file encoding, default=UTF-8
  -tft TEMPLATE_FILE_TAG, --template-file-tag TEMPLATE_FILE_TAG
                        tag on data with the path to a template file to
                        process
  -o OUTPUT, --output OUTPUT
                        path to output file, prints the output only in the
                        file
  -oe OUTPUT_ENCODING, --output-encoding OUTPUT_ENCODING
                        output file encoding, default=UTF-8
  -ofp OUTPUT_FILE_PATTERN, --output-file-pattern OUTPUT_FILE_PATTERN
                        output file pattern, will generate many files as
                        entries. Outputs on path and parse the pattern with
                        data tags
  -iter, --iterate      When iterate over data file, needs to press a key to
                        continue
```


## [Template](samples/template-sample.txt)
[samples/template-sample.txt](samples/template-sample.txt)
```txt
${KEY}
some stuffs here
${OTHER_KEY}
```

## [JSON](samples/data-sample.json)
[samples/data-samples.json](samples/data-sample.json)
```json
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
```csv
KEY	OTHER_KEY
VALUE_KEY	VALUE_OTHER_KEY
OTHER_VALUE_KEY	OTHER_VALUE_OTHER_KEY

```

## [Expected output](samples/output-samples.txt)

[samples/output-samples.txt](samples/output-samples.txt)

```txt
VALUE_KEY
some stuffs here
VALUE_OTHER_KEY

OTHER_VALUE_KEY
some stuffs here
OTHER_VALUE_OTHER_KEY

```


## Example

#### 1 - JSON
```bash
./simple_template_parser.py -t samples/template-sample.txt -d samples/data-sample.json
```
#### 2 - CSV
```bash
./simple_template_parser.py -t samples/template-sample.txt -d samples/data-sample.csv -dt csv
```
#### 3 - JSON WITH OUTPUT
```bash
    ./simple_template_parser.py -t samples/template-sample.txt -d samples/data-sample.json -o samples/output-samples.txt
```

#### In this example the command will create a file with all entries.

##### 3.1 - Output file:
[samples/output-samples.txt](samples/output-samples.txt)

##### 3.2 - Content file:
```txt
VALUE_KEY
some stuffs here
VALUE_OTHER_KEY

OTHER_VALUE_KEY
some stuffs here
OTHER_VALUE_OTHER_KEY

```

#### 4 - JSON WITH OUTPUT FILE PATTERN
```bash
./simple_template_parser.py -t samples/template-sample.txt -d samples/data-sample.json -o samples/ -ofp 'output-samples-${KEY}.txt'
```
#### In this example the command will create a file for each entry on the ouput file path, replacing the pattern with data keys.

#### 4.1 - Files:

##### 4.1.1 - Output file:
[samples/output-samples-VALUE.txt](samples/output-samples-VALUE.txt)

##### 4.1.2 - Content file:
```txt
VALUE_KEY
some stuffs here
VALUE_OTHER_KEY

```

##### 4.2.1 - Output file:
[samples/output-samples-OTHER_VALUE.txt](samples/output-samples-OTHER_VALUE.txt)

##### 4.2.2 - Content file:
```txt
OTHER_VALUE_KEY
some stuffs here
OTHER_VALUE_OTHER_KEY

```

#### 5 - JSON WITH MULTI-TEMPLATE AND OUTPUT FILE PATTERN
```bash
./simple_template_parser.py -d samples/data-sample-multi-template.json -tft 'TEMPLATE_FILES' -o samples/ -ofp 'output-samples-${KEY}-${OTHER_KEY}.txt'
```
#### In this example the command will process every template on the array and create a ouput file for each entry, replacing the pattern with data keys.

##### 5.1 - Data file:

[samples/data-sample-multi-template.json](samples/data-sample-multi-template.json)
```json
[
    {
        "KEY": "VALUE",
        "OTHER_KEY": "VALUE_OTHER_KEY",
        "TEMPLATE_FILES":
          [
            "samples/template-sample.txt",
            "samples/template-other-sample.txt"
          ]
    },
    {
        "KEY": "OTHER_VALUE",
        "OTHER_KEY": "OTHER_VALUE_OTHER_KEY",
        "TEMPLATE_FILES":
          [
            "samples/template-sample.txt",
            "samples/template-another-sample.txt"
          ]
    }
]
```

##### 5.2 - Template files:

[samples/template-sample.txt](samples/template-sample.txt)
```txt
${KEY}
some stuffs here
${OTHER_KEY}

```

[samples/template-other-sample.txt](samples/template-other-sample.txt)
```txt
-------------HERE-IS-OTHER-SAMPLE-------------
${KEY} + ${OTHER_KEY}
----------------------------------------------
```
[samples/template-another-sample.txt](samples/template-another-sample.txt)
```txt
----------------------------------------------
                ANOTHER-SAMPLE                
----------------------------------------------
${OTHER_KEY}
${KEY}
${KEY}
${OTHER_KEY}
----------------------------------------------
                ANOTHER-SAMPLE                
----------------------------------------------
```

##### 5.3 - Output files:

[samples/output-samples-VALUE-VALUE_OTHER_KEY.txt](samples/output-samples-VALUE-VALUE_OTHER_KEY.txt)
```txt
VALUE
some stuffs here
VALUE_OTHER_KEY

-------------HERE-IS-OTHER-SAMPLE-------------
VALUE + VALUE_OTHER_KEY
----------------------------------------------
```

[samples/output-samples-OTHER_VALUE-OTHER_VALUE_OTHER_KEY.txt](samples/output-samples-OTHER_VALUE-OTHER_VALUE_OTHER_KEY.txt)
```txt
OTHER_VALUE
some stuffs here
OTHER_VALUE_OTHER_KEY

----------------------------------------------
                ANOTHER-SAMPLE                
----------------------------------------------
OTHER_VALUE_OTHER_KEY
OTHER_VALUE
OTHER_VALUE
OTHER_VALUE_OTHER_KEY
----------------------------------------------
                ANOTHER-SAMPLE                
----------------------------------------------
```