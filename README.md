# Text Mining
Repository for Mini Project 3: Text Mining

## Markov Text Generation of Political News Headlines
What I did:
* Scraped html of news sites for headlines: CNN, Fox, Politico, Washington Post, New York Times
* Used markov chains to generate fake news

What I found out:
* Chains longer than one word don’t have many diverging options due to dataset size
* Varying degrees of believability/readability (markov chains not an ideal way to implement)

Examples:

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

Top 20 words in the news:
* ['to', 'of', 'for', 'on', 'in', 'with', 'is', 'says', 'as', 'from', 'be', 'he', 'during', 'response', 'by', 'will', 'that', 'pandemic', 'more', 'are']

Top 20 words in the news excluding common words:
* ['during', 'response', 'pandemic', 'need', 'amid', 'outbreak', 'governor', 'federal', 'public', 'political', 'home', 'help', 'guidelines', 'crisis', 'coronavirus,', 'bill', 'administration', 'virus', 'trillion', 'stimulus']
