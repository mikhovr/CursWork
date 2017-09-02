require(tm)
require(wordcloud)
stops <- read.table("stopwords.txt", encoding ="UTF-8")
wordtags <- Corpus(DirSource("file4", encoding="UTF-8"))
wordtags <- tm_map(wordtags, stripWhitespace)
wordtags <- tm_map(wordtags, removeWords, stops)
inspect(wordtags)

wordcloud(wordtags, scale=c(5,0.5), max.words=25, random.order=TRUE, rot.per=0.35, use.r.layout=FALSE, colors=brewer.pal(8, "Dark2"))