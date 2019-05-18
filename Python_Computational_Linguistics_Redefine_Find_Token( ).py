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

from pattern.text import Parser
 
ABBREVIATIONS = [
    "a.C.", "all.", "apr.", "b.c.", "c.m.", "C.V.", "d.C.", 
    "Dott.", "ecc.", "egr.", "giu.", "Ing.", "orch.", "p.es.", 
    "Prof.", "prof.", "ql.co.", "Spett."
]
 
CONTRACTIONS = {
     "all'": "all' ",
    "anch'": "anch' ",
       "c'": "c' ",
    "coll'": "coll' ",
     "com'": "com' ",
    "dall'": "dall' ",
    "dell'": "dell' ",
     "dev'": "dev' ",
     "dov'": "dov' ",
      "mo'": "mo' ",
    "nell'": "nell' ",
    "sull'": "sull' "
}
 
class ItalianParser(Parser):
     
    def find_tokens(self, tokens, **kwargs):

        kwargs.setdefault("abbreviations", ABBREVIATIONS)
        kwargs.setdefault("replace", CONTRACTIONS)
        return Parser.find_tokens(self, tokens, **kwargs)
