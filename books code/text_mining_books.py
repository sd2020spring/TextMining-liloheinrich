import string
import re
import random
import pickle

def get_words(str):
    """
    Return a list of words in str split by whitespace.
    Args:
        str: [str] a string to find all words in
    Return:
        [list] a list of all the words in str as strings
    """
    return str.split()

def get_top_words(word_list, n):
    """ Take a list of words as input and return a list of the n most
    frequently-occurring words ordered from most- to least-frequent.
    Args:
        word_list: [str] a list of words
        n: [int] number of words to return
    Returns: [int] n most frequently occurring words ordered from most to least
    """
    d = dict()
    for word in word_list:
        d[word] = d.get(word,0) + 1
    ordered = sorted(d.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)

    words = []
    for tup in ordered:
        if len(words) == n:
            break
        words.append(tup[0])
    return words

def get_word_dict(word_list, m):
    """ Returns a dictionary with keys that are tuples of all combinations of
    m number of words that are found in order in word list mapped to values of
    lists of which words were found to follow that sequence, including duplicates.
    Args:
        word_list: [list] a list of words in order
        m: [int] number of words to group by
    Returns:
        [dict] a dictionary of tuples of word sequences to lists of words that
            follow those sequences in word_list
    Example:
        get_keys(['the','brown','fox','jumped','over','the','brown','dog'], 2):
        >>> {('the','brown'):['fox','dog'],('brown','fox'):['jumped']...}
    """
    word_dict = {}
    for i in range(len(word_list)-m):
        key = []
        for j in range(m):
            key.append(word_list[i+j])

        if word_dict.get(tuple(key)) == None:
            word_dict[tuple(key)] = [word_list[i+m]]
        else:
            word_dict[tuple(key)].append(word_list[i+m])
    return word_dict

def analyze_word_dict(word_dict):
    total_possibles = 0
    mult_possibles = 0
    items = word_dict.items()

    for k, v in items:
        total_possibles += len(v)
        if len(v) > 1:
            mult_possibles += 1

    # print('avg options per step:', round(total_possibles/len(items), 2))
    # print('percent multi-choice:', round(mult_possibles/len(items)*100, 2))
    return total_possibles/len(items), mult_possibles/len(items)*100

def generate_text(word_dict, m, num_words):
    total_possibles = 0
    mult_possibles = 0

    key, val = random.choice(list(word_dict.items()))
    str = key[0]
    for i in range(1, m):
        str += ' ' + key[i]

    for n in range(num_words-m):
        possibles = word_dict[key]
        # print('possibles:', possibles)

        total_possibles += len(possibles)
        if len(possibles) > 1:
            mult_possibles += 1

        rand = random.randint(0,len(possibles)-1)
        next_word = possibles[rand]
        # print('next_word:', next_word)

        str += ' ' + next_word
        # print('str:', str)

        next_key = []
        for i in range(1, m):
            next_key.append(key[i])
        next_key.append(next_word)
        key = tuple(next_key)
        # print('key:', key)
    return str, total_possibles, mult_possibles

def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i + j < len1 and string1[i + j] == string2[j]):
                match += string2[j]
            else:
                if (len(match) > len(answer)): answer = match
                match = ""
    return answer

# Load data from a file (will be part of your data processing script)
input_file = open('all_books.pickle', 'rb')
reloaded_copy_of_texts = pickle.load(input_file)
word_list = get_words(reloaded_copy_of_texts)
print('number of keys:', len(word_list))

top_n = 20
top_words = get_top_words(word_list, top_n)
print('top', top_n, 'words:', top_words)

# m = 3
# word_dict = get_word_dict(word_list, m)
# print('dictionary:', word_dict)
# num_words = 100
# str, total_possibles, mult_possibles = generate_text(word_dict, m, num_words)
# analyze_word_dict(word_dict)
# print(num_words, 'words of Markov text generation with', m, 'word connections:\n', str)
# print('avg options per step:', round(total_possibles/num_words, 2))
# print('percent multi-choice:', round(mult_possibles/num_words*100, 2), '%\n')
# print()


a = []
p = []
aa = []
pp = []
for m in range(1,10):
    # print(m)
    word_dict = get_word_dict(word_list, m)
    # print('dictionary:', word_dict)
    num_words = 100
    str, total_possibles, mult_possibles = generate_text(word_dict, m, num_words)
    a0, p0 = analyze_word_dict(word_dict)
    a.append(a0)
    p.append(p0)
    print(m, ':', str)
    aa.append(total_possibles/num_words)
    pp.append(mult_possibles/num_words*100)
    print()

print('avg options per step by m:', a)
print('percent multi-choice by m:', p)
print('avg options per step by m generated:', aa)
print('percent multi-choice by m generated:', pp)

import matplotlib
import matplotlib.pyplot as plt

# fig, axs = plt.subplots(2, 2)
fig, axs = plt.subplots()
x = [i for i in range(1,10)]
# axs[0, 0].plot(x, a)
# axs[0, 0].set_title('avg options per step')
# axs[0, 1].plot(x, p, 'tab:orange')
# axs[0, 1].set_title('percent multi-choice')
# axs[1, 0].plot(x, aa, 'tab:green')
# axs[1, 0].set_title('avg options per step generated')
# axs[1, 1].plot(x, pp, 'tab:red')
# axs[1, 1].set_title('percent multi-choice generated')

axs.plot(x, p)
axs.plot(x, pp)
axs.set_title('percent multi-choice')
plt.show()

""" ways to measure uniqueness of markov text generation:
- longest copied sequence
- percent of generated text that matches the longest copied sequence
- total options / total words generated
- % of steps with multiple option divergence

How to improve word separation ideas???
- include punctuation
- remove punctuation
- leave punctuation

- lowercase all
- don't lowercase all

- try different types of texts
"""

# word_string = ' '.join(word_list)
# substr = longestSubstringFinder(word_string, str)
# print('longest substring:', substr)
# print('percent word match:', round(len(substr.split())/num_words*100, 2), '%\n')
