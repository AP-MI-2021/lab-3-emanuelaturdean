import math
print("inceput lab 3")

def functie(numbers : list[int]) -> list[int]:
    return numbers
def  get_longest_div_k(lst: list[int], k: int) -> list[int]:
    listanrdivizibilecuk = []
    for element in lst:
        if element % k == 0:
            listanrdivizibilecuk.append(int(element))
    # print(listanrdivizibilecuk)
    return listanrdivizibilecuk
def get_longest_concat_is_prime(lst: list[int]) -> list[int]:
    listasiruri=''
    for element in lst:
        element=str(element)
        listasiruri=listasiruri + element
    listasiruri=int(listasiruri)
    

# print(functie([1,2,3]))
def citireLista():
    #aceasta functie citeste numarul de elemente si apoi elementele de la tastatura
    lista = []
    numarElemente=int(input("Numar elemente lista:"))
    for i in range (0,numarElemente):
        element=float(input("Valoare:"))
        lista.append(element)
def printMenu():
    #am definit meniul cu toate functiile sale de apel,incluzand si o functie de exit ,spre incheierea programului
    print('1.Citire date')
    print('2.Determinare ceamai lunga subsecventa cu proprietatea ca toate numerele sunt divizibile cu k (citit).')
    print('3.Determinare cea mai lunga subsecventa cu proprietatea ca ,concatenarea numerelor din subsecvență este număr prim.')
    print('4.Iesire')
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
            get_longest_div_k(listaCitita,k)

