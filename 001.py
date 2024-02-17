n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2

#PRINT COM FORMAT
#Format vai adicionar o respectivos números em sequencia nos {}
print ('A soma entre {} e {} é de {}'.format(n1,n2,s)) 
print ('Sucessor de {} é {}'.format(n1, (n1+1)))
print ('Antecessor de {} é {}'.format(n1, (n1-1)))
print ('Sucessor de {} é {}'.format(n2, (n2+1)))
print ('Antecessor de {} é {}'.format(n2, (n2-1)))
print ('Sucessor do resultado {} é {}'.format(s, (s+1)))
print ('Antecessor do resultado {} é {}'.format(s, (s-1)))
exit

#Remover index.lock para funcionar .git/index.lock