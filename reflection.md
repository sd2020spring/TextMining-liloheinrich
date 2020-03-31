# Markov Text Generation of Political News Headlines

## Project Overview [Maximum 200 words]
### Sources
Data Sources:

    New York Times: https://www.nytimes.com/section/politics
    Fox News: https://www.foxnews.com/politics
    Washington Post: https://www.washingtonpost.com/politics/?nid=top_nav_politics
    CNN News: https://www.cnn.com/politics
    Politico: https://www.politico.com/politics

Other sources I indentified but wasn't able to process include:

    National Public Radio (NPR): https://www.npr.org/sections/politics/
    Breitbart https://www.breitbart.com/politics/
    National Broadcasting Company (NBC): https://www.nbcnews.com/politics
    Columbia broadcasting System (CBS): https://www.cbsnews.com/politics
    Wall Street Journal (WSJ): https://www.wsj.com/news/politics
    Boston Globe: https://www.bostonglobe.com/nation/politics/?p1=BGHeader_MainNav
    Huffington Post: https://www.huffpost.com/news/politics

I deliberately chose wide-ranging and controversial sources for variety.

### Libraries
Libraries used:

    _requests_: get the html code of these webpages
    _re_: split out the headlines using regular expressions by the surrounding tags or syntax identified
    _pickle_: condense the data and save it as a file which can be reloaded later

To get the information found on these news sites, I used the _requests_ library to get the html code. Next, to process the code I identified the tags or syntax typically surrounding the headlines, then used the _re_ library to split the code using regular expressions. This proved slightly challenging, due to each site having a different format/language. I learned a lot about regular expression syntax in trying to accurately filter out only headlines from a whole webpage where the code included escape characters, repeating sequences, etc. Lastly, I used the _pickle_ library to condense the data and save it as a file which I could later load from my main program.


## Implementation [~2-3 paragraphs]
Describe your implementation at a system architecture level. You should NOT walk through your code line by line, or explain every function (we can get that from your docstrings). Instead, talk about the major components, algorithms, data structures and how they fit together. You should also discuss at least one design decision where you had to choose between multiple alternatives, and explain why you made the choice you did.

## Results [~2-3 paragraphs + figures/examples]
Present what you accomplished:
    If you did some text analysis, what interesting things did you find? Graphs or other visualizations may be very useful here for showing your results.
    If you created a program that does something interesting (e.g. a Markov text synthesizer), be sure to provide a few interesting examples of the program’s output.

## Alignment [~3 paragraphs]
How much alignment did you find between what you set out to explore and the data and tools used to carry out the project? What was set of questions you had that sparked your exploration, and what you imagined an answer might look like upon completion? To what degree did you feel that the data source(s) you selected could help you explore those questions given its limitations? How well did the tools that you employed, given their limitations, serve you during the analysis. How confident are you in the answers they provided.

## Reflection [~1 paragraph]
From a process point of view, what went well? What could you improve? How would you attempt to mitigate the data-related or tool-choice problems with your project? Other possible reflection topics: Was your project appropriately scoped? Did you have a good plan for unit testing? How will you use what you learned going forward? What do you wish you knew before you started that would have helped you succeed?
