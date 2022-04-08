import hashlib
from hmac import digest

# arquivo = open('b.txt', 'w')
# arquivo.write('Python para segurançã da informação')

arquivo1='a.txt'
arquivo2='b.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(arquivo1,'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2,'rb').read()) #gera i hash

if hash1.digest() != hash2.digest():
    print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}')
else: 
    print(f'O arquivo: {arquivo1} é igual ao arquivo: {arquivo2}')

print(hash1.hexdigest)
print(hash2.hexdigest)



