# Markov Text Generation of Political News Headlines

## Project Overview
### Sources

    New York Times: https://www.nytimes.com/section/politics
    Fox News: https://www.foxnews.com/politics
    Washington Post: https://www.washingtonpost.com/politics/?nid=top_nav_politics
    CNN News: https://www.cnn.com/politics
    Politico: https://www.politico.com/politics

I deliberately chose wide-ranging and sometimes controversial news sources for variety.

### Libraries
* __requests__
  * To get the html code of these news sites.
* __re__
  * Split out the headlines using regular expressions by the surrounding tags or syntax identified. This proved slightly challenging, due to each site having a different format/language.
  * I learned a lot about regular expression syntax in trying to accurately filter out only headlines from a whole webpage where the code included escape characters, repeating sequences, etc.
* __pickle__
  * To condense the data and save it as a file which can be reloaded later.
* __random__
  * To pick random keys from the Markov chain dictionaries

## Implementation
### Dictionary data structures
The way that it encodes the Markov chain is that it first takes all of the headlines and turns them into a single string, separated by newline characters. Next, it processes the text, creating two dictionaries relating groupings of '*chain_length*' number of words to a list of the words that follow that grouping, including the duplicates for the ease of randomization. The first dictionary is the '*starters*', containing the groupings from the start of each line, and providing a starting point for generating text. The second is '*word_dict*', containing all of the rest. To create them, for each of the headlines, it adds the word at index [i+chain_length+1] to the list of words that follow the grouping preceding it [i, i+chain_length].  

Examples:
* process_text(text=['I have a dog', 'I have a cat', 'I have a fish'], chain_length=3)
  * word_list=['I', 'have', 'a', 'dog', 'I', 'have', 'a', 'cat', 'I', 'have', 'a', 'fish']
  * word_dict={}
  * starters={('I', 'have', 'a'): ['dog', 'cat', 'fish']})
* make_word_dict(starters={}, word_dict={}, text=['the','red','fox','jumped','over','the','dog'], chain_length=2)
  * word_dict={('red','fox'): ['jumped'], ('fox', 'jumped'): ['over'], ('jumped', 'over'): ['the'], ('over', 'the'): ['dog']}
  * starters={('the','red'): ['fox']}

### Generating text
Next, to randomly generate text, it traverses through '*word_dict*' and '*starters*'. First, it picks a random item from '*starters*' and adds the first word in the key's tuple to the randomly generated string. Next, it picks a random word from the list of options of words that follow that key. Then it updates the key tuple, effectively shifting over all of the words to the left, getting rid of the oldest and adding the one picked in the previous step. It repeats the previous two steps either until there are no values to choose from or it hits the maximum words limit.  

Example:
* generate_text(starters={('Trump', 'thinks', 'golf'): ['is']}, word_dict={('thinks', 'golf', 'is'):['the'], ('golf', 'is', 'the'): ['best']}, chain_length=3, max_words=10)
  * 'Trump thinks golf is the best'

### Word frequency
It also creates a list of all words including duplicates, in order, that is used to calculate the most frequent words by going through the whole list and adding 1 to the value corresponding to the dictionary key of that word. Then the dictionary is sorted by its' values and iterated through to grab the top n keys and append them to a list.  

Examples:
* get_top_words(word_list=['hi', 'my', 'name', 'is', 'steve', 'hi', 'my', 'name', 'is', 'not', 'amon'], num_words=4, exclude_common_words=False)
  * ['name', 'my', 'is', 'hi']
* get_top_words(word_list=['hi', 'my', 'name', 'is', 'steve', 'hi', 'my', 'name', 'is', 'not', 'amon'], num_words=4, exclude_common_words=True)
  * ['name', 'hi', 'steve', 'amon']

### Design Decision
One decision that I made is that I deliberately left case, punctuation, and special characters in for everything except the word frequency count because it helped retain the original meaning and produce authentic and grammatically correct headlines while avoiding the issue of figuring out how to code out punctuation and capitalization correction. The drawback in doing so was that I lost some possible word connections, decreasing the options available for text generation for example if the case didn't match, etc. The other option that I didn't pursue because it added a bit more complexity was to try separating punctuation into its' own tokens, expanding the available options - ex. 'I tripped, said the man.' becoming word_list = ['I', 'tripped', ',', 'said', 'the', 'man', '.']. However, that has the potential to allow for too much or too little punctuation, leading to run on sentences or fragments.

