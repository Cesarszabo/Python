# metodo não retorna valor e função retorna valor 
# modulo cada arquivo .py - lambda - função anonima
from operator import truediv



class Televisao:
    def __init__ (self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada == True:
            self.ligada = False
        else:
            self.ligada = True
    
    def aumenta_canal(self):
        self.canal +=1
    def diminui_canal(self):
        self.canal -=1



televisao = Televisao()

print('televisão ligada: {}' .format(televisao.ligada))
televisao.power()
print('televisão ligada: {}' .format(televisao.ligada))
televisao.aumenta_canal()
televisao.aumenta_canal()
televisao.aumenta_canal()
televisao.diminui_canal()
print('canal: {}' .format(televisao.canal))

