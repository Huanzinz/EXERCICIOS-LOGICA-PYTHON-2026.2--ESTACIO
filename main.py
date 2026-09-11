# Questão 01 — Cadastro e apresentação de perfil pessoal
print("=== CADASTRO DE IDENTIFICAÇÃO ===")
# Entrada e validação do nome
nome = input("Digite seu nome completo: ").strip()
# Entrada e validação da idade
while True:
    idade = input("Digite a sua idade: ")

    try:
         idade = int(idade)

         if idade >= 0:
              break
         else:
              print("Erro: a idade deve ser um valor inteiro não negativo")
    except ValueError:
        print("Erro: informe a idade usando um número inteiro.")
# Entrada e validação da altura
while True:
    altura = input("Digite a sua altura em metros: ").strip()
    try:
         altura = float(altura.replace(",", "."))

         if altura > 0:
              break
         else:
              print("Erro: a altura deve ser um valor positivo")
    except ValueError:
        print("Erro: informe a altura usando um valor númerico.")
# Entrada da cidade
cidade = (input("Digite a cidade onde reside: ")).strip()
# Exibição do cartão
print("=======CARTÃO DE IDENTIFICAÇÃO=======")
print(f"{'Nome completo:':<18} {nome}")
print(f"{'Idade:':<18} {idade} anos")
print(f"{'Altura:':<18} {altura:.2f} m")
print(f"{'Cidade:':<18} {cidade}")
print("=" * 42)
