# Python Computational Linguistics.
# Computational Linguistics is a field in computer science that studies language lexicons 
# and patterns using techniques like artificial intelligence (AI), Machine Learning (ML) 
# and Data Analytics. 
# Pattern contains part-of-speech taggers for a number of languages (including English, German, French and Dutch).
# Part-of-speech tagging is useful in many data mining tasks. 
# A part-of-speech tagger takes a string of text and identifies the sentences and the words in the text along with 
# their word type. 

# Extracting contextual rules with NLTK.
# The Natural Language Toolkit for Python (NLTK) has an implementation of Brill's algorithm that we can use to learn
# contextual rules.
# First, we will anonymize proper nouns. The reason is that we want to learn general rules in the form of, for example: any
# proper noun followed by a verb instead of "Puerto Rico" followed by a verb.

sentences = wikicorpus(words=1000000)
 
ANONYMOUS = "anonymous"

for s in sentences:

    for i, (w, tag) in enumerate(s):
        if tag == "NP": # NP = proper noun in Parole tagset.
            s[i] = (ANONYMOUS, "NP")

# We can then train NLTK's FastBrillTaggerTrainer. It is based on a unigram tagger, which is simply a lexicon of known words
# and their part-of-speech tag. It will then boost the accuracy with a set of contextual rules that change a word's part-of-speech
# tag depending on the surrounding words.

from nltk.tag import UnigramTagger
from nltk.tag import FastBrillTaggerTrainer
 
from nltk.tag.brill import SymmetricProximateTokensTemplate
from nltk.tag.brill import ProximateTokensTemplate
from nltk.tag.brill import ProximateTagsRule
from nltk.tag.brill import ProximateWordsRule
 
ctx = [ # Context = surrounding words and tags.
    SymmetricProximateTokensTemplate(ProximateTagsRule,  (1, 1)),
    SymmetricProximateTokensTemplate(ProximateTagsRule,  (1, 2)),
    SymmetricProximateTokensTemplate(ProximateTagsRule,  (1, 3)),
    SymmetricProximateTokensTemplate(ProximateTagsRule,  (2, 2)),
    SymmetricProximateTokensTemplate(ProximateWordsRule, (0, 0)),
    SymmetricProximateTokensTemplate(ProximateWordsRule, (1, 1)),
    SymmetricProximateTokensTemplate(ProximateWordsRule, (1, 2)),
    ProximateTokensTemplate(ProximateTagsRule, (-1, -1), (1, 1)),
]
 
tagger = UnigramTagger(sentences)
tagger = FastBrillTaggerTrainer(tagger, ctx, trace=0)
tagger = tagger.train(sentences, max_rules=100)
 
#print tagger.evaluate(wikicorpus(10000, start=1))  
