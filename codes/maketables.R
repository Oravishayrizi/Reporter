library(stargazer)
library(ggplot2) #the dataset mpg is from  ggplot2

stargazer(mpg,out = "../tables/mpg_desc_stat.tex",title = "mpg dataset- desc stat")


stargazer(head(mpg),summary = FALSE, out = "../tables/mpg_head.tex",title = "mpg dataset- first 5 rows")
