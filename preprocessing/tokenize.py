# -*- coding: utf-8 -*-
from gensim import corpora
from collections import defaultdict

documents = [line.strip() for line in open("lemm.csv", 'r')]

stoplist = set(line.strip() for line in open('stopwords.txt'))
texts = [[word for word in document.lower().split() if word not in stoplist]
          for document in documents]
# remove words that appear only once
frequency = defaultdict(int)
for text in texts:
     for token in text:
         frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1]
          for text in texts]

dictionary = corpora.Dictionary(texts)
dictionary.save('dictionary.dict')

corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('corporacorp.mm', corpus) # store to disk, for later use