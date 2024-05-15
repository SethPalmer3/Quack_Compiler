#!/bin/bash

python3 ./quack_front.py "$1" > ./tmp.txt

FILENAME="$(basename "$1")"
FILE="${FILENAME%.*}"
echo "$FILE"
touch "tiny_vm/OBJ/$FILE.json"
cd ./tiny_vm/
python3 assemble.py ../tmp.txt > "OBJ/$FILE.json"
./bin/tiny_vm "$FILE"
rm ../tmp.txt

