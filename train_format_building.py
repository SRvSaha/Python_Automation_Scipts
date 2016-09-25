#
#   @author      : SRvSaha
#   Filename     : train_format_building.py
#   Timestamp    : 15:38 24-September-2016 (Saturday)
#   Description  : Code for ANNOTATION of Train Data || CMEE-IL
#
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1) as f:
    annotated = f.readlines()
with open(file2) as f:
    raw = f.readlines()
f_out = open("annonated_output.txt", 'w')
output = []
for line in raw:
    words = []
    splitted_line = line.strip().rstrip('\n').split("\t")
    tag_ = splitted_line[0]
    splitted_words = (splitted_line[2].replace("\\n", ' ').replace(
        ".", ' .').replace("'", " ' ").replace("#", "# ").replace(",", ' , ').replace("  ", ' ').strip()).split(" ")
    for word in splitted_words:
        word = word.strip()
        words.append([word, 0])  # List of List
    # Logic for checking id from annotated
    tagged = []
    for item in annotated:
        if tag_ in item:
            # print(tag_)
            splitted_line = item.split("\t")
            tag = (splitted_line[2])[6:]
            entities = ((splitted_line[3])[3:].lstrip().rstrip()).split(" ")
            if(len(entities) == 1):
                tagged.append([entities[0], "B-"+tag])
                pass
            else:
                tagged.append([entities[0], "B-"+tag])
                for entity in entities[1:]:
                    tagged.append([entity, "I-"+tag])

    for item in words:
        for tag in tagged:
            if item[0] == tag[0]:
                item[1] = tag[1]
                break
    for item in words:
        output.append(item[0]+" "+str(item[1])+"\n")
    output.append("\n")
f_out.writelines(output)
print("Operation Successful :)")

