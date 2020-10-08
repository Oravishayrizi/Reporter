library(ggplot2)

ggplot(mpg, aes(displ, hwy, colour = class)) + 
    geom_point()+ggsave("../figures/scatter plot.pdf")


ggplot(data=iris, aes(x=Sepal.Width))+
    geom_histogram(binwidth=0.2, color="black", aes(fill=Species)) + 
    xlab("Sepal Width") +  ylab("Frequency") + ggtitle("Histogram of Sepal Width")+
    ggsave("../figures/iris_histogram.pdf")

ggplot(mpg, aes(displ, hwy, colour = class)) + 
    geom_line()+ggsave("../figures/mpg_line_plot.jpeg")