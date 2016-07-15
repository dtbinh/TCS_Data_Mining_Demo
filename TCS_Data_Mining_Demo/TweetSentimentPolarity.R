#set working directory
setwd("Libraries\Documents")

#install and load packages
library(twitteR)
library(ROAuth)
library(plyr)
library(dplyr)
library(stringr)
library(ggplot2)
library(wordcloud)
library(SnowballC)
library(qdap)
library(e1071)
library(tm)
library(RColorBrewer)

#use sample data
myTweets <- read.csv("tweetCSV.csv")

#create Corpus
myCorpus <- Corpus(VectorSource(myTweets$TWEET))

#stemming: shortening the words
myCorpus <- tm_map(myCorpus, stemDocument)

#convert to plain text by removing punctuation
myCorpus <- tm_map(myCorpus, removeWords, c(stopwords('en'), keywords))

#sentSplit

sent_df = data.frame(myCorpus = unlist(myCorpus))

myTweets = sentSplit(sent_df, myTweets, rm.var = NULL, endmarks = c("?", ".", "!",
                                                           "|"), incomplete.sub = TRUE, rm.bracket = TRUE, stem.col = FALSE,
          text.place = "right", verbose = is.global(2))

#polarity(myCorpus, grouping.var = NULL,
 #        polarity.frame = qdapDictionaries::key.pol, constrain = FALSE,
  #       negators = qdapDictionaries::negation.words,
   #      amplifiers = qdapDictionaries::amplification.words,
    #     deamplifiers = qdapDictionaries::deamplification.words,
     #    question.weight = 0, amplifier.weight = 0.8, n.before = 4,
      #   n.after = 2, rm.incomplete = FALSE, digits = 3)

polarity(myCorpus)

#myTweets = sapply(myTweets, functions(x) x $getText())
################OLD CODE#############################
#classify emotions
# uses naive bayes theorem 
classEmo = classify_emotions(myTweets, algorithm = "bayes", prior = 1,0)

#get emotion best fit
emotion = classEmo(0.7)

#substitue N/A with "unknown"
emotion[is.na(emotion)] = "unknown"

#classify polarity
classPol = classify_polarity(myTweets, algorithm = "bayes")
#get polarity best fit 
polarity = classPol[0.4]

#create data frame w resukts and obtain some gen stats

#data frame w results
sent_df = data.frame(text=myTweets, emotion = emotion, polarity = polarity, stringsAsFactors = FALSE)

#sort data frame
sent_df = within(sent_df, emotion <- factor(emotion, levels = names(sort(table(emotion), decreasing = TRUE))))
sent_df1 = within(sent_df, polarity <- factor(polarity, levels = names(sort(table(polarity), decreasing = TRUE)))) 
#plot the results
ggplot(sent_def, aes(x=emotion)) +
  geom_bar((aes(y = ..count.., fill = emotion)) +
             scale_fill_brewer(palette = "Dark2") +
             labs(x="emotion categories", y = "number of Tweets"), title = "classification based on emotion")

#plot distribution of polarity
ggplot(sent_df1, aes(x=polarity))+
  geom_bar (aes(y=..count..,fille = polarity))+
  scale_fill_brewer(palette = "Dark2")+labs(x="polarity categories", y = "number of tweets", title = "classification based on polarity")
