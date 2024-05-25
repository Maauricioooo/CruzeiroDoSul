notas = []
soma = 0 



n = int ( input("Digite a quantidade de notas que seja inserir:"))

for i in range (n):
    nota = float(input("Digite a %dª nota:" %i))
    notas.append(notas)
    soma+=notas
    
print("Notas inseridas:", notas)
media = soma/n 
print("média: %.2f" %media)