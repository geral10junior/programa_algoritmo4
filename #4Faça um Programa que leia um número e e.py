#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
print('Digite um número de 1 à 7, e o programa irá informar qual dia da semana se corresponde')
numero = int(input('Informe o número '))
if numero == 1:
    print('Domingo')
elif numero== 2:
    print('Segunda')    
elif numero== 3:
    print('Terça') 
elif numero== 4:
    print('Quarta')
elif numero== 5:
    print('Quinta') 
elif numero== 6:
    print('Sexta')
elif numero== 7:
    print('Sábado')
else:
    print('Valor inválido')