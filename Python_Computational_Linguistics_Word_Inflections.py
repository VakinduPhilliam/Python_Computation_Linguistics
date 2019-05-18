# Python Computational Linguistics.
# Computational Linguistics is a field in computer science that studies language lexicons 
# and patterns using techniques like artificial intelligence (AI), Machine Learning (ML) 
# and Data Analytics. 
# Mining data for word inflections. 
# In many languages, words inflect according to tense, mood, person, gender and number.
# This is true for verbs and often for nouns and adjectives. 
# In Italian, for example, the plural form of the noun affetto (affection) is affetti, while the plural
# feminine form of the adjective affetto (affected) is affette. 
# Unfortunately, the inflected forms are not always in the Wiktionary index. 
# We need to mine deeper to retrieve them. This is a time-consuming process. We need to set a high throttle 
# between requests to avoid being blacklisted by Wiktionary's servers.
# This script defines an inflect() function. Given a word, it returns a dictionary of word forms:

from pattern.web import URL, DOM, plaintext
import re
 
def inflect(word, language="italian"):

    inflections = {}
    url = "http://en.wiktionary.org/wiki/" + word.replace(" ", "_") 
    dom = DOM(URL(url).download(throttle=10, cached=True))

    pos = ""

    # Search the header that marks the start for the given language:
    # <h2><span class="mw-headline" id="Italian">Italian</span></h2>

    e = dom("#" + language)[0].parent

    while e is not None: # e = e.next_sibling

        if e.type == "element":

            if e.tag == "hr": # Horizontal line = next language.
                break

            if e.tag == "h3": # <h3>Adjective [edit]</h3>
                pos = plaintext(e.content.lower())
                pos = pos.replace("[edit]", "").strip()[:3].rstrip("ouer") + "-"

            # Parse inflections, using regular expressions.

            s = plaintext(e.content)

            # affetto m (f affetta, m plural affetti, f plural affette)

            if s.startswith(word):

                for gender, regexp, i in (
                  ("m" , r"(" + word + r") m", 1),
                  ("f" , r"(" + word + r") f", 1),
                  ("m" , r"(" + word + r") (mf|m and f)", 1),
                  ("f" , r"(" + word + r") (mf|m and f)", 1),
                  ("m" , r"masculine:? (\S*?)(,|\))", 1),
                  ("f" , r"feminine:? (\S*?)(,|\))", 1),
                  ("m" , r"(\(|, )m(asculine)? (\S*?)(,|\))", 3),
                  ("f" , r"(\(|, )f(eminine)? (\S*?)(,|\))", 3),
                  ("mp", r"(\(|, )m(asculine)? plural (\S*?)(,|\))", 3),
                  ("fp", r"(\(|, )f(eminine)? plural (\S*?)(,|\))", 3),
                  ( "p", r"(\(|, )plural (\S*?)(,|\))", 2),
                  ( "p", r"m and f plural (\S*?)(,|\))", 1)):
                    m = re.search(regexp, s, re.I)
                    if m is not None:
                        # {"adj-m": "affetto", "adj-fp": "affette"}
                        inflections[pos + gender] = m.group(i)

            #print s

         e = e.next_sibling

    return inflections
