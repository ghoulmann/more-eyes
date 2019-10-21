import readability
import syntok.segmenter as segmenter

class ReadabilityAnalysis():
    def __init__(self, text):
        tokenized = '\n\n'.join(
     '\n'.join(' '.join(token.value for token in sentence)
        for sentence in paragraph)
     for paragraph in segmenter.analyze(text))
        results = readability.getmeasures(tokenized, lang='en')
        