#!/bin/bash
FILE_PATH=$1
if test -f "$FILE_PATH"; then
    FILE_NAME=$(basename $FILE_PATH)
    echo "$FILE_NAME exists."
    docker rm  -f  mailmetrics-encoding-converter
	  docker create --volume ./app:/app --name "mailmetrics-encoding-converter" "encoding-converter:latest" python main.py --input /data/input/$FILE_NAME
	  docker cp $FILE_PATH "mailmetrics-encoding-converter":/data/input/
	  docker start -a mailmetrics-encoding-converter
	  docker cp "mailmetrics-encoding-converter":/data/output/file.txt $2
else
    echo "$FILE_PATH does not exist."
fi
