# Python Computational Linguistics.
# Computational Linguistics is a field in computer science that studies language lexicons 
# and patterns using techniques like artificial intelligence (AI), Machine Learning (ML) 
# and Data Analytics. 
# Contextual rules.
# When we constructed a CSV-file, we saw that some words can have multiple tags, depending on their 
# role in the sentence. 
# In English, in "I can", "you can" or "we can", can is a verb. In "a can" and "the can" it is a noun.
# We could generalize this in two contextual rules: PRP + can -> VB, and DT + can -> NN. 
# Examine the English en-context.txt to see the rule format.
# We can create contextual rules by hand. We can also analyze a corpus of tagged texts (a treebank) to 
# predict how word tags change according to the surrounding words. 
# However, a corpus of tagged texts implies that it was tagged with another part-of-speech tagger.
# It is a thin line between using someone else's tagger and plagiarizing someone else's tagger.
# We should contact the authors and/or cite their work.
# For Italian, we can use the freely available WaCKy corpus (Baroni, Bernardini, Ferraresi & Zanchetta, 2009). T
# he following script reads 1 million words from the WaCKy MultiTag Wikipedia corpus. 
# For words that can have multiple tags, it records the tag of the preceding word and its frequency:

from pattern.db import Datasheet
 
ambiguous = {}

for frequency, word, tags in Datasheet.load("it-lexicon.csv"):
    tags = tags.split(", ")
    tags = [tag for tag in tags if tag] 

    if len(tags) != 1 and int(frequency) > 100:
        ambiguous[word] = (int(frequency), tags)

from codecs import open
from collections import defaultdict
 
# Map TANL tags to Penn Treebank II.
# medialab.di.unipi.it/wiki/Tanl_POS_Tagset

TANL = {
     "A": "JJ",
     "B": "RB",
     "C": "CC", "CC": "CC", "CS": "IN",
     "D": "DT",
     "E": "IN",
    "FF": ",", "FS": ".", "FB": "(",
     "I": "UH",
     "N": "CD",
     "P": "PRP", "PP": "PRP$",
     "R": "DT",
     "S": "NN", "SP": "NNP", 
     "T": "DT",
     "V": "VB", "VM": "MD"
}
 
# Word tags linked to frequency of preceding word tag:
# {"le": {"DT": {"IN": 1580}, "PRP": {"VB": 105}}}

context = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
 
window = [] # [(word1, tag1), (word2, tag2), (word3, tag3)]
 
for i, s in enumerate(open("/downloads/wikiMT", encoding="utf-8")):

    s = s.split("\t")

    if i > 1000000:
        break

    if i > 1 and len(s) >= 3:
        word, tag = s[0:2] # ("l'", "RD", "il")
        tag = TANL.get(tag[:2]) or \
              TANL.get(tag[:1]) or tag
        window.append((word, tag))

    if len(window) > 3:
        window.pop(0)

    if len(window) == 3 and window[1][0] in ambiguous:

        w1, tag1 = window[0] # word left
        w2, tag2 = window[1] # word that can have multiple tags
        w3, tag3 = window[1] # word right

        context[w2][tag2][tag1] += 1

# We can then examine the output, sorted by word frequency:

for word in reversed(sorted(ambiguous, key=lambda k: ambiguous[k][0])):

    print word

    for tag in context[word]:

        left = context[word][tag]
        s = float(sum(left.values()))

        left = [("%.2f" % (n / s), x) for x, n in left.items()]
        left = sorted(left, reverse=True)

        print "\t", int(s), tag, left[:5]
