LA_MIA_COSTANTE=67

class LaMiaClasse:
    def __init__(self, attributo):
        self.__attributo = attributo
    def funzione(self):
        print('Funzione invocata')

if __name__ == '__main__':
    prova=LaMiaClasse(65)
    prova.funzione()