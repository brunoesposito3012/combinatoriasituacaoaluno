def obter_status_aluno(media):
    if media > 6:
        return "Aprovado"
    elif 4 <= media <= 6:
        return "Verificação Suplementar"
    else:
        return "Reprovado"

# Obter a média do aluno
media_aluno = float(input("Digite a média do aluno: "))

# Obter e imprimir o status do aluno
status = obter_status_aluno(media_aluno)
print(f"O status do aluno é: {status}")