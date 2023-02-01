#megoldas
def eredmeny(jPont, gPont):
    if osszegzes(jPont) > 21:
        return "Játékos vesztett"
    elif osszegzes(gPont) > 21:
        return "Gép vesztett"

def osszegzes(lista):
    i = 0
    osszeg = 0
    while i < len(lista):
        osszeg += lista[i]
        i += 1
    return osszeg
#teszt esetek
