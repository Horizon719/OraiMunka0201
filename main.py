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
        print("A játékos_vesztett_teszt sikeres")
    else:
        print("A játékos_vesztett_teszt megbukott")


def jatekos_vesztett_teszt2():
    jLapok = [10, 1, 7]
    gLapok = [5, 7, 9]
    kapott = eredmeny(jLapok, gLapok)
    vart = "Játékos vesztett"
    if kapott == vart:
        print("A játékos_vesztett_teszt2 sikeres")
    else:
        print("A játékos_vesztett_teszt2 megbukott")


def jatekos_vesztett_teszt3():
    jLapok = [8, 5, 6]
    gLapok = [10, 11]
    kapott = eredmeny(jLapok, gLapok)
    vart = "Játékos vesztett"
    if kapott == vart:
        print("A játékos_vesztett_teszt3 sikeres")
    else:
        print("A játékos_vesztett_teszt3 megbukott")


def gep_vesztett_teszt():
    jLapok = [10, 5, 4]
    gLapok = [6, 7, 10]
    kapott = eredmeny(jLapok, gLapok)
    vart = "Gép vesztett"
    if kapott == vart:
        print("A gép_vesztett_teszt sikeres")
    else:
        print("A gép_vesztett_teszt megbukott")


def gep_vesztett_teszt2():
    jLapok = [9, 1, 7]
    gLapok = [5, 7, 10]
    kapott = eredmeny(jLapok, gLapok)
    vart = "Gép vesztett"
    if kapott == vart:
        print("A gép_vesztett_teszt2 sikeres")
    else:
        print("A gép_vesztett_teszt2 megbukott")


def gep_vesztett_teszt3():
    jLapok = [10, 11]
    gLapok = [8, 5, 6]
    kapott = eredmeny(jLapok, gLapok)
    vart = "Gép vesztett"
    if kapott == vart:
        print("A gép_vesztett_teszt3 sikeres")
    else:
        print("A gép_vesztett_teszt3 megbukott")


def dontetlen_teszt():
    jLapok = [10, 5, 7]
    gLapok = [2, 7, 9]
    kapott = eredmeny(jLapok, gLapok)
    vart = "Döntetlen vesztett"
    if kapott == vart:
        print("A döntetlen_teszt sikeres")
    else:
        print("A döntetlen_teszt megbukott")


def dontetlen_teszt2():
    jLapok = [5, 6, 10]
    gLapok = [11, 4, 6]
    kapott = eredmeny(jLapok, gLapok)
    vart = "Döntetlen vesztett"
    if kapott == vart:
        print("A döntetlen_teszt2 sikeres")
    else:
        print("A döntetlen_teszt2 megbukott")


def dontetlen_teszt3():
    jLapok = [8, 9]
    gLapok = [10, 7]
    kapott = eredmeny(jLapok, gLapok)
    vart = "Döntetlen vesztett"
    if kapott == vart:
        print("A döntetlen_teszt3 sikeres")
    else:
        print("A döntetlen_teszt3 megbukott")


def tesztek():
    jatekos_vesztett_teszt()
    jatekos_vesztett_teszt2()
    jatekos_vesztett_teszt3()
    gep_vesztett_teszt()
    gep_vesztett_teszt2()
    gep_vesztett_teszt3()
    dontetlen_teszt()
    dontetlen_teszt2()
    dontetlen_teszt3()


tesztek()
