import string
import re
import random
import pickle

def get_top_words(word_list, n, exclude_common_words):
    """ Take a list of words as input and return a list of the n most
    frequently-occurring words ordered from most- to least-frequent.
    Args:
        word_list: [str] a list of words
        n: [int] number of words to return
    Returns: [int] n most frequently occurring words ordered from most to least
    """
    d = dict()
    words_exclude = ['to','of','for','on','in','with','is','says','as','from','be','he','by','will','that','more','are','his','has','up','or','could','who','not','most','it','at','an','they','the','over','out','and','after','was','under','a']
    for word in word_list:
        if word[0].isalpha() and ((exclude_common_words and word not in words_exclude) or not exclude_common_words):
            d[word.lower()] = d.get(word,0) + 1
    ordered = sorted(d.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)

    words = []
    for tup in ordered:
        if len(words) == n:
            break
        words.append(tup[0])
    return words

def get_word_dict(starters, word_dict, word_list, chain_length):
    """ Returns a dictionary with keys that are tuples of all combinations of
    chain_length number of words that are found in order in word list mapped to values of
    lists of which words were found to follow that sequence, including duplicates.
    Args:
        word_list: [list] a list of words in order
        chain_length: [int] number of words to group by
    Returns:
        [dict] a dictionary of tuples of word sequences to lists of words that
            follow those sequences in word_list
    Example:
        get_keys(['the','brown','fox','jumped','over','the','brown','dog'], 2):
        >>> {('the','brown'):['fox','dog'],('brown','fox'):['jumped']...}
    """
    for i in range(len(word_list)-chain_length):
        key = []
        for j in range(chain_length):
            key.append(word_list[i+j])

        if i == 0:
            if starters.get(tuple(key)) == None:
                starters[tuple(key)] = [word_list[i+chain_length]]
            else:
                starters[tuple(key)].append(word_list[i+chain_length])
        else:
            if word_dict.get(tuple(key)) == None:
                word_dict[tuple(key)] = [word_list[i+chain_length]]
            else:
                word_dict[tuple(key)].append(word_list[i+chain_length])

def generate_text(starters, word_dict, m, num_words):
    key, val = random.choice(list(starters.items()))
    str = key[0]
    for i in range(1, m):
        str += ' ' + key[i]
    for n in range(num_words-m):
        if word_dict.get(key) != None:
            possibles = word_dict[key]
        elif word_dict.get(key) == None and starters.get(key) != None:
            possibles = starters[key]
        else:
            break
        # print('possibles:', possibles)

        rand = random.randint(0,len(possibles)-1)
        next_word = possibles[rand]
        # print('next_word:', next_word)

        str += ' ' + next_word
        next_key = []
        for i in range(1, m):
            next_key.append(key[i])
        next_key.append(next_word)
        key = tuple(next_key)
        # print('key:', key)
    return str

def reload_headlines():
    names = ['nytimes', 'wapo', 'fox', 'cnn', 'politico']
    text = []
    for i in names:
        reloaded = pickle.load(open('pickles/'+i+'.pickle', 'rb'))
        text += reloaded
    return text

if __name__== '__main__':
    text = reload_headlines()
    print('headlines:', text)

    chain_length = 1
    word_list = []
    starters = {}
    word_dict = {}
    for i in text:
        word_list += i.split()
        get_word_dict(starters, word_dict, i.split(), chain_length)

    print('dictionary:', word_dict)
    print('starters:', starters)
    print()

    print('fake headlines:')
    num_words = 15
    num_headlines = 15
    for i in range(num_headlines):
        print(generate_text(starters, word_dict, chain_length, num_words))
    print()

    n = 20
    print('Top', n, 'words in the news:')
    print(get_top_words(word_list, n, False))
    print('Top', n, 'words in the news excluding common words:')
    print(get_top_words(word_list, n, True))
