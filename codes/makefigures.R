library(ggplot2)

ggplot(mpg, aes(displ, hwy, colour = class)) + 
    geom_point()+ggsave("../figures/scatter plot.pdf")


ggplot(mpg, aes(displ, hwy, colour = class)) + 
    geom_bar()+ggsave("../figures/mpg_bar_plot.pdf")

ggplot(mpg, aes(displ, hwy, colour = class)) + 
    geom_line()+ggsave("../figures/mpg_line_plot.jpeg")