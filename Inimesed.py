from ModuleInimesed import *

arv=input("Kui palju inimesed sa soovid lisada? ")
while arv.isdigit()==False:
    arv=input("Kirjuta õige arv ")
ListIni,ListPikk=inimesed(int(arv))

while True:
    menu=input("""
    0-Kuva nimekirjad
    1-Eemalda nimekirjast isik ja andmed tema pikkuse kohta, sisestades isiku nime
    2-Sorteeri nimed
    3-Leidke inimestest kõrgeim ja madalaim
    4-Leia loendist n inimese keskmine pikkus, inimeste nimed sisestab kasutaja
    5-Sorteeri numbreid
    """)
    print()
    if menu=="0":
        print(ListIni,ListPikk)
    elif menu=="1":
        ListIni,ListPikk=kustunimi(ListIni,ListPikk)
    elif menu=="2":
        ListIni,ListPikk=sortAlph(ListIni,ListPikk)
        print(ListIni,ListPikk)
    elif menu=="3":
        mima(ListIni,ListPikk)
    elif menu=="4":
        keskNi(ListIni,ListPikk)
    elif menu=="5":
        ListIni,ListPikk=sortNum(ListIni,ListPikk)
        print(ListIni,ListPikk)
    else:
        print("Kirjuta pakutavad numbrid ")