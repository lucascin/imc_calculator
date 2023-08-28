# Calculadora de Índice de Massa Corporal

def calculate_IMC(weight, height):
    imc_return = weight / (height * height)
    return imc_return

altura = float(input("Insira sua altura: \n"))
peso = float(input("Insira o seu peso: \n"))
imc = calculate_IMC(peso, altura)

print("O IMC baseado na altura " + str(altura) + " e no peso " + str(peso) + " é igual a: " + imc)