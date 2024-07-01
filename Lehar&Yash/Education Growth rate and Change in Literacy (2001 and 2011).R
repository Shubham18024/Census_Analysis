getwd()
setwd("C:/Users/lehar/OneDrive/Desktop/SIRF")
library(ggplot2)
library(dplyr)
library(xlsx)
data<- read.csv("Literate.csv")

ggplot(data, aes(x = Change.in.Literacy, y = Change.population)) + # this is only for  Below_Primary,Primary, Middle, Secondary and Higher Secondary 
 geom_point() +
# geom_smooth(method = "lm", se = FALSE) +
  labs(
    title = "Relationship between Population Growth Rate and Literacy Rate Change",
    x = "Change in Literacy Rate ",
    y = "Population Growth Rate (%)"
  ) +
  theme_minimal()

ggplot(data, aes(x = Change.in.Literacy.., y = Change.population)) + # this is only for  Below_Primary,Primary, Middle, Secondary and Higher Secondary in %
  geom_point() +
  labs(
    title = "Relationship between Population Growth Rate and Literacy Rate Change",
    x = "Change in Literacy Rate (%)",
    y = "Population Growth Rate (%)"
  ) +
  theme_minimal()

ggplot(data, aes(x = Change.in.Total.Literacy, y = Change.population)) + # this is for total literates 
  geom_point() +
  labs(
    title = "Relationship between Population Growth Rate and Literacy Rate Change",
    x = "Change in Literacy Rate ",
    y = "Population Growth Rate (%)"
  ) +
  theme_minimal()

ggplot(data, aes(x = Change.in.Total.Literacy.., y = Change.population)) + # this is only for  Below_Primary,Primary, Middle, Secondary and Higher Secondary in %
  geom_point() +
  labs(
    title = "Relationship between Population Growth Rate and Literacy Rate Change",
    x = "Change in Literacy Rate (%)",
    y = "Population Growth Rate (%)"
  ) +
  theme_minimal()