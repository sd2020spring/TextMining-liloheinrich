"""
Mini Project 3: Text Mining for Software Design Spring 2020
Markov text generator for political news headlines
@author Lilo Heinrich
"""

import re
import random
import pickle

def get_top_words(word_list, n, exclude_common_words):
    """ Take a list of words as input and return a list of the n most
    frequently occurring words ordered from most- to least- frequent.

    Args:
        word_list: [str] a list of words including all duplicates
        n: [int] number of words to return
        exclude_common_words: [bool] whether to exclude words such as 'with'
    Returns:
        [int] n most frequently occurring words ordered from most to least
    """
    d = dict()
    words_exclude = ['to','of','for','on','in','with','is','says','as','from',
            'be','he','by','will','that','more','are','his','has','up','or',
            'could','who','not','most','it','at','an','they','the','over','out',
            'and','after','was','under','a','but','might','getting','get']

    for word in word_list:
        include_word = exclude_common_words and word not in words_exclude
        if word[0].isalpha() and (include_word or not exclude_common_words):
            d[word.lower()] = d.get(word,0) + 1
    ordered = sorted(d.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)

    words = []
    for tup in ordered:
        if len(words) == n:
            break
        words.append(tup[0])
    return words

def process_text(text, chain_length):
    """ Compile the markov chain dictionary, starting points, and list of all
    words in the given text.

    Args:
        text: [string] all of the text to process as one headline per line
        chain_length: [int] the number of words in each grouping

    Returns:
        word_list: [list of strings] all words including duplicates in text
            (intentionally leaving case, punctuation, and special characters to preserve authenticity)
        word_dict: [dictionary] matches tuples of words of length chain_length
            to the list of words that follows each sequence including duplicates
            ex. {('I', 'have', 'a'), ['dog', 'cat', 'fish']}
        starters: [dictionary] the same format as word_dict, but for only the
            sequences that start each headline, used to pick a starting point for the chain
    """
    word_list = []
    starters = {}
    word_dict = {}
    for i in text:
        word_list += i.split()
        make_word_dict(starters, word_dict, i.split(), chain_length)
    return word_list, word_dict, starters

def make_word_dict(starters, word_dict, word_list, chain_length):
    """ Modifies two dictionary with keys that are tuples of all combinations of
    chain_length number of words that are found in order in word list, mapped to
    lists of which words were found to follow that sequence, including duplicates.
    The starters dictionary has all of the starting points, word_dict has everything else.

    Args:
        word_list: [list] a list of words in a text, in order
        chain_length: [int] number of words to group by

    Example:
        get_keys(['and','the','brown','fox','jumped','over','the','brown','dog'], 2):
        word_dict: {('the','brown'):['fox','dog'],('brown','fox'):['jumped']...}
        starters: {('and', 'the'), ['brown']}
    """
    for i in range(len(word_list)-chain_length):
        key = []
        for j in range(chain_length):
            key.append(word_list[i+j])

        if i == 0:
            val = starters.get(tuple(key), [])
            val.append(word_list[i+chain_length])
            starters[tuple(key)] = val
        else:
            val = word_dict.get(tuple(key), [])
            val.append(word_list[i+chain_length])
            word_dict[tuple(key)] = val

def generate_text(starters, word_dict, chain_length, num_words):
    """ Generates text randomly from the given dictionaries of word sequences.

    Args:
        word_dict: [dictionary] matches tuples of words of length chain_length
            to the list of words that follows each sequence including duplicates
            ex. {('I', 'have', 'a'), ['dog', 'cat', 'fish']}
        starters: [dictionary] the same format as word_dict, but for only the
            sequences that start each headline, used to pick a starting point for the chain
        chain_length: [int] number of words the dictionaries are grouped by
        num_words: [int] the number of words to cut off the generated text at

    Return:
        [string] the randomly generated text
    """
    key, val = random.choice(list(starters.items()))
    str = key[0]
    for i in range(1, chain_length):
        str += ' ' + key[i]
    for n in range(num_words-chain_length):
        if word_dict.get(key) != None:
            possibles = word_dict[key]
        elif word_dict.get(key) == None and starters.get(key) != None:
            possibles = starters[key]
        else:
            break
        # print('possibles:', possibles)

        rand = random.randint(0,len(possibles)-1)
        next_word = possibles[rand]
        str += ' ' + next_word
        next_key = []
        for i in range(1, chain_length):
            next_key.append(key[i])
        next_key.append(next_word)
        key = tuple(next_key)
        # print('key:', key)
    return str

def reload_headlines():
    """ Load up the text inside of the pickle files of news sites' headlines.

    Returns:
        [string] the headlines from all of the pickled sites compiled into one
            string, with each headline separated by new line characters
    """
    names = ['nytimes', 'wapo', 'fox', 'cnn', 'politico']
    text = []
    for i in names:
        reloaded = pickle.load(open('pickles/'+i+'.pickle', 'rb'))
        text += reloaded
    return text

if __name__== '__main__':
    # load up headlines
    chain_length = 1
    max_words = 20
    num_words = 15
    num_headlines = 15
    text = reload_headlines()

    # analyze headlines, compile the data structures necessary
    word_list, word_dict, starters = process_text(text, chain_length)

    # generate text using markov chains of length chain_length
    print('Fake headlines:')
    for i in range(num_headlines):
        headline = generate_text(starters, word_dict, chain_length, max_words)
        print(headline)
    print()

    # get top num_words number of words
    print('Top', num_words, 'words in the news:')
    print(get_top_words(word_list, num_words, False))
    print('Top', num_words, 'words in the news excluding common words:')
    print(get_top_words(word_list, num_words, True))
