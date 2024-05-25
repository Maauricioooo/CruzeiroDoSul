numero = []
soma = 0

print ("Digite qunatas notas quiser.")
print ("Digite 0 para sair do sistema.")


while True: 
    n = float ( input("Digite uma nota:"))
    if (n == 0):
        break
    numero.append(n)
    soma +=n
    
media = soma/len(numero)
print("media %.2f" %media)
print ("Notas digitadas:", )