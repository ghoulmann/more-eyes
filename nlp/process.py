import spacy
from spacy_readability import Readability

def process(text):
    nlp = spacy.load('en_core_web_sm') 
    nlp.add_pipe(Readability(), last=True)
    return nlp(text)
    