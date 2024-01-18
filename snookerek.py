from Snooker import Snooker

snookerek:list[Snooker]=[]

def beolvas(fajlnev):
    fajl=open(fajlnev,'r',encoding='UTF8')
    fajl.readline()
    for sor in fajl:
        snookerek.append(sor.strip())
    fajl.close()

def versenyzo_bevetel():
    osszeg=0
    for s in snookerek:
        osszeg+=s.nyeremeny
    return osszeg/len(snookerek)

def legjobb_versenyzo():
    legjobb=snookerek[0].nyeremeny
    rec=None
    for s in snookerek:
        if s.orszag=='Kína':
            if s.nyeremeny>legjobb:
                legjobb=s.nyeremeny
                rec=s
    return rec

def versenyzo_keres(orszag):
    for s in snookerek:
        if s.orszag==orszag:
            return False
    return True

def statisztika():
    stat={}
    for s in snookerek:
        if s.orszag in stat.keys():
            stat[s.orszag]+=1
        else:
            stat[s.orszag]=1
    return stat

    
