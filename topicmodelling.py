from gensim import corpora, models
import csv
dictionary = corpora.Dictionary.load('dictionary.dict')
corpus = corpora.MmCorpus('corporacorp.mm')
tfidf = models.TfidfModel(corpus, normalize=True)
corpus_tfidf = tfidf[corpus]
lda = models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=117)

corpus_lda = lda[corpus_tfidf]
l = lda.print_topics(117)
for item in l: print(item)


#Playing with vector models
#
##lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=2)
#corpus_lsi = lsi[corpus_tfidf]
#
#weightstf = [[wgt for word_id,wgt in doc] for doc in corpus_tfidf]
#for doc in corpus_tfidf:
#    for (word_id, wgt) in doc:
#        print(word_id, wgt),
#    print ''
#    
#with open("D:/cw/outtfidf.csv", "wb") as tf:
#    tfwriter = csv.writer(tf)
#    for item in weightstf:
#        tfwriter.writerow(item)
#
#weights_lsi = [[wgt for th_id,wgt in doc] for doc in corpus_lsi]
#for doc in corpus_lsi:
#    for (th_id, wgt) in doc:
#        print(th_id, wgt),
#    print ''
#
#
#with open("D:/cw/outcsv.csv", "wb") as f:
#    writer = csv.writer(f)
#    for item in weights_lsi:
#        if len(item)==2: writer.writerow(item)



