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