## Results
### Fake News

    How the level of Aircraft Carrier Pleads for investigation
    Both public health and voting-rights experts say there's little time for customers to Power Shift
    Both public health experts and hundreds of aircraft carrier hit by coronavirus is affecting US
    The FBI's surveillance.
    US economy shuttered to treat Covid-19, pitching him head-to-head with public health and provide models
    Analysis: Trump's interview with Sean Hannity
    Fox Nation hosts have reasons to talk to him head-to-head with anti-environment voting procedures
    5 takeaways from coronavirus briefings
    Fauci says he won't allow Democrats "to achieve unrelated policy items they wouldn't otherwise"
    Doctors disagree with coronavirus stimulus checks
    How two weeks changed America, brace for six months under a strict quarantine after intensive
    4 takeaways from Congress to expand in praising Trump wildly exaggerates 1918 flu mortality rate
    History's verdict on hold -- White House reassessing deal bars Trump's poll surge last?
    NYPD to hear case of the Country: 2 Sets of Netflix stock.
    Lilly Ledbetter, advocate for female VP pledge

These are somewhat hand-picked, 15 out of 30 generated. I also took the liberty of completing quotes and deleting some run on endings.

### Word Frequency
Top 20 words in the news (on 3/31/20):
* ['to', 'of', 'for', 'on', 'in', 'with', 'is', 'says', 'as', 'from', 'be', 'he', 'during', 'response', 'by', 'will', 'that', 'pandemic', 'more', 'are']

Top 20 words in the news excluding common words:
* ['during', 'response', 'pandemic', 'need', 'amid', 'outbreak', 'governor', 'federal', 'public', 'political', 'home', 'help', 'guidelines', 'crisis', 'coronavirus,', 'bill', 'administration', 'virus', 'trillion', 'stimulus']

This appears to make a lot of sense, because I have recently read a lot about *federal* and *governors'* *response* to the *epidemic*, things people *need* *amid* the *coronavirus* *outbreak*, and the *administration* releasing a *bill* for *trillions* of dollars of economic *stimulus* in the US.

## Alignment
Political news currently seems to be a very relevant topic and I found the idea of creating 'fake news' interesting. I wanted to see how easy/hard it would be to come up with my own fake news headlines that draw on the buzzwords circulating in the actual news currently.

In the process of trying to create fake news, I found out that Markov chains of news headlines that are longer than one word didn't usually have many diverging options. This may be because certain keywords just tend to follow each other in the English language or when talking about a certain topic, no matter the author/source, especially in short sentences where the goal is to get the point across and there is not much room to elaborate. This limited my random headline generation to work with single word chains, increasing the likelihood of rapid topic changes and grammatical errors throughout the sentence, making most of them nonsensical. It was slightly disappointing as I had expected to be able to utilize the functionality I had written for longer chains to improve my results. Possibly if I was able to gather a lot more headlines, or instead shifted to generating sentences from articles, I would have better luck with this.

However, I was able to have a measure of success with this implementation, at least producing headlines which, if filtered by hand, are readable. Of course, I see a lot of key words or buzzwords thrown together in some headlines, such as 'pandemic', 'Trump', 'Congress', etc. Overall, this matches my expectation of what the output would be. I know that Markov chains are not the ideal implementation, and that using another model could produce far better results, but that would take a significant amount of research to identify options and would probably be too complex/new to me to be able to implement for this project.

## Reflection
I was unmotivated and behind on this project from the start. When I started on reading journal 11, which was about the text we planned to use, I was stuck on finishing the Computational Art project which detracted my attention so I put off working on it. When I started a week later, I had hoped that exploring and extending the examples in the project description would guide me in a specific direction, but I was too critical of my own ideas. A week later, I had written code messing around with Markov chains, sentiment analysis, word frequency, and used texts from Wikipedia, Project Gutenberg, and news sites, but couldn't decide what to do with it! Shortly thereafter project 4 and coronavirus happened and I put it off for 2 more weeks. I ended up skipping putting my slide in the slideshow and turning it in about a week after spring break, detracting project points, which I regret. I was too hard on myself and not decisive enough; I should have just gone with Markov on news headlines from the start!
