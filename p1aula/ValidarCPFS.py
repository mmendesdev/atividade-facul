#algoritimo para validar CPF
cpf = int(input("Digite seu CPF: "))
nove_digitos = cpf[:9] #pegar os noves digitos do cpf
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) + contador_regressivo_1
    contador_regressivo_1 -= 1
