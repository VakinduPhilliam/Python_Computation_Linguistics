# Python Computational Linguistics.
# Computational Linguistics is a field in computer science that studies language lexicons 
# and patterns using techniques like artificial intelligence (AI), Machine Learning (ML) 
# and Data Analytics. 
# Pattern contains part-of-speech taggers for a number of languages (including English, German, French and Dutch).
# Part-of-speech tagging is useful in many data mining tasks. 
# A part-of-speech tagger takes a string of text and identifies the sentences and the words in the text along with 
# their word type. 
# Testing the accuracy of the parser.
# The following script can be used to test the accuracy of the parser against Wikicorpus.
# We used 1.5 million words with 300 contextual and 100 morphological rules for an accuracy of about 91%.
# So we lost 9% but the parser is also fast and compact – the data files are about 1MB in size.
# Note how we pass map=None to the parse() command. This parameter is in turn passed to SpanishParser.find_tags()
# so that the original Parole tags are returned, which we can compare to the tags in Wikicorpus.

i = 0
n = 0

for s1 in wikicorpus(100000, start=1):

    s2 = " ".join(w for w, tag in s1)
    s2 = parse(s2, tags=True, chunks=False, map=None).split()[0]

    for (w1, tag1), (w2, tag2) in zip(s1, s2):

        if tag1 == tag2:
            i += 1
        n += 1
             
print float(i) / n
