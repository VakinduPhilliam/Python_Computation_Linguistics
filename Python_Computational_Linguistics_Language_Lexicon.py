# Python Computational Linguistics.
# Computational Linguistics is a field in computer science that studies language lexicons 
# and patterns using techniques like artificial intelligence (AI), Machine Learning (ML) 
# and Data Analytics. 
# Mining data for part-of-speech tags
# The following script uses the pattern.web module to populate a language lexicon. 
# The URL class has a download() method that retrieves the HTML from a given web address. 
# The DOM class takes a string of HTML and transforms it into a tree of nested elements. 
# We can then search the tree with CSS selectors for the elements we need, i.e., the words and their type:

from pattern.web import URL, DOM

# Example URL.
 
url = "http://en.wiktionary.org/wiki/Index:Italian/"
 
lexicon = {}

for ch in "abcdefghijklmnopqrstuvwxyz0":

    print ch, len(lexicon)

    # Download the HTML source of each Wiktionary page (a-z).

    html = URL(url + ch).download(throttle=10, cached=True)

    # Parse the HTML tree.

    dom = DOM(html)

    # Iterate through the list of words and parse the part-of-speech tags.
    # Each word is a list item:
    # <li><a href="/wiki/additivo">additivo</a><i>n adj</i></li>

    for li in dom("li"):

        try:
            word = li("a")[0].content
            pos = li("i")[0].content.split(" ")

            if word not in lexicon:
                lexicon[word] = []
            lexicon[word].extend(pos)

        except:
            pass

# We end up with a lexicon dictionary that contains about a 100,000 words, each linked to a list of part-of-speech tags. 
# For example: la -> DT, PRP, NN.
# We don't have any tags for punctuation marks, but we can add them manually:
