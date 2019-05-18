# Python Computational Linguistics.
# Computational Linguistics is a field in computer science that studies language lexicons 
# and patterns using techniques like artificial intelligence (AI), Machine Learning (ML) 
# and Data Analytics. 
# Pattern contains part-of-speech taggers for a number of languages (including English, German, French and Dutch).
# Part-of-speech tagging is useful in many data mining tasks. 
# A part-of-speech tagger takes a string of text and identifies the sentences and the words in the text along with 
# their word type. 
# Reading the Spanish Wikicorpus.
# The corpus contains over 50 text files, each 25-100MB in size. Each line in each file is a word with its lemma (base form)
# and its part-of-speech tag in the Parole tagset. 
# The following function reads the corpus efficiently.
# Note how open() is used as an iterator that yields lines from a given text file. 
# This way, we avoid loading the whole text file into memory.
# The function simplifies the tags and returns a list of sentences, in which each sentence is a list of
# (word, tag)-tuples:
# The function can be adapted to read other corpora of course.

from glob import glob
from codecs import open, BOM_UTF8 
  
def wikicorpus(words=1000000, start=0):

    s = [[]]
    i = 0

    for f in glob("tagged.es/*")[start:]:

        for line in open(f, encoding="latin-1"):

            if line == "\n" or line.startswith((
              "<doc", "</doc>", "ENDOFARTICLE", "REDIRECT",
              "Acontecimientos", 
              "Fallecimientos", 
              "Nacimientos")):
                continue
            w, lemma, tag, x = line.split(" ")

            if tag.startswith("Fp"):
                tag = tag[:3]

            elif tag.startswith("V"):  # VMIP3P0 => VMI
                tag = tag[:3]

            elif tag.startswith("NC"): # NCMS000 => NCS
                tag = tag[:2] + tag[3]

            else:
                tag = tag[:2]

            for w in w.split("_"): # Puerto_Rico
                s[-1].append((w, tag)); i+=1

            if tag == "Fp" and w == ".":
                s.append([])

            if i >= words:
                return s[:-1]
