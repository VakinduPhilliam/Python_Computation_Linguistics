# Python Computational Linguistics.
# Computational Linguistics is a field in computer science that studies language lexicons 
# and patterns using techniques like artificial intelligence (AI), Machine Learning (ML) 
# and Data Analytics. 
# Preprocessing a CSV-file.
# This is a good time to store the data (so we don't need to rerun the miner). 
# We map Wiktionary's word tags to Penn Treebank II, and combine the entries in lexicon and frequency. 
# We then use pattern.db to store the result as a CSV-file.

from pattern.db import Datasheet
 
PENN = {  "n": "NN",
          "v": "VB",
        "adj": "JJ",
        "adv": "RB",
    "article": "DT",
       "prep": "IN",
       "conj": "CC",
        "num": "CD",
        "int": "UH",
    "pronoun": "PRP",
     "proper": "NNP"
}
      
SPECIAL = ["abbr", "contraction"]
special = set()
 
csv = Datasheet()

for word, pos in lexicon.items():

    if " " not in word:

        f = frequency.get(word, frequency.get(word.lower(), 0))

        # Map to Penn Treebank II tagset.

        penn  = [PENN[tag] for tag in pos if tag in PENN]
        penn += [tag] if tag in ("SYM",".",",",":","\"","(",")","#","$") else [] 
        penn  = ", ".join(penn)

        # Collect tagged words in the .csv file.

        csv.append((f, word, penn))

        # Collect special words for post-processing.

        for tag in SPECIAL:

            if tag in pos:
                special.add(word)
 
csv.columns[0].sort(reverse=True)
csv.save("it-lexicon.csv")
 
print special
