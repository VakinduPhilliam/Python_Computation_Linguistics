# Python Computational Linguistics.
# Computational Linguistics is a field in computer science that studies language lexicons 
# and patterns using techniques like artificial intelligence (AI), Machine Learning (ML) 
# and Data Analytics. 
# Mining Data for verb conjugations.
# Italian verbs inflect by person, tense and mood. For example, the 1st person present indicative of 
# essere (to be) is sono (I am). 
# We can mine the verb conjugation tables from Wiktionary for frequent verbs, and use the data to expand
# our lexicon or to build a lemmatizer.
# The verb conjugation table for a given verb is on the same page that we mined with inflect().
# So, for many words the HTML may already be cached locally and the process should not take too long.

from pattern.web import URL, DOM, plaintext as plain
 
MOOD, TENSE, PARTICIPLE = (
    ("indicative", "conditional", "subjunctive", "imperative"),
    ("present", "imperfect", "past historic", "future"),
    ("present participle", "past participle")
)
 
def conjugate(verb, language="italian"):

    url  = URL("http://en.wiktionary.org/wiki/%s" % verb)
    dom  = DOM(url.download(throttle=10, cached=True))
    conj = {"infinitive": verb}
    mood = None

    for table in dom("table.inflection-table"):

        # Search the header that marks the start for the given language:
        # <h2><span class="mw-headline" id="Italian">Italian</span></h2>

        h2 = table.parent.parent

        while h2:
            h2 = h2.previous

            if getattr(h2, "tag", "") == "h2" and \
               getattr(h2("span")[0], "id", "") != language:
                continue

        for tr in table("tr"):

            for th in tr("th"):

                # <th>indicative</th>

                if th.content in MOOD:
                    mood = th.content

                # <th>present</th><td>sono</td><td>sei></td>...

                if th.content in TENSE:
                    conj[th.content, mood] = [plain(td.content) for td in tr("td")]

                # <th>gerund</th><td>essendo</td>

                if th.content in PARTICIPLE:
                    conj[th.content] = plain(th.next.next.content)

            # <th>imperative</th></tr><tr><td></td><td>sii</td>...

            if mood == "imperative" and len(tr("th")) == 0:
                conj["present", mood] = [plain(td.content) for td in tr("td")]

        return conj

    return {}
