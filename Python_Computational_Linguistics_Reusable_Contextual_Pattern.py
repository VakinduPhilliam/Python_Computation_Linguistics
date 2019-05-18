# Python Computational Linguistics.
# Computational Linguistics is a field in computer science that studies language lexicons 
# and patterns using techniques like artificial intelligence (AI), Machine Learning (ML) 
# and Data Analytics. 
# Pattern contains part-of-speech taggers for a number of languages (including English, German, French and Dutch).
# Part-of-speech tagging is useful in many data mining tasks. 
# A part-of-speech tagger takes a string of text and identifies the sentences and the words in the text along with 
# their word type. 
# Brill's algorithm uses an iterative approach to learn contextual rules.
# In short, this means that it tries different combinations of interesting rules to find a subset that produces the
# best tagging accuracy. This process is time-consuming (minutes or hours), so we want to store the final subset
# for reuse.
# Brill's algorithm in NLTK defines context using indices. For example, (1, 2) in the previous script means: one or 
# two words (or tags) after the current word. Brill's original implementation uses commands to describe context, e.g.,
# NEXT1OR2WORD or NEXT1OR2TAG. Pattern also uses these commands, so we need to map NLTK's indices to the command set:
# We end up with a file es-context.txt with a 100 contextual rules in a format usable with Pattern.

ctx = []
 
for rule in tagger.rules():

    a = rule.original_tag
    b = rule.replacement_tag
    c = rule._conditions
    x = c[0][2]
    r = c[0][:2]

    if len(c) != 1: # More complex rules are ignored in this script. 
        continue

    if isinstance(rule, ProximateTagsRule):
        if r == (-1, -1): cmd = "PREVTAG"
        if r == (+1, +1): cmd = "NEXTTAG"
        if r == (-2, -1): cmd = "PREV1OR2TAG"
        if r == (+1, +2): cmd = "NEXT1OR2TAG"
        if r == (-3, -1): cmd = "PREV1OR2OR3TAG"
        if r == (+1, +3): cmd = "NEXT1OR2OR3TAG"
        if r == (-2, -2): cmd = "PREV2TAG"
        if r == (+2, +2): cmd = "NEXT2TAG"

    if isinstance(rule, ProximateWordsRule):
        if r == (+0, +0): cmd = "CURWD"
        if r == (-1, -1): cmd = "PREVWD"
        if r == (+1, +1): cmd = "NEXTWD"
        if r == (-2, -1): cmd = "PREV1OR2WD"
        if r == (+1, +2): cmd = "NEXT1OR2WD"

    ctx.append("%s %s %s %s" % (a, b, cmd, x))
 
open("es-context.txt", "w").write(BOM_UTF8 + "\n".join(ctx).encode("utf-8"))
