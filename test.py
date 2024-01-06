import os
import re
from nltk import word_tokenize

string = """*****Creating [6] the works from print editions not protected by U.S. copyright
law means that no one owns a [illustration: pig] _United_ _States_ copyright in these works,
so the Foundation (and you!)
*****"""

filename = input('file')

tex = open(filename, "r", encoding='utf8')
lines = tex.readlines()
new = open('../nthCenturyEnglish/testingtexts/silentspring,1962.txt', 'w', encoding='utf8')
for line in lines:
    if re.findall('\d[.]', line[0:2]) == []:
        new.write(line)
quit()
temp_count = 0
for line in lines:
    line = line.replace('\n', '')
    if re.findall('FEDERALIST No. \d+?', line) != []:
        temp_count += 10
    if temp_count > 0:
        temp_count -= 1
    else:
        new.write(line + '\n')

quit()
for line in lines:
    line = line.replace('\n', '')
    try:
        if line[-1] == '-':
            new.write(line[:-1])
        else:
            new.write(line + '\n')
    except IndexError:
        new.write('\n')

quit()
temp_count = 0
for line in lines:
    line = line.replace('\n', '')
    if re.findall('CHAPTER [XVI]+?[.]', line) != []:
        temp_count = 3
    if temp_count > 0:
        temp_count -=1
    else:
        new.write(line + '\n')
quit()
temp_count = 0
for line in lines:
    line = line.replace('\n', '')
    if line == 'JULIA GRANBY.' or line == 'ELIZA WHARTON.' or line == 'J. BOYER.' or  line == 'PETER SANFORD.' or line == 'LUCY FREEMAN.' or line == 'M. WHARTON.' or line == 'T. SELBY.' or line == 'S. RICHMAN.' or line == 'LUCY SUMNER.':
        temp_count = 8
    if temp_count > 0:
        temp_count -= 1
    else:
        new.write(line + '\n')
quit()
# for line in lines:
#     try:
#         line = line.replace('\n', '')
#         if line[-1] == ' ':
#             new.write(line[:-1] + '\n')
#         else:
#             print('damn')
#             new.write(line + '\n')
#     except:
#         new.write('\n')

# quit()
for line in lines:
    line = line.replace('\n', '')
    try:
        print(line[-1])
        if line[-1] == '¬':
            new.write(line[:-1])
        else:
            new.write(line + '\n')
    except:
        if not line.isdigit():
            new.write(line + '\n')
quit()
for line in lines:
    if re.findall('[XVI]+?[.]', line) == []:
        new.write(line)
quit()
# age of innocence

# print(re.findall(r'[*]{5}.*?[*]{5}', tex.read().replace('\n', '')))
# for line in lines:
#     if re.findall('[{].*?[}]', line) == []:
#         new.write(line)
# quit()
for line in lines:
    line = line.replace('\n', '')
    if len(word_tokenize(line)) > 2:
        try:
            print(line[-1])
            if line[-1] == '-':
                new.write(line[:-1])
            else:
                new.write(line + '\n')
        except:
            pass
quit()
for line in lines:
    write = True
    if re.findall("A[.]D[.]", line) != []:
        write = False
    else:
        for character in line:
            if character == '_':
                write = False
                break
    if write:
        new.write(line)

quit()

for line in lines:
    write = True
    if re.findall("' \d{2}", line) != []:
        write = False
    else:
        for character in line:
            if character == '•' or character == '■':
                write = False
                break
    if write:
        new.write(line)