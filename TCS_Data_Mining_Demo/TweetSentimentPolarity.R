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

print(myTweets)

#myTweets = sapply(myTweets, functions(x) x $getText())

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
sentimentDF = data.frame(text=myTweets, emotion = emotion, polarity = polarity, stringsAsFactors = FALSE)

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

