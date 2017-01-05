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
f_out = open("deepti_final.csv",'w')
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
