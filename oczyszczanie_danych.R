{dane <- read.csv(file = "Ankieta.csv",
                  header = T, encoding = "UTF-8")
lab <- c("timestamp", "plec", "wiek", "zly_humor", "swietnie",
         "zly_nastroj", "roz_spok", "szaro_bezn","dobry_humor",
         "pogodny", "przygnebiony", "zle_samop", "dobre_samop",
         "radosc", "niepokoj", "strach", "milosc", "gniew",
         "wesolosc", "upokorzenie", "smutek", "wzburzenie", 
         "lek", "zal", "obawa", "zlosc", "zalamanie", 
         "szczescie", "wscieklosc", "oddanie", "zadowolenie",
         "czulosc", "wstyd", "pocz_winy", "przywiazanie", 
         "depresja", "nieszczescie", "liczba_przespanych_godzin",
         "wyzn_pory_snu", "jakosc_snu", "godziny_sportu",
         "srodek_transportu", "kondycja_fizyczna", "godziny_pracy_urzadzenia",
         "godziny_rozrywki_urzadzenia", "poczucie_uzaleznienia_urzadzenia",
         "dieta", "jakosc_posilkow", "regularnosc_posilkow", 
         "posiadanie_zaufanej_osoby", "liczba_osob_kontakty",
         "znaczenie_kontaktow")
colnames(dane) <- lab
dane <- dane[2:ncol(dane)] #pozbywamy się kolumny timestamp
} #wczytanie danych, nadanie etykiet
{dane$wiek <- as.character(dane$wiek)
  indeksy <- which(nchar(dane$wiek)>3) #53, 82, 107, 219
  dane$wiek[indeksy]
  dane$wiek[53] <- 17
  dane$wiek[82] <- 21
  dane$wiek[107] <- 22
  dane$wiek[219] <- 15
  dane$wiek <- as.numeric(dane$wiek)
} #oczyszczanie danych w kolumnie 'wiek'
{
  samopoczucie1 <- c("zly_humor", "swietnie", "zly_nastroj", "roz_spok", "szaro_bezn",
                     "dobry_humor", "pogodny", 
                     "przygnebiony", "zle_samop", "dobre_samop")
  poziomy1 <- c("nie zgadzam się", "raczej się nie zgadzam", 
                "trochę tak, trochę nie", "raczej się zgadzam", "zgadzam się")
  for (i in(1:length(samopoczucie1)))   dane[, samopoczucie1[i]] <- factor(dane[, samopoczucie1[i]], levels = poziomy1)
  
}#poprawki w kolejności poziomów - samopoczucie cz1
{
  samopoczucie2 <- c("radosc", "niepokoj", "strach", "milosc", "gniew",
                     "wesolosc", "upokorzenie", "smutek", "wzburzenie", 
                     "lek", "zal", "obawa", "zlosc", "zalamanie", 
                     "szczescie", "wscieklosc", "oddanie", "zadowolenie",
                     "czulosc", "wstyd", "pocz_winy", "przywiazanie", 
                     "depresja", "nieszczescie")
  poziomy2 <- c("nigdy", "bardzo rzadko", "rzadko", "czasami", "często", "bardzo często", "zawsze")
  for(i in (1:length(samopoczucie2))) dane[, samopoczucie2[i]] <- factor(dane[, samopoczucie2[i]], levels = poziomy2)
  
} #poprawki w kolejności poziomów - samopoczucie cz2
{
  dane$liczba_przespanych_godzin <- factor(dane$liczba_przespanych_godzin,
                                           levels = c("mniej niż 4", "4-6", "6-8", "8-10", "więcej niż 10"))
  dane$liczba_przespanych_godzin <- as.factor(dane$liczba_przespanych_godzin)
  dane$jakosc_snu <- as.factor(dane$jakosc_snu)  
  dane$wyzn_pory_snu <- as.factor(dane$wyzn_pory_snu)
}#levels i as.factor - sen
{
  dane$godziny_sportu <- factor(dane$godziny_sportu, levels = c("nie uprawiam żadnego sportu",
                                                                "mniej niż 1", "1 - 2,5", "2,5 - 4", "więcej niż 4"))
  
  dane$srodek_transportu <- factor(dane$srodek_transportu, levels = 
                                     c("chodzę pieszo", "rower", "komunikacja miejska",
                                       "motocykl", "samochód"))
  dane$kondycja_fizyczna <- as.factor(dane$kondycja_fizyczna)
} #levels i as.factor - sport
{
  dane$godziny_pracy_urzadzenia <- factor(dane$godziny_pracy_urzadzenia, levels = 
                                            c("nie używam/rzadko używam komputera do pracy/nauki",
                                              "mniej niż 3", "3 - 5", "5 - 8", "powyżej 8"))
  dane$godziny_rozrywki_urzadzenia <- factor(dane$godziny_rozrywki_urzadzenia, levels = 
                                               c("mniej niż 1", "1 - 2", "2 - 3", "3 - 4", "więcej niż 4"))
  dane$poczucie_uzaleznienia_urzadzenia <- factor(dane$poczucie_uzaleznienia_urzadzenia, levels = 
                                                    c("nigdy", "rzadko", "czasami", "często", "bardzo często"))
} #levels - urządzenia
{
  dane$dieta <- factor(dane$dieta, levels=
                         c("fast food", "żywność mocno przetworzona (mrożonki, gotowe dania)", 
                           "mięso i ciężkostrawne potrawy", "warzywa i owoce",
                           "mam zbilansowaną dietę")) 
  indeksy_blad <- which(dane$jakosc_posilkow == "staram się jeść zdrowo, ale mi nie wychodzi :(")
  dane$jakosc_posilkow[indeksy_blad] <- "staram się jeść zdrowo, ale mi nie wychodzi"
  dane$jakosc_posilkow <- factor(dane$jakosc_posilkow, levels = 
                                   c("wszystko mi jedno", "nie jest to moim priorytetem", 
                                     "staram się jeść zdrowo, ale mi nie wychodzi", 
                                     "jest to dla mnie dość ważne", "jestem tym, co jem!"))
  dane$regularnosc_posilkow <- factor(dane$regularnosc_posilkow, levels = 
                                        c("jem nieregularnie", "różnie z tym bywa",
                                          "staram się jeść regularnie", "zazwyczaj jem regularnie",
                                          "mam stałe pory posiłków"))
  
} #levels i oczyszczenie danych - dieta
{
  dane$posiadanie_zaufanej_osoby <- factor(dane$posiadanie_zaufanej_osoby, levels = 
                                             c("nie mam nikogo takiego",
                                               "z rodziną/znajomymi nie poruszam poważnych tematów",
                                               "nie czuję się komfortowo rozmawiając na trudne tematy z rodziną/znajomymi",
                                               "na ogół mam do kogo zwrócić się z problemem",
                                               "mam osoby, z którymi mogę porozmawiać o wszystkim"))
  levels(dane$liczba_osob_kontakty) #tutaj wyjątkowo wszystko ok :)
  dane$znaczenie_kontaktow <- as.factor(dane$znaczenie_kontaktow)
} #levels i as.factor - kontakty
{
  suma_samop1 <- -(as.numeric(dane$zly_humor))+as.numeric(dane$swietnie)-
    as.numeric(dane$zly_nastroj)+as.numeric(dane$roz_spok)-as.numeric(dane$szaro_bezn)+
    as.numeric(dane$dobry_humor)+as.numeric(dane$pogodny)-as.numeric(dane$przygnebiony)-
    as.numeric(dane$zle_samop)+as.numeric(dane$dobre_samop) #uczucia ze skalą 1-5
  suma_samop1sr <- suma_samop1/length(samopoczucie1)
  suma_samop2 <- as.numeric(dane$radosc)-as.numeric(dane$niepokoj)-as.numeric(dane$strach)+
    as.numeric(dane$milosc)-as.numeric(dane$gniew)+as.numeric(dane$wesolosc)-
    as.numeric(dane$upokorzenie)-as.numeric(dane$smutek)-as.numeric(dane$wzburzenie)-as.numeric(dane$lek)-
    as.numeric(dane$zal)-as.numeric(dane$obawa)-as.numeric(dane$zlosc)-as.numeric(dane$zalamanie)+
    as.numeric(dane$szczescie)-as.numeric(dane$wscieklosc)+as.numeric(dane$oddanie)+as.numeric(dane$zadowolenie)+
    as.numeric(dane$czulosc)-as.numeric(dane$wstyd)-as.numeric(dane$pocz_winy)+
    as.numeric(dane$przywiazanie)-as.numeric(dane$depresja)-as.numeric(dane$nieszczescie) #uczucia ze skalą 1-7
  suma_samop2sr <- suma_samop2/length(samopoczucie2)
  ocena_samop_ogolna <- suma_samop1+suma_samop2
  dane <- cbind(dane, suma_samop1sr, suma_samop2sr, ocena_samop_ogolna)
} #propozycja sumowania samopoczucia (pozytywne uczucia z plusem, negatywne z minusem)

save(dane, file = "dane.RData")
