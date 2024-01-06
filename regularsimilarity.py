import pickle
from numpy import dot
from numpy.linalg import norm
from numpy.linalg import norm
import nltk
from nltk.tokenize import TweetTokenizer
from nltk import ConditionalFreqDist
import os
import re


sample_name = input('read file?')
with open("testingtexts/" + sample_name + '.txt', "r", encoding='utf8') as f:
    text = re.sub(r'\[.*?\]', '', f.read())
    f.close()
text = re.search(r'(?<=[*]{5}).*?(?=[*]{5})', text.replace('_', '').replace('\n', ' ')).group()

# with open(str(data_name) + ".pickle", 'rb') as g:
#     data_set = pickle.load(g)

bg = nltk.bigrams
tk = TweetTokenizer()
check_words = [1000, 3000, 10000, 25000]

b_list = list(bg(nltk.pos_tag(tk.tokenize(text))))

sample_set = ConditionalFreqDist()
reverse_sample_set = ConditionalFreqDist()

bg_count = 0
for count in check_words:
    print(str(count) + ' words' + '\n')
    for bgram in b_list:
        if (bgram[0][1] != 'NNP') and (bgram[1][1] != 'NNP') and bg_count < count:
            sample_set[bgram[0][0].lower()][bgram[1][0].lower()] += 1
            reverse_sample_set[bgram[1][0].lower()][bgram[0][0].lower()] += 1
            bg_count += 1
        elif bg_count > count:
            break

    print(bg_count)

    for filename in os.listdir("bigramdata"):
        print(filename[0:2] + 'th century similarity score:')
        with open('bigramdata/' + str(filename), 'rb') as f:
            data_set = pickle.load(f)
            f.close()
        count = 0
        word_list = []
        cosine_similarity_sum = 0
        for item in dict(sample_set):
            # if count > 100:
            #     break
            # else:
            data_dstrbtion = data_set[item]
            sample_dstrbtion = sample_set[item]
            data_vector = []
            sample_vector = []
            all_follows = dict(data_dstrbtion).keys() | dict(sample_dstrbtion).keys()
            for word in all_follows:
                data_vector.append(sample_dstrbtion[word])
                sample_vector.append(data_dstrbtion[word])
            # print(sample_vector)
            # print(data_vector)
            # print('\n')

            if norm(data_vector) == 0 or norm(sample_vector) == 0:
                pass
            else:
                cosine_similarity_sum += dot(data_vector, sample_vector)/(norm(data_vector)*norm(sample_vector))
            count += 1

        print(round(cosine_similarity_sum / count, ndigits=5))
    sample_set = ConditionalFreqDist()
    reverse_sample_set = ConditionalFreqDist()