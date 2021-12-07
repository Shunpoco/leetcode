#!/bin/bash

cat file.txt | if [[ $(wc -l $1) -ge 10 ]]; then head -10 file.txt | tail -1; else echo ""; fi
