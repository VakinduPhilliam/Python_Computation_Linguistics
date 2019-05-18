# Python Computational Linguistics.
# Computational Linguistics is a field in computer science that studies language lexicons 
# and patterns using techniques like artificial intelligence (AI), Machine Learning (ML) 
# and Data Analytics. 
# Mining data for texts
# The lexicons bundled in Pattern are about 500KB to 1MB in file size. If we save our Italian lexicon as a 
# file, it is about 2MB (or 4MB with the inflections). We may want to reduce it, by removing less important words.
# Which words to remove? We don't want to remove la; it looks important in Italian. We can assess a word's importance
# by counting how many times it occurs in written text.
# The following script uses the pattern.web module to retrieve Italian texts from Wikipedia. 
# The Wikipedia class has a search() method that returns a WikipediaArticle. 
# We then use the pattern.vector module to count the words in articles:
# Word frequency.

from pattern.web import Wikipedia
from pattern.vector import words
 
frequency = {}

# Spreading activation.
# Parse links from seed article & visit those articles.

links, seen = set(["Italia"]), {}

while len(links) > 0:

    try:
        article = Wikipedia(language="it").search(links.pop(), throttle=10)
        seen[article.title] = True

        # Parse links from article.

        for link in article.links:

            if link not in seen:
                links.add(link)

        # Parse words from article. Count words.

        for word in words(article.string):

            if word not in frequency:
                frequency[word] = 0
            frequency[word] += 1
        print sum(frequency.values()), article.title

    except:
        pass

    # Collect a reliable amount of words (e.g., 1M).

    if sum(frequency.values()) > 1000000:
        break
 
#top = sorted((count, word) for word, count in frequency.items())
#top = top[-1000:]
#print top

# We should also boost our miner by including contemporary newspaper articles:

from glob import glob
 
# Up-to-date newspaper articles:

for f in glob("repubblica-*.txt"):

    for word in words(open(f).read()):

        if word not in frequency:
            frequency[word] = 0

        frequency[word] += 1
