print ('Bem Vindo a SmartCalculator')
print ('Qual operação você deseja realizar?')
print ('1 - Adição')
print ('2 - Subtração')
print ('3 - Multiplicação')
print ('4 - Divisão')
print ('5 - Porcentagem')
op = input()
lista = []

#Adição
if op == '1':
    var = 0
    while var != 'f':
      print ('Digite os numeros a serem somados:')
      print ('Digite F para finalizar a soma')
      var = input()
      if var != 'f':
        lista.append(float(var))
    else:
        soma = sum(lista)
        print('O Total da soma é:' , soma)

#Subtração
if op == '2':
    var = 0
    subtracao = 0
    while var != 'f':
      print ('Digite os numeros a serem subtraidos:')
      print ('Digite F para finalizar a subtracao')
      var = input()
      if var != 'f':
        lista.append(float(var))
    else:
        num1 = lista.pop(0)
        soma = sum(lista)
        print('O Total da Subtração é:' , num1 - soma)

#Multiplicação
if op == '3':
    var = 0
    multiplicacao = 1
    while var != 'f':
      print ('Digite os numeros a serem multiplicados:')
      print ('Digite F para finalizar a multiplicação')
      var = input()
      if var != 'f':
        lista.append(float(var))
    else:
        for m in lista:
          multiplicacao *= m
        print('O Total da Multiplicação é:' , multiplicacao)



#Divisão
if op == '4':
    num1 = float(input('Digite o Primeiro Numero:'))
    num2 = float(input('Digite o Segundo Numero:'))
    print('Divisão =' , num1 / num2)
    print('Divisão Inteira=' , num1 // num2)
    print('Resto da Divisão=' , num1 % num2)

#Porcentagem
if op == '5':
    num1 = float(input('Digite o Numero:'))
    num2 = float(input('Qual a porcentagem que deseja extrair?:'))
    total = num1 * (num2 / 100)
    print(num2 , '% de' , num1 , 'é igual a:' , total)

else:
  print ('Opção Invalida, Reinicie o Programa')
