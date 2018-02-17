import re
import cgi
from chain import Chain, BEGIN, END

class Words(object):
    def __init__(self, corpus, state_size = 2, min_word_len = 2, chain = None):
        self.threshold = 100
        self.corpus = corpus
        self.state_size = state_size
        self.min_word_len = min_word_len
        self.chain = chain or Chain(self.split_corpus(corpus), state_size)

    def split_corpus(self, corpus):
        if (len(corpus) == 0):
            raise Exception("Corpus is empty")

        corpus_list = []

        for line in corpus.split('\n'):
            '''remove punctuation and lowercase everything'''
            line = re.sub(ur"\p{P}+", "", line).lower()

            for word in line.split():
                corpus_list += [list(word)]

        return corpus_list

    def generate_word(self):
        word = []
        error_count = 0

        while len(word) < self.min_word_len:
            word = []
            error_count += 1
            for letter in self.chain.walk():
                word += letter

            if error_count > self.threshold:
                raise Exception('Incorrect parameters. There is no way to generate words long enough with these parameters')

        return cgi.escape(''.join(word))

    def add_word(self, word):
        if not word:
            raise Exception("No word was given")
        
        corpus = self.split_corpus(word)
        return self.chain.add(corpus)






