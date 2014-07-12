#!/bin/bash
echo "Caesar shift solver!"
python caesar.py shifts.txt
python wordrec.py shifts.txt ans.txt
cat ans.txt
echo "Answer stored in ans.txt, shifts stored in shifts.txt"
