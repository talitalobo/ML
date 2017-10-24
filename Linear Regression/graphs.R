library(ggplot2)

rss<-read.csv("rss.csv",sep = ",")
colnames(rss) <- c("erro","iteracao")

png(filename="erro.png")
erro<-ggplot(rss, aes(x=iteracao, y=erro)) + 
  geom_point() + xlab("Iteração") + ylab("Erro") + ggtitle("Learning Rate: 0.001")
plot(erro)
dev.off()