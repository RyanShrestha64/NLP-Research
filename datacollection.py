import nltk
import pickle
from nltk.probability import ConditionalFreqDist
from nltk.tokenize import TweetTokenizer
import os
import re
#
# dic = ConditionalFreqDist()
# name = input('name?')
# with open("reversebigramdata/" + str(name) + "thbigramdatareverse.pickle", "wb") as f:
#     pickle.dump(dic, f)
#     f.close()
#
# quit()
century = input('Century?')

words = 0

# for filename in os.listdir('testingtexts'):
for filename in os.listdir(century + "thcenturytexts"):
    print(filename)
    tex = open(century + "thcenturytexts/" + filename, "r", encoding='utf8')
    # tex = open("testingtexts/" + filename, "r", encoding='utf8')
    text = re.sub(r'\[.*?\]', '', tex.read())
    text = re.search(r'(?<=[*]{5}).*?(?=[*]{5})', text.replace('_', '').replace('\n', ' ')).group()

    # replace = re.findall(r"@@\d{7}", text)
    # for i in replace:
    #     text = text.replace(i, "")
    # text = re.sub(r'<.!?>', '', re.sub('@ ', '', text))

    bg = nltk.bigrams
    tk = TweetTokenizer()
    print(len(tk.tokenize(text)))
    print('\n')
    bg_list = list(bg(nltk.pos_tag(tk.tokenize(text))))
    # for bgram in bg_list:
    #     print(bgram[0], bgram[1])
print(words)
quit()
    #
    # with open('bigramdata/' + century + 'thbigramdata.pickle', "rb") as f:
    #     bgdata = pickle.load(f)
    #     f.close()
    #
    # with open('reversebigramdata/' + century + 'thbigramdatareverse.pickle', "rb") as f:
    #     reversebgdata = pickle.load(f)
    #     f.close()
    #
    # for bgram in bg_list:
    #     if (bgram[0][1] != 'NNP') and (bgram[1][1] != 'NNP'):
    #         bgdata[bgram[0][0].lower()][bgram[1][0].lower()] += 1
    #         reversebgdata[bgram[1][0].lower()][bgram[0][0].lower()] += 1
    #
    # with open('bigramdata/' + century + "thbigramdata.pickle", "wb") as f:
    #     pickle.dump(bgdata, f)
    #     f.close()
    #
    # with open('reversebigramdata/' + century + "thbigramdatareverse.pickle", "wb") as f:
    #     pickle.dump(reversebgdata, f)
    #     f.close()