numero1: int
numero2: int
operacao: int



numero1 = int(input('Digite o primeiro número: '))
numero2 =int(input('Digite o segundo número: '))

# operação == 1 // soma
# operação == 2 // sub

operacao = int(input('Você gostaria de somar (1) ou subtrair (2)? '))

#print(numero1, numero2, operacao)

# Espaço que aparece abaixo do if chama-se identação, quer dizer que tudo que está identado está dentro do if.

if operacao == 1:
  soma: int = numero1 + numero2
  print(numero1, '+', numero2, '=', soma)

else :
  sub: int = numero1 - numero2
  print(numero1, '-', numero2, '=', sub)


if operacao == 1 :
  soma: int = numero1 + numero2
  print(numero1, '+', numero2, '=', soma)

if operacao == 2 :
  sub: int = numero1 - numero2
  print(numero1, '-', numero2, '=', sub)

print('tchau!')
