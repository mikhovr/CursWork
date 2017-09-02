similarity_data <- read.csv("outcsv.csv", header = FALSE, sep=",")

#choosing number of clusters block start
wss <- (nrow(similarity_data)-1)*sum(apply(similarity_data,2,var))
for (i in 2:15) wss[i] <- sum(kmeans(similarity_data,
                                       centers=i)$withinss)
plot(1:15, wss, type="b", xlab="Number of Clusters",
     ylab="Within groups sum of squares")
#choosing number of clusters block finish

clust_number <- 8

km<-kmeans(data, clust_number, iter.max = 10, nstart = 1, trace=TRUE)

plot(data, col = km$cluster, main="k-means clustering", xlab="1st distrib similarity", ylab="2nd distrib similarity")
points(km$centers, col = 1:8, pch = 8)