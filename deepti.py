'''

#
#   @author      : SRvSaha
#   Filename     : deepti.py
#   Timestamp    : 15:52 18-January-2017 (Wednesday)
#   Description  : The script converts CSV file given in the format of

(a)
date1,long1,long2,long3.....
lat1, 1,2,3,...
lat2, 4,5,6,...
lat3, 7,8,9,...
.
.
.
date2,long1,long2,long3.....
lat1, 11,12,13,...
lat2, 14,15,16,...
lat3, 17,18,19,...
.
.
.

to this format :
(b)
date1,lat1,long1,1
date1,lat1,long2,2
date1,lat1,long2,3
date1,lat2,long1,4
.
.
.
date2,lat1,long1,11
date2,lat2,long1,12
date2,lat3,long1,13
...
date2,lat2,long3,16
date2,lat3,long1,17
date2,lat3,long2,18
....

INPUT : Formatted CSV file as (a)
OUTPUT : Formatted CSV file as (b)

Requirements : Python3

TO RUN : python3 deepti.py <INPUT.csv>
'''


import sys

records = []
with open(sys.argv[1]) as f:
    for record in f.readlines():
        records.append(record.strip().split(','))
date = []

for i, item in enumerate(records):
    item = item[0]
    if(len(item) == 8):
        date.append((item, i))
# print(date)
header = "DATE,LATITUDE,LONGITUDE,RAINFALL\n"
f_out = open("deepti_final.csv", 'w')
f_out.write(header)
for index in range(len(date) - 1):
    start = int(date[index][1])
    end = int(date[index + 1][1])
    for row in range(start + 1, end):
        for column in range(1, len(records[0])):
            # print(date[index][0], records[row][0], records[0][column], records[row][column])
            f_out.write(str(date[index][0]) + ',' + str(records[row][0]) + ',' +
                        str(records[0][column]) + ',' + str(records[row][column]) + '\n')

start = int(date[-1][1])
end = len(records)
for row in range(start + 1, end):
    for column in range(1, len(records[0])):
            # print(date[-1][0], records[row][0], records[0][column], records[row][column])
        f_out.write(str(date[-1][0]) + ',' + str(records[row][0]) + ',' +
                    str(records[0][column]) + ',' + str(records[row][column]) + '\n')
f_out.close()
print("Output Successful :)")
