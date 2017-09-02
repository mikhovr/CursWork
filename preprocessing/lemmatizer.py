import pymorphy2
morph = pymorphy2.MorphAnalyzer()
base = open('csvtest.csv', 'r')
lemmatized = open('lemm.csv', 'w')
badPOS = set(['VERB','INFN', 'NUMR', 'NPRO', 'PREP', 'CONJ', 'PRCL', 'INTJ', 'COMP', 'GRND', 'PRED'])
for doc in base:
    sp = doc.split()
    for word in sp:
        testword = morph.parse(unicode(word, "utf-8"))[0]
        if not testword.tag.POS in badPOS:
            lemmatized.write(testword.normal_form.encode("utf-8")+' ')
    lemmatized.write('\n')
base.close()
lemmatized.close()