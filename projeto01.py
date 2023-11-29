import math

def calcular_combinacoes(N, M):
    combinacoes = math.factorial(N) / (math.factorial(M) * math.factorial(N - M))
    return int(combinacoes)

# Obter entrada do usuário
N = int(input("Digite o valor de N (número total de alunos): "))
M = int(input("Digite o valor de M (número de alunos em um dos grupos): "))

# Calcular e imprimir o número de combinações
resultado_combinacoes = calcular_combinacoes(N, M)
print(f"O número de combinações possíveis é: {resultado_combinacoes}")
