import pickle
import requests
import re
import string

def get_book(i):
    link = 'http://www.gutenberg.org/cache/epub/'+str(i)+'/pg'+str(i)+'.txt'
    text = requests.get(link).text
    text = text.replace('\n', ' ')
    arr = re.findall("START OF THIS PROJECT GUTENBERG EBOOK(.*?)END OF THIS PROJECT GUTENBERG EBOOK", text)
    if len(arr) == 1:
        text = arr[0]
        arr = re.findall("\*\*\*(.*?)\*\*\*", text)
        text = arr[0]
        print('text', i, ':', len(text))
        f = open('text'+str(i)+'.pickle', 'wb')
        pickle.dump(text, f)
        f.close()
    else:
        print('text', i, ': error')

def get_book_text(i):
    link = 'http://www.gutenberg.org/cache/epub/'+str(i)+'/pg'+str(i)+'.txt'
    text = requests.get(link).text
    text = text.replace('\n', ' ')
    arr = re.findall("START OF THIS PROJECT GUTENBERG EBOOK(.*?)END OF THIS PROJECT GUTENBERG EBOOK", text)
    if len(arr) == 1:
        text = arr[0]
        arr = re.findall("\*\*\*(.*?)\*\*\*", text)
        text = arr[0]
        print('text', i, ':', len(text))
        return text
    else:
        print('text', i, ': error')
        return ''

min = 1549
max = 49739
print('max num books:', max-min)
max = min + 20
# for i in range(min, max):
#     get_book(i)

text = ''
for i in range(min, max):
    text += get_book_text(i)
print(len(text))
f = open('all_books.pickle', 'wb')
pickle.dump(text, f)
f.close()
