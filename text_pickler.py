import pickle
import requests
import re

def pickle_it(filename, link, regex, method):
    """

    Args:
        link: [string] the link to the webpage to read
        regex: the regular expression to use for the 'findall' function
        filename: [string] filename to save pickle file as
        method: [int] 0/1/2 - signals which method of processing the 'findall' result to use
    """
    nytimes = requests.get(link).text
    string = str(nytimes)
    match = re.findall(regex, string)
    if method == 1:
        match = match[3:]
    elif method == 2:
        res = []
        for i in match:
            if i not in res and len(i) >= 15:
                res.append(i)
        match = res
    print(filename, len(match), match)
    f = open('pickles/'+filename+'.pickle', 'wb')
    pickle.dump(match, f)
    f.close()

info = [['nytimes', 'https://www.nytimes.com/section/politics', "==.headline\":{\"default\":\"(.*?)\"", 1],
        ['wapo', 'https://www.washingtonpost.com/politics/?nid=top_nav_politics', "itemprop=\"url\">(.*?)</a></h2>", 0],
        ['fox', 'https://www.foxnews.com/politics', "\"title\":\"(.*?)\"", 2],
        ['cnn', 'https://www.cnn.com/politics', "\"headline\":\"(.*?)\"", 2],
        ['politico', 'https://www.politico.com/politics', "<p>(.*?)</p>", 2]]

# https://www.npr.org/sections/politics/
# https://www.breitbart.com/politics/
# https://www.nbcnews.com/politics
# https://www.cbsnews.com/politics
# https://www.wsj.com/news/politics
# https://www.bostonglobe.com/nation/politics/?p1=BGHeader_MainNav
# https://www.huffpost.com/news/politics

for i in info:
    pickle_it(i[0], i[1], i[2], i[3])
