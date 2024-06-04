def cadastrar_notas(alunos):
    nome = input("Digite o nome do aluno: ")
    notas = []
    for i in range(4):
        nota = float(input(f"Digite a nota {i+1} do aluno: "))
        notas.append(nota)
    alunos[nome] = notas

def calcular_media(notas):
    return sum(notas) / len(notas)

def mostrar_notas(alunos):
    for nome, notas in alunos.items():
        media = calcular_media(notas)
        situacao = "Aprovado" 
        if media >= 5 else "Reprovado"
        print(f"Aluno: {nome}, Notas: {notas}, Média: {media}, Situação: {situacao}")

alunos = {}

while True:
    print("\nMenu:")
    print("1. Cadastrar notas de um aluno")
    print("2. Mostrar notas cadastradas")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar_notas(alunos)
    elif opcao == "2":
        mostrar_notas(alunos)
    elif opcao == "3":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")