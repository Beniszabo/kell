from hegycsucs import hegycsucs

hegyek:list[hegycsucs]=[]

def beolvas(fajlnev):
    fajl=open(fajlnev,'r',encoding='utf8')
    fajl.readline()
    for sor in fajl:
        hegyek.append(hegycsucs(sor.strip()))
    fajl.close()

def hegyek_szama(): # ha mindent fgv-nyel kell megoldani
    return len(hegyek)

def atlag_magassag()->float:
    osszeg=0
    for h in hegyek:
        osszeg+=h.magassag
    return osszeg/hegyek_szama()  # lehetne len(hegyek) is

def legmagasabb_hegy() ->hegycsucs: # visszaad egy példányt
    legmagasabb=hegyek[0]
    for h in hegyek[1:]:
        if h.magassag>legmagasabb.magassag:
            legmagasabb=h
    return legmagasabb

def van_magasabb(magassag)->bool|str:
    for h in hegyek:
        if h.magassag>magassag:
            return h.nev
    return False

