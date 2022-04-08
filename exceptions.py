lista = [1,10]
try:
    arquivo = open('notas_alunos.txt', 'r')
    divisão = 10/0
    numero = lista[1]


except ZeroDivisionError: 
    print('Não é possivel divisão por zero')
except IndexError:
    print('indice inválido')
except BaseException as ex: #erro generico
    print('erro desconhecido: {}' .format(ex))
else: 
    print('Executa quando não houve exceção')
finally:
    print('Sempre executa')
    arquivo.close()
    print('fechando arquivo')



