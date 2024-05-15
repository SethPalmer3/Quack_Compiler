#!/bin/bash

source venv/bin/activate
python3 ./quack_front.py -r "$1" > ./tmp.txt

FILENAME="$(basename "$1")"
FILE="${FILENAME%.*}"
echo "$FILE"
touch "tiny_vm/OBJ/$FILE.json"
cd ./tiny_vm/
python3 assemble.py ../tmp.txt > "OBJ/$FILE.json"
# rm ../tmp.txt
./bin/tiny_vm "$FILE"

