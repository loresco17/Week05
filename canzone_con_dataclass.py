from dataclasses import dataclass

@dataclass(eq=True, order=True)
class Canzone:
    _titolo:str
    _artista:str
    _anno:int (compare=False)
    _durata:str

c=Canzone('T', 'A', 1999, '5:23')
print(c)