print("Siemano kolano")
print("Elo pomelo")
dane <- read.csv(file = "Ankieta.csv",
                 header = T, encoding = "UTF-8")
View(dane)
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
dane$wiek[53] <- 17
