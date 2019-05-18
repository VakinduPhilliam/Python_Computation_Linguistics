# Python Computational Linguistics.
# Computational Linguistics is a field in computer science that studies language lexicons 
# and patterns using techniques like artificial intelligence (AI), Machine Learning (ML) 
# and Data Analytics. 
# Morphological rules based on word suffixes.
# When we remove words from the lexicon (to reduce file size), the tagger may no longer
# recognize some words.
# By default, it will tag unknown words as NN. We can improve the tags of unknown words using 
# morphological rules. 
# Examine the English en-morphology.txt to see the rule format.
# One way to predict tags is to look at word suffixes. For example, English adverbs usually end in -ly.
# In Italian they end in -mente. The following script determines the most frequent tag for each word
# suffix:

from pattern.db import Datasheet
 
lexicon = {}

for frequency, word, tags in Datasheet.load("it-lexicon.csv"):
    lexicon[word] = tags.split(", ")

from collections import defaultdict
 
# {"mente": {"RB": 2956.0, "JJ": 8.0, NN: "2.0"}}

suffix = defaultdict(lambda: defaultdict(float))

for w in lexicon:

    if len(w) > 5: # Last 5 characters.
        x = w[-5:] #

        for tag in lexicon[w]:
            suffix[x][tag] += 1.0
 
# Map the dictionary to a list sorted by total tag count.

suffix = [(sum(tags.values()), x, tags) for x, tags in suffix.items()]
suffix = sorted(suffix, reverse=True)
 
for n, x, tags in suffix[:100]:

    # Relative count per tag (0.0-1.0).
    # This shows the tag distribution per suffix more clearly.

    tags = [("%.3f" % (i/n), tag) for tag, i in tags.items()]
    tags = sorted(tags, reverse=True)

    print x, n, tags
