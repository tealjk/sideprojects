#!/bin/sh



file="/Users/junkim/Desktop/PythonTOexcel/stAGING/inputdata/dataexcel.xlsx"


 if [ -f "$file" ]

 then
     python createwb.py | python initExcel.py >> /Users/junkim/Desktop/PythonTOexcel/staging/arc/Doc-$(date +%Y-%m-%d_%H:%M).txt

     echo "done"

     else

         echo "Error the InputFile does not exist. Please place a file in the /staging/inputdata/"

 fi













