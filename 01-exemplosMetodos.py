def exibirMensagem():
    print("Olá, tudo bem?")
 #   print("Estou no método ...")
    
#exibirMensagem()
#print("Até Logo!")

#def retornaValor(y):
 #   return y, 2*y, 3*y, 4*y
#print(retornaValor('joão'))


def somaDoisValores(a, b):
    print('Iniciando a soma de valores ...')
    result = a + b 
    print('Sua soma foi realizada com sucesso')
    return result 
n1 = float (input("Entre com o 1o Valor"))
n2 = float (input("Entre com o 2o Valor"))

print("A soma dos valores é:", somaDoisValores(n1, n2))