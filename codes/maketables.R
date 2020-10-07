library("stargazer")

stargazer(mpg,out = "../tables/mpg_desc_stat.tex",title = "mpg dataset- desc stat")


stargazer(head(mpg),summary = FALSE, out = "../tables/mpg_head.tex",title = "mpg dataset- foirst 5 rows")
