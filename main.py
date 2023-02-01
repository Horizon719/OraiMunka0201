#megoldas
def eredmeny(jLapok: list[int], gLapok: list[int]):
    if osszegzes(jLapok) > 21:
        return "Játékos vesztett"
    elif osszegzes(gLapok) > 21:
        return "Gép vesztett"


def osszegzes(lista: list[int]):
    i = 0
    osszeg = 0
    while i < len(lista):
        osszeg += lista[i]
        i += 1
    return osszeg
#teszt esetek


def jatekos_vesztett_teszt():
    jLapok = [10, 5, 7]
    gLapok = [2, 7, 9]
    kapott = eredmeny(jLapok, gLapok)
    vart = "Játékos vesztett"
    if kapott == vart:
        print("A teszt sikeres")
    else:
        print("A teszt megbukott")


def gep_vesztett_teszt():
    jLapok = [10, 5, 4]
    gLapok = [6, 7, 10]
    kapott = eredmeny(jLapok, gLapok)
    vart = "Gép vesztett"
    if kapott == vart:
        print("A teszt sikeres")
    else:
        print("A teszt megbukott")



def dontetlen_teszt():
    jLapok = [10, 5, 7]
    gLapok = [6, 7, 9]

    if osszegzes(jLapok) == osszegzes(gLapok):
        print("A teszt sikeres")
    else:
        print("A teszt megbukott")

def tesztek():
    jatekos_vesztett_teszt()
    gep_vesztett_teszt()
    dontetlen_teszt()


tesztek()
