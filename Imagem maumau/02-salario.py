mes = ["jan", "fev", "mar","abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]

totalSalario = 0 

for i in range (12):
    salario = float(input("Digite o sálario de %s em R$:"%mes[i]))
    totalSalario = totalSalario + salario
    
decimoTerceiro = (totalSalario / 12)
tercoFerias = (totalSalario / 12)* (1/3)

print ("O decimo terceiro salário é:", decimoTerceiro)
print ("O terço das fé rias corresponde á:", tercoFerias)
