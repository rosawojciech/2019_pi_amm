# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 11:44:14 2020

@author: Alicja
"""
#%%
import tkinter as tk
from PIL import Image, ImageTk
#%%
global twoje_odp
twoje_odp=[] #lista, w której będą zapisane odp użytkownika

#%% pytania i odpowiedzi do ankiety
#%% sen
pytania_sen = ["Ile godzin średnio przesypiasz w ciągu doby? ", "Czy masz wyznaczone pory snu? \n(1-nie, 5-tak) ",
               "Jak oceniasz jakość swojego snu? \n(1-bardzo źle, 5-bardzo dobrze)"]
odpowiedzi_sen = [["mniej niż 4", "4-6", "6-8", "8-10","więcej niż 10"],[1,2,3,4,5],[1,2,3,4,5]]
#%%aktywnosc
pytania_aktywnosc = ["Ile godzin tygodniowo poświęcasz na sport?","Jaki środek transportu wybierasz najczęściej? ",
                     "Jak oceniasz swoją kondycję fizyczną? \n(1-źle, 5-dobrze)"]
odpowiedzi_aktywnosc = [["nie uprawiam żadnego sportu", "mniej niż 1", "1-2.5", "2.5-4", "więcej niż 4"],
                        ["samochód", "komunikacja miejska", "rower", "chodzę pieszo", "inny"],
                        [1,2,3,4,5]]
#%%urzadzenia
pytania_urzadzenia = ["Ile godzin (średnio) w ciągu dnia korzystasz \nz urządzeń elektronicznych \n(komputer, laptop, tablet) pracując lub ucząc się?",
                      "Ile godzin dziennie poświęcasz na korzystanie \nz urządzeń w celach rozrywkowych?",
                      "Czy zdarza Ci się mieć poczucie, \nże za dużo czasu spędzasz korzystając \nz urządzeń elektronicznych?"]
odpowiedzi_urzadzenia = [["nie używam/rzadko używam komputera do pracy/nauki",
                          "mniej niż 3", "3-5","5-8", "powyżej 8"],
                         ["mniej niż 1", "1-2", "2-3", "3-4", "więcej niż 4"],
                         ["nigdy", "rzadko", "czasami", "często", "bardzo często"]]

#%%dieta
pytania_dieta = ["Co przeważa w Twojej diecie?", "Jaką wagę przywiązujesz do jakości swoich posiłków?", "Jak oceniasz regularność swoich posiłków?"]
odpowiedzi_dieta = [["fast food", "żywność mocno przetworzona (mrożonki, gotowe dania)", "mięso i ciężkostrawne potrawy", "warzywa i owoce", "mam zbilansowaną dietę"],
                    ["wszystko mi jedno", "nie jest to moim priorytetem", "staram się jeść zdrowo, ale mi to nie wychodzi", "jest to dla mnie dość ważne", "jestem tym, co jem!"],
                    ["jem nieregularnie", "różnie z tym bywa", "staram się jeść regularnie", "zazwyczaj jem regularnie", "mam stałe pory posiłków"]]
#%%kontakty
pytania_kontakty = ["Czy masz kogoś, na kim możesz polegać w trudnej sytuacji?", "Z iloma osobami utrzymujesz kontakt w celach towarzyskich?",
                    "Jakie znaczenie mają dla Ciebie kontakty z innymi ludźmi? \n(1-małe, 5-duże)"]
odpowiedzi_kontakty = [["nie mam nikogo takiego", "z rodziną/znajomymi nie poruszam \npoważnych tematów",
                        "nie czuję się komfortowo rozmawiając na trudne \ntematy z rodziną/znajomymi",
                        "na ogół mam do kogo zwrócić się z problemem","mam osoby, z którymi mogę porozmawiać o wszystkim"],
                       ["0", "1", "2-3", "4-5", "5 i więcej"],[1,2,3,4,5]]
#%%
pytania_wszystkie = pytania_sen + pytania_aktywnosc + pytania_urzadzenia + pytania_dieta + pytania_kontakty
odpowiedzi_wszystkie = odpowiedzi_sen + odpowiedzi_aktywnosc + odpowiedzi_urzadzenia + odpowiedzi_dieta + odpowiedzi_kontakty

#%%
def start(ramka_startu):
    ramka_startu.destroy()
    
    n = len(twoje_odp)
    if(n<15):
        ramka_pytania = tk.Frame(okno, bd = 5)
        ramka_pytania.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        pytanie = tk.Label(ramka_pytania, text = pytania_wszystkie[n])
        pytanie.config(font=30)
        pytanie.pack(fill = "both", expand = "yes")
        przyciski_odp = []
        odp= tk.StringVar()
        odp.set(None)
    
        for i in range(5):
            przyciski_odp.append(tk.Radiobutton(ramka_pytania, text = odpowiedzi_wszystkie[n][i],value = odpowiedzi_wszystkie[n][i], variable = odp))
        przyciski_odp.append(tk.Button(ramka_pytania, bg="green", text = "Wybierz", command = lambda:wybieram(odp, ramka_pytania)))
        for (i, btn) in enumerate(przyciski_odp):
            btn.config(font=30)
            btn.pack(fill = "both", expand = "yes")
    else:
        okno.destroy()
        nowe_okno = tk.Tk()
        nowe_okno.geometry('600x600')
        nowe_okno.title("Oceń swoje samopoczucie!")
        nowe_okno.call('wm', 'iconphoto', okno._w, tk.PhotoImage(file='smiley.png'))
        nowe_okno.configure(bg="white")
        #canvas = tk.Canvas(nowe_okno, height = HEIGHT, width = WIDTH)
        #canvas.pack()
        wynik = oblicz_samopoczucie()
        komunikat = "Twoje samopoczucie zostało ocenione na "+str(wynik[0])+", \nczyli powinno być "+str(wynik[1])
        
        load = Image.open(wynik[2])
        render = ImageTk.PhotoImage(load)
        img = tk.Label(nowe_okno, image=render)
        img.image = render
        img.place(x=225, y=225)
        
    
        twoja_ocena = tk.Label(nowe_okno, text = komunikat,bg = wynik[3])
        twoja_ocena.config(font=44)
        #twoja_fotka = tk.Label(nowe_okno, image = fotka)
        twoja_ocena.place(x=100, y = 100)
        #twoja_fotka.place(relx =0, rely = 0, relwidth =0.2)
        wiecej_info = tk.Button(nowe_okno,text = "Więcej informacji", command = pokaz_info)
        wiecej_info.place(x=450, y =550)
        #skala = tk.Label(ramka_konca, text = "Skala oceny od -137 do +81, \nśrednia na podstawie naszych badań to -2.61")
        #skala.config(font=22)
        #skala.pack(fill = "both", expand = "yes")
#%%
def pokaz_info():
    tk.messagebox.showwarning(title="Informacje", message = "Skala oceny od -124 do +60, na podstawie naszych badań przeprowadzonych na grupie 240 osób średnia to -2.61, minimum to -79, maksimum to 55. Dane do badania samopoczucia były zbierane na podstawie ankiety, pytania dotyczace samopoczucia pochodziły z artykułu “Skale do Pomiaru Nastroju i Sześciu Emocji” autorstwa Bogdana Wojciszke i Wiesława Baryły. Autorami badania, na podstawie którego stworzono tą aplikację, są Marcin Dziadosz, Alicja Hołowiecka i Matylda Jankowska.")
#%%
def wybieram(odp, ramka_pytania):
    if(odp.get() == "None"):
        tk.messagebox.showwarning(title = "Uwaga", message = "Nie wybrano żadnej odpowiedzi!")
    else:
        twoje_odp.append(odp.get())
        start(ramka_pytania)


#%%
def oblicz_samopoczucie():
    
    ocena_sen1 = 0
    for i in range(5):
        if(twoje_odp[0] == odpowiedzi_sen[0][i]):
            ocena_sen1 = i+1
    ocena_sen2 = int(twoje_odp[1])
    ocena_sen3 = int(twoje_odp[2])
    ocena_sen = ocena_sen1+ocena_sen2+ocena_sen3
    
    ocena_akt1=0
    for i in range(5):
        if(twoje_odp[3]==odpowiedzi_aktywnosc[0][i]):
            ocena_akt1 = i+1
    ocena_akt2 = 0
    for i in range(5):
        if(twoje_odp[4]==odpowiedzi_aktywnosc[1][i]):
            ocena_akt2 = i+1
    ocena_akt3 = int(twoje_odp[5])
    ocena_aktywnosc = ocena_akt1 + ocena_akt2 + ocena_akt3
    ocena_urz1 = 0
    for i in range(5):
        if(twoje_odp[6]==odpowiedzi_urzadzenia[0][i]):
            ocena_urz1 = i+1
    ocena_urz2 = 0
    for i in range(5):
        if(twoje_odp[7]==odpowiedzi_aktywnosc[1][i]):
            ocena_urz2 = i+1
    ocena_urz3 = 0
    for i in range(5):
        if(twoje_odp[8]==odpowiedzi_aktywnosc[2][i]):
            ocena_urz3 = i+1
    ocena_urzadzenia = ocena_urz1 + ocena_urz2 + ocena_urz3
    ocena_dieta1 = 0
    for i in range(5):
        if(twoje_odp[9]==odpowiedzi_dieta[0][i]):
            ocena_dieta1 = i+1
    ocena_dieta2 = 0
    for i in range(5):
        if(twoje_odp[10]==odpowiedzi_aktywnosc[1][i]):
            ocena_dieta2 = i+1
    ocena_dieta3 = 0
    for i in range(5):
        if(twoje_odp[11]==odpowiedzi_aktywnosc[2][i]):
            ocena_dieta3 = i+1
    ocena_dieta = ocena_dieta1+ ocena_dieta2+ocena_dieta3
    ocena_kontakty1 = 0
    for i in range(5):
        if(twoje_odp[12]==odpowiedzi_kontakty[0][i]):
            ocena_kontakty1 = i+1
    ocena_kontakty2 = 0
    for i in range(5):
        if(twoje_odp[13]==odpowiedzi_kontakty[1][i]):
            ocena_kontakty2 = i+1
    ocena_kontakty3 = int(twoje_odp[14])
    ocena_kontakty = ocena_kontakty1+ocena_kontakty2+ocena_kontakty3
    
    intercept = -105.4690
    b_sen = 1.5224
    b_dieta = 2.3292
    b_aktywnosc = 1.4130
    b_urzadzenia = -1.6513
    b_kontakty = 5.5768
    
    samopoczucie = intercept + b_sen*ocena_sen + b_dieta*ocena_dieta + b_aktywnosc * ocena_aktywnosc + b_urzadzenia*ocena_urzadzenia + b_kontakty*ocena_kontakty
    
    samopoczucie = round(samopoczucie, 2)
    
    opis=""
    zdjecie=""
    if(samopoczucie<=-40):
        opis = "złe"
        zdjecie = "zle.png"
        bg='red'
    elif(samopoczucie>-40 and samopoczucie<=-20):
        opis = "kiepskie"
        zdjecie = "kiepskie.png"
        bg='orange'
    elif(samopoczucie>-20 and samopoczucie<3):
        opis = "przeciętne"
        zdjecie = "przecietne.png"
        bg='yellow'
    elif(samopoczucie>=3 and samopoczucie<20):
        opis = "dobre"
        zdjecie = "dobre.png"
        bg = 'pale green'
    else:
        opis = "świetne"
        zdjecie = "swietne.png"
        bg= 'green'
    wynik = []
    wynik.append(samopoczucie)
    wynik.append(opis)
    wynik.append(zdjecie)
    wynik.append(bg)
    return wynik
        






#%%

HEIGHT = 600
WIDTH = 600

okno = tk.Tk()
okno.title("Oceń swoje samopoczucie!")
okno.call('wm', 'iconphoto', okno._w, tk.PhotoImage(file='smiley.png'))
canvas = tk.Canvas(okno, height = HEIGHT, width = WIDTH)
canvas.pack()

ramka_startu = tk.Frame(okno, bd = 5)
ramka_startu.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
czy_gotowy = tk.Label(ramka_startu, text = "Oceń swoje samopoczucie!")
czy_gotowy.config(font=(44))
przycisk_start = tk.Button(ramka_startu, text = "START", command = lambda:start(ramka_startu), bg="green")
przycisk_start.config(font=(44))
czy_gotowy.pack(fill = "both", expand = "yes")
przycisk_start.pack(fill = "both", expand = "yes")



okno.mainloop()