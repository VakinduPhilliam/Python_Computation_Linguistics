# Python Computational Linguistics.
# Computational Linguistics is a field in computer science that studies language lexicons 
# and patterns using techniques like artificial intelligence (AI), Machine Learning (ML) 
# and Data Analytics. 
# Pattern contains part-of-speech taggers for a number of languages (including English, German, French and Dutch).
# Part-of-speech tagging is useful in many data mining tasks. 
# A part-of-speech tagger takes a string of text and identifies the sentences and the words in the text along with 
# their word type. 
# Rules for unknown words based on word suffixes.
# By default, unknown words (= not in lexicon) will be tagged as nouns. We can improve this with morphological rules,
# in other words, rules based on word prefixes and suffixes. For example, English words ending in -ly are usually adverbs:
# really, extremely, and so on. Similarily, Spanish words that end in -mente are adverbs. Spanish words ending in -ando
# or -iendo are verbs in the present participle: hablando, escribiendo, and so on.

# {"mente": {"RG": 4860, "SP": 8, "VMS": 7}}

suffix = defaultdict(lambda: defaultdict(int))
 
for sentence in wikicorpus(1000000):

    for w, tag in sentence:

        x = w[-5:] # Last 5 characters.

        if len(x) < len(w) and tag != "NP":
            suffix[x][tag] += 1
 
top = []

for x, tags in suffix.items():

    tag = max(tags, key=tags.get) # RG
    f1  = sum(tags.values())      # 4860 + 8 + 7
    f2  = tags[tag] / float(f1)   # 4860 / 4875

    top.append((f1, f2, x, tag))
 
top = sorted(top, reverse=True)
top = filter(lambda (f1, f2, x, tag): f1 >= 10 and f2 > 0.8, top)
top = filter(lambda (f1, f2, x, tag): tag != "NCS", top)
top = top[:100] 
top = ["%s %s fhassuf %s %s" % ("NCS", x, len(x), tag) for f1, f2, x, tag in top]
 
open("es-morphology.txt", "w").write(BOM_UTF8 + "\n".join(top).encode("utf-8"))
