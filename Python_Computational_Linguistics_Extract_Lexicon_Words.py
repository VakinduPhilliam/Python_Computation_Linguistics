# Python Computational Linguistics.
# Computational Linguistics is a field in computer science that studies language lexicons 
# and patterns using techniques like artificial intelligence (AI), Machine Learning (ML) 
# and Data Analytics. 
# Pattern contains part-of-speech taggers for a number of languages (including English, German, French and Dutch).
# Part-of-speech tagging is useful in many data mining tasks. 
# A part-of-speech tagger takes a string of text and identifies the sentences and the words in the text along with 
# their word type. 
# Extracting a lexicon of known words.
# Pattern uses Brill's algorithm to construct its part-of-speech taggers.
# Other algorithms are more robust, but a Brill tagger is fast and compact (i.e., 1 MB of data) so it makes a good 
# candidate for Pattern.
# Brill's algorithm essentially produces a lexicon of known words and their part-of-speech tag (e.g., can -> VB), along
# with some rules for unknown words, and rules that change the tag according to a word's role in the sentence
# (e.g., "can of soda" -> NN).
# Using a large lexicon of the most common words and tagging unknown words as nouns, we can get quite decent tagging
# accuracy: between 80–90%. Then, we can use rules to improve the part-of-speech tags.
# Constructing the lexicon is not difficult. We simply count the occurrence of words in Wikicorpus, count the occurrence
# of their tags (some words have multiple tags), and take the top most frequent words with their most frequent tag.

from collections import defaultdict
 
# "el" => {"DA": 3741, "NP": 243, "CS": 13, "RG": 7}) 

lexicon = defaultdict(lambda: defaultdict(int))
  
for sentence in wikicorpus(1000000):

    for w, tag in sentence:
        lexicon[w][tag] += 1
 
top = []  

for w, tags in lexicon.items():    

    freq = sum(tags.values())      # 3741 + 243 + ...
    tag  = max(tags, key=tags.get) # DA

    top.append((freq, w, tag))
 
top = sorted(top, reverse=True)[:100000] # top 100,000
top = ["%s %s" % (w, tag) for freq, w, tag in top if w]
 
open("es-lexicon.txt", "w").write(BOM_UTF8 + "\n".join(top).encode("utf-8"))
