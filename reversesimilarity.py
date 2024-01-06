import pickle
from numpy import dot
from numpy.linalg import norm
import nltk
from nltk.tokenize import TweetTokenizer
from nltk import ConditionalFreqDist
import os
import re


sample_name = input('read file?')
tex = open("testingtexts/" + sample_name + '.txt', encoding='utf8')
text = re.sub(r'\[.*?\]', '', tex.read())
text = re.search(r'(?<=[*]{5}).*?(?=[*]{5})', text.replace('_', '').replace('\n', '')).group()

# with open(str(data_name) + ".pickle", 'rb') as g:
#     data_set = pickle.load(g)

bg = nltk.bigrams
tk = TweetTokenizer()

b_list = list(bg(nltk.pos_tag(tk.tokenize(text))))

sample_set = ConditionalFreqDist()
reverse_sample_set = ConditionalFreqDist()

for bgram in b_list:
    if (bgram[0][1] != 'NNP') and (bgram[1][1] != 'NNP'):
        sample_set[bgram[0][0].lower()][bgram[1][0].lower()] += 1
        reverse_sample_set[bgram[1][0].lower()][bgram[0][0].lower()] += 1

for filename in os.listdir("reversebigramdata"):
    print(filename[0:2] + 'th century similarity score:')
    with open('reversebigramdata/' + str(filename), 'rb') as f:
        data_set = pickle.load(f)
        f.close()
    count = 0
    word_list = []
    cosine_similarity_sum = 0
    for item in dict(sample_set):
        data_dstrbtion = data_set[item]
        sample_dstrbtion = reverse_sample_set[item]
        data_vector = []
        sample_vector = []
        all_follows = dict(data_dstrbtion).keys() | dict(sample_dstrbtion).keys()
        for word in all_follows:
            data_vector.append(sample_dstrbtion[word])
            sample_vector.append(data_dstrbtion[word])

        if norm(data_vector) == 0 or norm(sample_vector) == 0:
            pass
        else:
            cosine_similarity_sum += dot(data_vector, sample_vector)/(norm(data_vector)*norm(sample_vector))
        count += 1

    print(round(cosine_similarity_sum / count, ndigits=5))