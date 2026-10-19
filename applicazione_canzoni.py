from operator import attrgetter

from canzone import Canzone
c1=Canzone('Someone like you', 'Adele', 2011, '3:11')
c2=Canzone('Yellow Submarine', 'The Beatles', 1966, '4:01')
c3=Canzone('Scrivile scemo', 'Pinguini Tattici Nucleari', 2020, '2:30')
c4=Canzone('Someone like you', 'Altro artista', 2011, '3:11')

if c1==c4:
    print('Le canzoni sono uguali')
else:
    print('Le canzoni sono diverse')

lista=[c1,c2,c3]
lista.append(Canzone('Nuova Canzone', 'Ciao', 1966, '1:23'))

print("Lista canzoni ordinate per anno")
lista_ordinata=sorted(lista)
for c in lista_ordinata:
    print(c)

print("\nLista canzoni ordinate per titolo")
lista_ordinata2=sorted(lista_ordinata, key=attrgetter('_titolo'), reverse=True)
for c in lista_ordinata2:
    print(c)

print("\nLista canzoni ordinate per artista")
lista_ordinata3=sorted(lista_ordinata, key=lambda canzone: canzone._artista)
for c in lista_ordinata3:
    print(c)