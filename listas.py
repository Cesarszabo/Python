lista = [1,2,3,4,5]
tupla = (1,2,3,4,5) # igual a lista porem imutavel
conjunto = {1,2,3,4,5} # ou set - não imprime valores duplicados

conjLista = set(lista) # conversão de lista para conjunto
listaConj = list(conjunto) # conversão para lista
tuplaList = tuple(lista) # conversão para tupla

print(type(tuplaList))
