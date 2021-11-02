print("inceput lab 3")
import itertools


def  get_longest_div_k(lst: list[int], k: int) -> list[int]:
    listamaxima = []
    #for element in lst:
    numarElemente = len(lst)
    i = 0
    while i < numarElemente:
        listanrdivizibilecuk = []
        while i < numarElemente and lst[i] % k == 0:
            listanrdivizibilecuk.append(lst[i])
            i = i+1
        if len(listanrdivizibilecuk) > len(listamaxima):
            listamaxima = listanrdivizibilecuk
        i = i+1
    return listamaxima

def test_get_longest_div_k():
    lista = [ 1, 2, 3 , 4, 6, 5, 4, 8, 10]
    k = 2
    rezultat=get_longest_div_k(lista, k)
    assert(rezultat == [4,8,10])

def is_prime(n):
    if n > 1:
        for i in range(2, int(n / 2) + 1):
            if (n % i) == 0:
                return 0
        return 1
    else:
        return 0

def test_is_prime():
    nr = 17
    rezultat = is_prime(nr)
    assert(rezultat == 1)

    nr = 18
    rezultat = is_prime(nr)
    assert(rezultat == 0)

def concatenare(lista) -> int:
    stringFinal = ""
    for element in lista:
        elementStr = str(element)
        stringFinal = stringFinal + elementStr
    if stringFinal != "":
        return int(stringFinal)
    return 0

def test_concatenare():
    lista=[1,2,3,4,5]
    rezultat=concatenare(lista)
    assert( rezultat == 12345 )
    lista = []
    rezultat=concatenare(lista)
    assert(rezultat == 0)

def get_longest_concat_is_prime(lst: list[int]) -> list[int]:
    listamaxima = []
    for L in range(0, len(lst) + 1):
        for subset in itertools.combinations(lst, L):
            if is_prime(concatenare(subset)):
                if len(subset) > len(listamaxima):
                    listamaxima = subset
    return listamaxima

def test_get_longest_concat_is_prime():
    lista=[1,2,3,4,5]
    rezultat = get_longest_concat_is_prime(lista)
    assert(rezultat == (1,3))


def citireLista():
    #aceasta functie citeste numarul de elemente si apoi elementele de la tastatura
    lista = []
    numarElemente=int(input("Numar elemente lista:"))
    for i in range (0,numarElemente):
        element=float(input("Valoare:"))
        lista.append(element)
    return lista

def printMenu():
    #am definit meniul cu toate functiile sale de apel,incluzand si o functie de exit ,spre incheierea programului
    print('0. Iesire')
    print('1. Citire date')
    print('2. Determinare cea mai lunga subsecventa cu proprietatea ca toate numerele sunt divizibile cu k (citit).')
    print('3. Determinare cea mai lunga subsecventa cu proprietatea ca ,concatenarea numerelor din subsecvență este număr prim.')
    print('4. Teste')

listaCitita= []

if __name__ == '__main__':
    printMenu()
    numar = int(input("Apeleaza un numar de comanda din lista de mai sus:"))
    while (numar != 0):
        if numar == 1:
            listaCitita = citireLista()
            print(listaCitita)
        if numar == 2:
            k = int(input("scrie numarul cu care vrei sa verifici divizibilitatea nr.din lista:"))
            print(get_longest_div_k(listaCitita,k))
        if numar == 3:
            print(get_longest_concat_is_prime(listaCitita))
        if numar == 4:
            test_get_longest_div_k()
            test_get_longest_concat_is_prime()
            test_is_prime()
            test_concatenare()
            print('Am rulat testele')
        printMenu()
        numar = int(input("Apeleaza un numar de comanda din lista de mai sus:"))

