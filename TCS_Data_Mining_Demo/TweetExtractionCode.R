#set working directory
setwd("C:\\Users\\priyabhatnagar\\TCS_Data_Mining_Demo")

#install and load packages
library(twitteR)
library(ROAuth)
library(plyr)
library(dplyr)
library(stringr)
library(ggplot2)
library(wordcloud)
library(SnowballC)
library(tm)
library(RColorBrewer)

#use sample data
myTweets <- read.csv("data\\tweetCSV.csv")

#create Corpus
myCorpus <- Corpus(VectorSource(myTweets$Tweets))

#convert to plain text by removing punctuation
myCorpus <- tm_map(myCorpus, removeWords, stopwords(kind = "en"))

#stemming: shortening the words
myCorpus <- tm_map(myCorpus, stemDocument)

#cloud

pal <- brewer.pal(8, "Dark2")
wordcloud(myCorpus, min.freq = 4, max.words = 100, width = 1000, height = 1000, random.order = FALSE, color=pal)

myCorpus <- tm_map(myCorpus, PlainTextDocument)
