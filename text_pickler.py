import pickle
import requests
import re

# 12 big news sites' politics pages:

# https://www.nytimes.com/section/politics
nytimes = requests.get('https://www.nytimes.com/section/politics').text
string = str(nytimes)
match = re.findall("==.headline\":{\"default\":\"(.*?)\"", string)
match = match[3:]
print('nytimes', len(match), match)
f = open('pickles/nytimes.pickle', 'wb')
pickle.dump(match, f)
f.close()

# https://www.washingtonpost.com/politics/?nid=top_nav_politics
wapo = requests.get('https://www.washingtonpost.com/politics/?nid=top_nav_politics').text
string = str(wapo)
match = re.findall("itemprop=\"url\">(.*?)</a></h2>", string)
print('wapo', len(match), match)
f = open('pickles/wapo.pickle', 'wb')
pickle.dump(match, f)
f.close()

# https://www.foxnews.com/politics
fox = requests.get('https://www.foxnews.com/politics').text
string = str(fox)
match = re.findall("\"title\":\"(.*?)\"", string)
res = []
for i in match:
    if i not in res and len(i) >= 15:
        res.append(i)
match = res
print('fox', len(match), match)
f = open('pickles/fox.pickle', 'wb')
pickle.dump(match, f)
f.close()

# https://www.cnn.com/politics
cnn = requests.get('https://www.cnn.com/politics').text
string = str(cnn)
match = re.findall("\"headline\":\"(.*?)\"", string)
res = []
for i in match:
    if i not in res and len(i) >= 15:
        res.append(i)
match = res
print('cnn', len(match), match)
f = open('pickles/cnn.pickle', 'wb')
pickle.dump(match, f)
f.close()

# https://www.politico.com/politics
politico = requests.get('https://www.politico.com/politics').text
string = str(politico)
match = re.findall("<p>(.*?)</p>", string)
res = []
for i in match:
    if i not in res and len(i) >= 16:
        res.append(i)
match = res
print('politico', len(match), match)
f = open('pickles/politico.pickle', 'wb')
pickle.dump(match, f)
f.close()

# https://www.npr.org/sections/politics/
# https://www.breitbart.com/politics/
# https://www.nbcnews.com/politics
# https://www.cbsnews.com/politics
# https://www.wsj.com/news/politics
# https://www.bostonglobe.com/nation/politics/?p1=BGHeader_MainNav
# https://www.huffpost.com/news/politics

for i in match:
    print(i)
print()
