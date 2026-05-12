#!/bin/bash

read -p "Enter student marks: " marks

if [ $marks -ge 90 ]; then
    echo "Grade A"

elif [ $marks -ge 75 ]; then
    echo "Grade B"

elif [ $marks -ge 50 ]; then
    echo "Grade C"

else
    echo "Grade Fail"
fi
