
import wikipedia as wiki



def osobnik(name):

    wiki.set_lang("pl")
    content = wiki.summary(name, sentences=6)
    return content

