# Python Computational Linguistics.
# Computational Linguistics is a field in computer science that studies language lexicons 
# and patterns using techniques like artificial intelligence (AI), Machine Learning (ML) 
# and Data Analytics. 
# Pattern contains part-of-speech taggers for a number of languages (including English, German, French and Dutch).
# Part-of-speech tagging is useful in many data mining tasks. 
# A part-of-speech tagger takes a string of text and identifies the sentences and the words in the text along with 
# their word type. 
# Subclassing the pattern.text Parser class.
# In summary, we constructed an es-lexicon.txt with the part-of-speech tags of known words together with an es-context.txt
# and an es-morphology.txt (step 4). We can use these to create a parser for Spanish by subclassing the base Parser in
# the pattern.text module. The pattern.text module has base classes for Parser, Lexicon, Morphology, etc.
# Take a moment to review the source code, and the source code of other parsers in Pattern.
# You'll notice that all parsers follow the same simple steps. A template for new parsers is included in pattern.text.xx.
# The Parser base class has the following methods with default behavior:
# Parser.find_tokens()  finds sentence markers (.?!) and splits punctuation marks from words,
# Parser.find_tags()    finds word part-of-speech tags,
# Parser.find_chunks()  finds words that belong together (e.g., the black cats),
# Parser.find_labels()  finds word roles in the sentence (e.g., subject and object), 
# Parser.find_lemmata() finds word base forms (cats -> cat)
# Parser.parse()        executes the above steps on a given string.
# We can create an instance of the SpanishParser and feed it our data. We will need to redefine find_tags() to map Parole
# tags to Penn Treebank tags (which all other parsers in Pattern use as well).

from pattern.text import Parser
 
PAROLE = {
    "AO": "JJ"  ,   "I": "UH"  , "VAG": "VBG",
    "AQ": "JJ"  ,  "NC": "NN"  , "VAI": "MD", 
    "CC": "CC"  , "NCS": "NN"  , "VAN": "MD", 
    "CS": "IN"  , "NCP": "NNS" , "VAS": "MD", 
    "DA": "DT"  ,  "NP": "NNP" , "VMG": "VBG",
    "DD": "DT"  ,  "P0": "PRP" , "VMI": "VB", 
    "DI": "DT"  ,  "PD": "DT"  , "VMM": "VB", 
    "DP": "PRP$",  "PI": "DT"  , "VMN": "VB", 
    "DT": "DT"  ,  "PP": "PRP" , "VMP": "VBN",
    "Fa": "."   ,  "PR": "WP$" , "VMS": "VB", 
    "Fc": ","   ,  "PT": "WP$" , "VSG": "VBG",
    "Fd": ":"   ,  "PX": "PRP$", "VSI": "VB", 
    "Fe": "\""  ,  "RG": "RB"  , "VSN": "VB", 
    "Fg": "."   ,  "RN": "RB"  , "VSP": "VBN",
    "Fh": "."   ,  "SP": "IN"  , "VSS": "VB", 
    "Fi": "."   ,                  "W": "NN", 
    "Fp": "."   ,                  "Z": "CD", 
    "Fr": "."   ,                 "Zd": "CD", 
    "Fs": "."   ,                 "Zm": "CD", 
   "Fpa": "("   ,                 "Zp": "CD",
   "Fpt": ")"   ,    
    "Fx": "."   ,    
    "Fz": "."  
}
 
def parole2penntreebank(token, tag):
    return token, PAROLE.get(tag, tag)
 
class SpanishParser(Parser):
     
    def find_tags(self, tokens, **kwargs):

        # Parser.find_tags() can take an optional map(token, tag) function,
        # which returns an updated (token, tag)-tuple for each token. 

        kwargs.setdefault("map", parole2penntreebank)
        return Parser.find_tags(self, tokens, **kwargs)

# Load the lexicon and the rules in an instance of SpanishParser:

from pattern.text import Lexicon
 
lexicon = Lexicon(
        path = "es-lexicon.txt", 
  morphology = "es-morphology.txt", 
     context = "es-context.txt", 
    language = "es"
)
 
parser = SpanishParser(
     lexicon = lexicon,
     default = ("NCS", "NP", "Z"),
    language = "es"
)
 
def parse(s, *args, **kwargs):
    return parser.parse(s, *args, **kwargs)

# It is still missing features (notably lemmatization) but our Spanish parser is essentially ready
# for use:

print parse(u"El gato se sentó en la alfombra.")
