dane$wiek_kat <- factor(findInterval(dane$wiek,c(21,25)),levels = 0:2, labels = c("<21","21-24",">=25"),ordered = T)
View(dane[,c("wiek","wiek_kat")])
