# Python Computational Linguistics.
# Computational Linguistics is a field in computer science that studies language lexicons 
# and patterns using techniques like artificial intelligence (AI), Machine Learning (ML) 
# and Data Analytics. 
# Mining data for word inflections. 
# In many languages, words inflect according to tense, mood, person, gender and number.
# This is true for verbs and often for nouns and adjectives. 
# In Italian, for example, the plural form of the noun affetto (affection) is affetti, while the plural
# feminine form of the adjective affetto (affected) is affette. 
# Unfortunately, the inflected forms are not always in the Wiktionary index. 
# We need to mine deeper to retrieve them. This is a time-consuming process. We need to set a high throttle 
# between requests to avoid being blacklisted by Wiktionary's servers.
# This script defines an inflect() function. Given a word, it returns a dictionary of word forms:
# We can add a call to inflect() for each noun, adjective or verb in the inner loop of our miner
# (see 'Python Word Infect'):

if any(tag in pos for tag in ("n", "v", "adj")):

    for pg, w in inflect(word).items():
        p, g = pg.split("-") # pos + gender: ("adj", "f")

        if w not in lexicon:
            lexicon[w] = []

        if p not in lexicon[w]:
            lexicon[w].append(p)