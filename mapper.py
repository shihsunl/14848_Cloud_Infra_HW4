#!/usr/bin/env python
  
# import sys because we need to read and write data to STDIN and STDOUT
import sys
valid_quality = [0, 1, 4, 5, 9]
invalid_temperature = [9999]
  
# reading entire line from STDIN (standard input)
for line in sys.stdin:
    # to remove leading and trailing whitespace
    line = line.strip()
    year_month_day = line[15:23]
    temperature = line[87:92]
    quality = line[92]

    int_temperature = int(temperature)
    int_quality = int(quality)

    #print("line:", line)
    #print("year_month_day:", year_month_day)
    #print("temperature:", int_temperature)
    #print("quality:", int_quality)

    if int_quality in valid_quality and int_temperature not in invalid_temperature:
        msg = '{}\t{}'.format(year_month_day, int_temperature)
        print (msg)
      

# head ncdc-data/data/1901 | python3 mapper.py


#hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -file mapper.py -mapper 'python mapper.py' -file reducer.py python reducer.py -input /data/* -output /OutputFolder

'''
hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
-files /code/mapper.py,/code/reducer.py \
-input /data/* \
-output /output \
-mapper 'python /code/mapper.py' \
-combiner 'python /code/reducer.py' \
-reducer 'python /code/reducer.py'


'''

