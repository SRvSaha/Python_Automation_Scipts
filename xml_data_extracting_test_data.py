#
#   @author      : SRvSaha
#   Filename     : xml_data_extracting.py
#   Timestamp    : 13:49 12-Aug-2016 (Sunday)
#   Description  : Given a XML file, this script extracts the value of elements || For TEST data
#   Requirement  : Python3
#

"""Extract the `value` element from the XML tree, if it exists."""


from xml.etree import ElementTree as ET
import sys

filename = sys.argv[1]
with open(filename) as f:
  xml = f.read().strip()
output = ""
pID = []
root = ET.fromstring(xml).find('Corpus')
for child in root:
  for attrib in (child.attrib).keys():
    if attrib == 'pID':
      # print(child.attrib.get(attrib))
      pID.append(child.attrib.get(attrib))
Language = ET.fromstring(xml).find('Corpus/Language')
Sentence1 = ET.fromstring(xml).findall('Corpus/Paraphrase/Sentence1')
Sentence2 = ET.fromstring(xml).findall('Corpus/Paraphrase/Sentence2')
Class = ET.fromstring(xml).findall('Corpus/Paraphrase/Class')
# print(Sentence1.text,Sentence2.text,Class.text,Language.text,sep ="\t") For single data
for i in range(len(Class)):
  # print(pID[i],(Sentence1[i]).text,(Sentence2[i]).text,(Class[i]).text,Language.text,sep ="\t")
  output += pID[i]+"\t"+(Sentence1[i]).text +"\t"+ (Sentence2[i]).text +"\t"+ Language.text + "\n"

filename = filename[:-4] + "_output.txt"
with open(filename,'w') as f:
  f.write(output)
print("Operation Sucessful :)")
