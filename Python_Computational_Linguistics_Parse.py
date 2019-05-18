# Python Computational Linguistics.
# Computational Linguistics is a field in computer science that studies language lexicons 
# and patterns using techniques like artificial intelligence (AI), Machine Learning (ML) 
# and Data Analytics. 
# Subclassing the pattern.text Parser class.
# In summary, we constructed an it-lexicon.csv with the frequency and part-of-speech tags of known 
# words together with an it-morphology.txt and an it-context.txt. 
# We can use these to create a parser for Italian by subclassing the base Parser in the pattern.text module.
# The pattern.text module has base classes for Parser, Lexicon, Morphology, etc. 
# Take a moment to review the source code, and the source code of other parsers in Pattern.
# You'll notice that all parsers follow the same simple steps.
# A template for new parsers is included in pattern.text.xx.
# The Parser base class has the following methods with default behavior:
# Parser.find_tokens()  finds sentence markers (.?!) and splits punctuation marks from words,
# Parser.find_tags()    finds word part-of-speech tags,
# Parser.find_chunks()  finds words that belong together (e.g., the black cats),
# Parser.find_labels()  finds word roles in the sentence (e.g., subject and object), 
# Parser.find_lemmata() finds word base forms (cats -> cat)
# Parser.parse()        executes the above steps on a given string.
# We will need to redefine find_tokens() with rules for Italian abbreviations and contractions
#  (e.g., dell'anno = di + l' + anno). 
# We can then create an instance of the ItalianParser and feed it our data.
# We need to convert it-lexicon.csv to an it-lexicon.txt file in the right format (a word and its tag on each line). 
# This only needs happens the first time, of course.

w = []

for frequency, word, tags in Datasheet.load("it-lexicon.csv"):

    if int(frequency) >= 1: # Adjust to tweak file size.

        for tag in tags.split(", "):

            if tag:
                w.append("%s %s" % (word, tag)); break
 
open("it-lexicon.txt", "w", encoding="utf-8").write("\n".join(w))

# Load the lexicon and the rules in an instance of ItalianParser:

from pattern.text import Lexicon
 
lexicon = Lexicon(
        path = "it-lexicon.txt", 
  morphology = "it-morphology.txt", 
     context = "it-context.txt", 
    language = "it"
)
 
parser = ItalianParser(
     lexicon = lexicon,
     default = ("NN", "NNP", "CD"),
    language = "it"
)
 
def parse(s, *args, **kwargs):
    return parser.parse(s, *args, **kwargs)

# It is still missing features (notably lemmatization) but our Italian parser is essentially ready for use:

print parse("Il gatto nero faceva le fusa.")
