#megoldas
def eredmeny(jLapok: list[int], gLapok: list[int]):
    s = ""
    jossz = osszegzes(jLapok)
    gossz = osszegzes(gLapok)
    jdb = lapdb(jLapok)
    gdb = lapdb(gLapok)
    if jossz <= 21 and gossz <= 21:
        if jossz > gossz:
            s = "Gép vesztett"
        elif gossz > jossz:
            s = "Játékos vesztett"
        elif jossz == gossz:
            if jdb < gdb:
                s = "Gép vesztett"
            elif gdb > jdb:
                s = "Játékos vesztett"
            else:
                s = "Döntetlen"
    else:
        if jossz > 21:
            s = "Játékos vesztett"
        if gossz > 21:
            s = "Gép vesztett"
        if jossz > 21 and gossz > 21:
            s = "Döntetlen"
    return s


def osszegzes(lista: list[int]):
    i = 0
    osszeg = 0
    while i < len(lista):
        osszeg += lista[i]
        i += 1
    return osszeg


def lapdb(lista: list[int]):
    return len(lista)
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
    jLapok = [5, 7, 9]
    gLapok = [10, 1, 7]
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
    gLapok = [6, 7, 9]
    kapott = eredmeny(jLapok, gLapok)
    vart = "Döntetlen"
    if kapott == vart:
        print("A döntetlen_teszt sikeres")
    else:
        print("A döntetlen_teszt megbukott")


def dontetlen_teszt2():
    jLapok = [5, 6, 10]
    gLapok = [11, 4, 6]
    kapott = eredmeny(jLapok, gLapok)
    vart = "Döntetlen"
    if kapott == vart:
        print("A döntetlen_teszt2 sikeres")
    else:
        print("A döntetlen_teszt2 megbukott")


def dontetlen_teszt3():
    jLapok = [8, 9]
    gLapok = [10, 7]
    kapott = eredmeny(jLapok, gLapok)
    vart = "Döntetlen"
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
