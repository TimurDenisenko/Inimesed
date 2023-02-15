def inimesed(x:int):
    """Kasutaja sisestas, mitu inimest
    lisada (arv x), misjärel loendid
    funktsioonis täidetakse (inimesed ja pikkus).
    :param int x: Kui palju lisada inimeste
    :rtype:list,list
    """
    ini=[] 
    pikk=[]
    for i in range(x):
        nimi=input("Millise inimese soovite lisada? (Kirjuta nimi) ").title()
        while nimi.isdigit() or len(nimi)==1 or len(nimi)>30:
            nimi=input("Kirjuta õige nimi ").title()
        ini.append(nimi)
        pikkus=input("Kui pikk ta on? ")
        while pikkus.replace(".","",1).isdigit()==False or 70>float(pikkus) or 250<float(pikkus):
            pikkus=input("Kirjuta õige pikkus ")
        pikk.append(float(pikkus)) 
    return ini,pikk 

def kustunimi(x:list,y:list):
    """Kasutaja sisestab nime, mille
    järel funktsioon eemaldab tema nime ja pikkuse.
    :param list x: Inimeste järjend
    :param list y: Pikkus järjend
    :rtype:list,list
    """
    vali=input("Kas sa tahad eemalda mõne inimesed? (jah või ei) ").lower()
    while vali not in ["jah","ei"]:
        vali=input("Kirjuta ainult jah või ei ").lower()
    if vali=="jah":
        arv=input("Kui palju inimesed sa tahad eemalda? ")
        while arv.isdigit()==False or arv=="0" or int(arv)>len(x):
            arv=input("Kirjuta õige arv! ")
    else:
        arv=1
    arv=int(arv)
    for i in range(arv):
        nimi=input("Palun kirjuta nimi mis tahad eemalda ").title()
        while nimi not in x:
            nimi=input("Palun kirjuta õige nimi ").title()
        ind=x.index(nimi)
        x.pop(ind)
        y.pop(ind)
    return x,y

def sortAlph(x:list,y:list):
    """Funktsioon võimaldab kuvada
    tähestikulises järjekorras inimeste
    nimesid ja nende pikkust. Ja ka vastupidises
    järjekorras.
    :param list x: Inimeste järjend
    :param list y: Pikkus järjend
    :rtype:list,list
    """
    sorti=input("Millises järjekorras soovite sorteerida? (Nimed (A–Z või Z–A)) ").lower()
    while sorti not in ["a-z","z-a"]:
        sorti=input("Kirjutage sellest ainult osa: A–Z või Z–A").lower()
    if sorti in ["a-z","z-a"]:
        for p in range(0,len(x)):
            for o in range(0,len(x)):
                if x[p]<x[o]:
                    abi=x[p]
                    x[p]=x[o]
                    x[o]=abi
                    abi=y[p]
                    y[p]=y[o]
                    y[o]=abi 
        if sorti=="z-a":
            x.reverse()
            y.reverse()
    return x,y 

def mima(x:list,y:list):
    """Funktsioon otsib kõige pikemat
    ja lühemat inimest, kuvades samal
    ajal tema pikkuse ja nime
    :param list x: Inimeste järjend
    :param list y: Pikkus järjend
    """
    indMi=y.index(min(y)) 
    indMa=y.index(max(y))
    print(f"Lühim inimesed on {x[indMi]}, tema pikkus on {y[indMi]}. Kõige pikem mees on {x[indMa]}, tema pikkus on {y[indMa]}.")

def keskNi(x:list,y:list): 
    """Kasutaja sisestab nimed, mille
    hulgast ta soovib leida keskmist kõrgust
    ja funktsioon teeb seda
    :param list x: Inimeste järjend
    :param list y: Pikkus järjend
    """
    summa=0
    arv=input("Mitme inimese vahelt me ​​keskmist pikkust otsime? ")
    while arv.isdigit()==False or arv=="0" or int(arv)>len(x):
        arv=input("Kirjuta õige arv ")
    for i in range(int(arv)):
        nimi=input("Kirjuta nimi ")
        while nimi not in x:
            nimi=input("Kirjuta õige nimi ")
        ind=x.index(nimi) 
        summa+=y[ind] 
    keskmine=summa/int(arv)
    print(f"Nende inimeste keskmine pikkus on {keskmine}")

def sortNum(x:list,y:list):
    """Funktsioon sorteerib numbrid
    kasvavas või kahanevas järjekorras.
    :param list x: Inimeste järjend
    :param list y: Pikkus järjend
    """
    sorti=input("Millises järjekorras soovite sorteerida? (Kasvas või kahanev) ").lower()
    while sorti not in ["kasvas","kahanev"]:
        sorti=input("Kirjutage sellest ainult osa: kasvas,kahanev").lower()
    for p in range(0,len(x)):
        for o in range(0,len(x)):
            if y[p]<y[o]:
                abi=y[p]
                y[p]=y[o]
                y[o]=abi
                abi=x[p]
                x[p]=x[o]
                x[o]=abi 
    if sorti=="kahanev":
        x.reverse() 
        y.reverse() 
    return x,y 
