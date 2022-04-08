def criar_arquivo(nome_arquivo):
    arquivo = open  (nome_arquivo, 'w') 
    arquivo.write('Cesar,10,10,8,9\nIsis,10,10,9,9\nNany,8,7,6,8\nLuiza,7,8,7,7')

def atualizar_arquivo(nome_arquivo):
    arquivo = open  (nome_arquivo, 'a') 
    arquivo.write('\n\nCesar,10,10,8,9\nIsis,10,10,9,9\nNany,8,7,6,8\nLuiza,7,8,7,7')

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

if __name__ == '__main__':
    # criar_arquivo('notas_alunos.txt')
    # atualizar_arquivo('notas_alunos.txt')
    # ler_arquivo('notas_alunos.txt')
    lista_media = media('notas_alunos.txt')
    print(lista_media)



