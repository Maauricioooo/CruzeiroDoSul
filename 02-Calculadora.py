def SomaDeValores (a,b):
    return a + b

def Subtração (a,b): 
    return a - b

def Mutiplicação (a,b):
    return a * b

def Divisão (a,b):
    return a /  b

n1 = float (input("Entre com o 1o Valor:"))
n2 = float (input("Entre com o 2o Valor:"))

operacao = input("Digite a operação desejada(+,-,*,/)")

if operacao == "+":
    resultado = SomaDeValores (n1,n2)

elif operacao == "-": 
    resultado = Subtração (n1,n2)
    
elif operacao == "*": 
    resultado = Mutiplicação (n1,n2)

elif operacao == "/": 
    resultado = Divisão (n1,n2)
    
else:
    print("operacao invalida")
    
print("O resultado da operação solicitada é", resultado)