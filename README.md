# mailmetrics task

Build command:

    make build

Convert file command:
    
    make convert INPUT_FILE=./example_files/utf-8.txt OUTPUT_FILE=./example_files/output.txt

Examples:

    make convert INPUT_FILE=./example_files/utf-16.txt OUTPUT_FILE=./example_files/output.txt
    make convert INPUT_FILE=./example_files/cp1250.txt OUTPUT_FILE=./example_files/output.txt
    make convert INPUT_FILE=./example_files/cp1252.txt OUTPUT_FILE=./example_files/output.txt
    make convert INPUT_FILE=./example_files/us-ascii.csv OUTPUT_FILE=./example_files/output.txt

**Limitations**:

1. Used library charset-normalizer can only detect encodings with limited predictability. 
Wrong prediction results in wrong file contents after conversion.

2. If output folder does not exist the script won't work