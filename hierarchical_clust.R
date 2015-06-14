#This code is only for 100 tweets

library(ape)
data <- read.csv("outcsv.csv", header=FALSE, sep=",")
distmatrix <- dist(data, method = "euclidean", diag=TRUE, p=2)
hc <- hclust(distmatrix, method="ward.D")
hcd <- as.dendrogram(hc)
plot(cut(hcd, h =10)$upper, hang=3,main = "Upper the of cut at h=10", xlab='')

#classical plot
plot(hc, labels = NULL, hang = -0.1, check = TRUE,
     axes = TRUE,frame.plot = FALSE, ann = TRUE,
     main = "Cluster Dendrogram",
     sub = NULL, xlab = NULL, ylab = "Height")

