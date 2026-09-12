----------------------------------------------------------
# Questão 01 — Cadastro e apresentação de perfil pessoal
print("======CADASTRO DE IDENTIFICAÇÃO======")
# Entrada do nome e cidade
nome = input("Digite seu nome completo: ")
cidade = input("Digite a cidade onde reside: ")
# Entrada e validação da idade
idade = int(input("Digite a sua idade: "))
while idade < 0:
    print("Erro: a idade não deve ser um valor negativo!")
    idade = int(input("Digite a sua idade novamente: "))
# Entrada e validação da altura
altura = float(input("Digite a sua altura em metros: "))
while altura <= 0:
    print("Erro: a altura deve ser um valor maior que zero!")
    altura = float(input("Digite a sua idade novamente: "))
# Exibição do cartão
print("=======CARTÃO DE IDENTIFICAÇÃO=======")
print(f"Nome completo: {nome}")
print(f"Idade: {idade} anos")
print(f"Altura: {altura:.2f} m")
print(f"Cidade: {cidade}")
------------------------------------------------------------------
# Questão 02 — Calculadora de operações aritméticas fundamentais
print("======CALCULADORA DE OPERAÇÕES ARITMÉTICAS======")
# Entrada dos dois números reais
num1 = float(input("Digite o seu primeiro numero: "))
num2 = float(input("Digite o seu segundo numero: "))
# Operações básicas que sempre funcionam
print(f"Adição (+): {num1 + num2}")
print(f"Subtração (-): {num1 - num2}")
print(f"Multiplicação (x): {num1 * num2}")
print(f"Potenciação (**): {num1 ** num2}")
# Operações com condições especiais 
if num2 != 0:
    print(f"Divisão (÷): {num1 / num2}")
    print(f"Divisão inteira (//): {num1 // num2}")
    print(f"Resto da divisão (%): {num1 % num2}")
else:
    print("Divisão (÷): Divisão por zero não permitida")
    print("Divisão inteira (//): Divisão por zero não permitida")
    print("Resto da divisão (%): Divisão por zero não permitida")
-------------------------------------------------------------------
# Questão 03 — Conversão entre escalas termométricas
# Solicitando a temperatura em celsius
Celsius = float(input("Digite a temperatura em celsius: "))
# Covertendo para as escalas Fahreheint e Kelvin
Fahrenheit = Celsius * 9/5 + 32
Kelvin = Celsius + 273.15
# Exibindo a conversão de temperatura
print("===TABELA DE CONVERSÃO DE TEMPERATURA===")
print(f"Celsius:            {Celsius:.2f} °C")
print(f"Fahrenheit:         {Fahrenheit:.2f} °F")
print(f"Kelvin:             {Kelvin:.2f} K")
-----------------------------------------------------------------------
# Questão 04 — Cálculo de média e determinação de situação acadêmica
# Solicitando a primeira nota
nota1 = float(input("Digite a primeira nota: "))
while nota1 < 0 or nota1 > 10:
    print("Erro! a primeira nota deve estar entre 0 e 10.")
    nota1 = float(input("Digite novamente a primeira nota: "))
# Solicitando a segunda nota
nota2 = float(input("Digite a segunda nota: "))
while nota2 < 0 or nota2 > 10:
    print("Erro! a segunda nota deve estar entre 0 e 10.")
    nota2 = float(input("Digite novamente a segunda nota: "))
# Solicitando a terceira nota
nota3 = float(input("Digite a terceira nota: "))
while nota3 < 0 or nota3 > 10:
    print("Erro! a terceira nota deve estar entre 0 e 10.")
    nota3 = float(input("Digite novamente a terceira nota: "))
# Calculando a média 
media = (nota1 + nota2 + nota3) / 3
# Verificando situação acadêmica do aluno
if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"
# Determinando e exibindo a situação acadêmica do aluno
print("==========RESULTADO==========")
print(f"nota1:           {nota1:.2f}")
print(f"nota2:           {nota2:.2f}")
print(f"nota3:           {nota3:.2f}")
print(f"media:           {media:.2f}")
print(f"situacao:        {situacao}")
---------------------------------------------------------------
# Questão 05 — Classificação etária com validação de entrada
# Solicitando a idade
idade = int(input("Digite a idade: "))
while idade < 0:
    print("Erro! a idade deve ser maior que 0.")
    idade = int(input("Digite novamente a idade: "))
# Classificando a idade
if idade <= 12:
    classificacao = "Criança"
elif idade <= 17:
    classificacao = "Adolescente"
elif idade <= 59:
    classificacao = "Adulto"
else:
    classificacao = "Idoso"
# Classificação etária
print("\n======CLASSIFICAÇÃO ETÁRIA======")
print(f"Idade:           {idade} anos")
print(f"Classificacao:   {classificacao}")
---------------------------------------------------------
# Questão 06 — Ordenação manual de três números inteiros
# Solicitando os três números inteiros
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
# Realizando a ordenação manual
if num1 > num2:
    if num1 > num3:
        maior = num1

        if num2 > num3:
            meio = num2
            menor = num3
        else:
            meio = num3
            menor = num2
    else:
        maior = num3
        meio = num1
        menor = num2
else:
    if num2 > num3:
        maior = num2

        if num1 > num3:
            meio = num1
            menor = num3
        else:
            meio = num3
            menor = num1
    else:
        maior = num3
        meio = num2
        menor = num1
# Exibindo os três números ordenados
print("\n======== RESULTADO ========")
print(f"Maior número:        {maior}")
print(f"Número intermediário: {meio}")
print(f"Número menor:        {menor}")
--------------------------------------------------------
# Questão 07 — Análise simultânea de sinal e paridade
# Solicitando o número inteiro
numero = int(input("Digite um número inteiro: "))
# Verificando se o número é positivo, negativo ou nulo.
if numero > 0:
    sinal = "positivo"
elif  numero < 0:
    sinal = "negativo"
else:
    sinal = "nulo"
# Verificando se o número é par ou ímpar
if numero % 2 == 0:
    paridade = "par"
else:
    paridade = "ímpar"

print(f"O número {numero} é {sinal} e {paridade}.")
--------------------------------------------------------------
# Questão 08 — Estatística descritiva de conjunto numérico
soma = 0
positivos = 0
negativos = 0
pares = 0
impares = 0
# Solicitando dez números inteiros ao usuáro
for i in range (10):
    numero = int(input("Digite um número: "))
# Verificando se o número é positivo, negativo, par ou ímpar.
    soma = soma + numero

    if numero > 0:
        positivos = positivos + 1
    elif numero < 0:
        negativos = negativos + 1

    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
media = soma / 10
# Exibindo relatório
print("=====RELATÓRIO ESTATÍSTICO=====")
print(f"Soma:",soma)
print(f"Números positivos:",positivos)
print(f"Números negativos:",negativos)
print(f"Números pares:",pares)
print(f"Números ímpares:",impares)
print(f"Média: {media:.2f}")
-----------------------------------------------------
# Questão 09 — Geração de tabuada de multiplicação
print("=====TABUADA DE MULTIPLICAÇÃO=====")
# Solicitando um número inteiro ao usuáro.
numero = int(input("Digite um número inteiro: "))
# Gerando e exibindo a tabuada de multiplicação.
for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")
------------------------------------------------------------------
# Questão 10 — Análise de temperaturas registradas em uma semana
temperaturas = []
# Leitura das 7 temperaturas
for i in range(1,8):
    temp = float(input(f"Digite a temperatura do {i}º dia (°C): "))
    temperaturas.append(temp)
# Análisando e calculando as temperaturas
maior_temp = max(temperaturas)
menor_temp = min(temperaturas)
media_temp = sum(temperaturas) / len(temperaturas)
# Contagem dos dias ácima da média
dias_acima_da_media = sum(1 for temp in temperaturas if temp > media_temp)
# Exibindo a análise das temperaturas
print("\n=== RESUMO DO PERÍODO ===")
print(f"Todas as temperaturas registradas: {temperaturas}")
print(f"Maior temperatura: {maior_temp:.2f}°C")
print(f"Menor temperatura: {menor_temp:.2f}°C")
print(f"Temperatura média: {media_temp:.2f}°C")
print(f"Quantidade de dias ácima da média: {dias_acima_da_media}")
---------------------------------------------------------------------------------
# Questão 11 — Relatório analítico de lista numérica
numeros = []
# Leitura dos 10 números
for i in range(1,11):
    num = int(input(f"Digite {i}º número inteiro: "))
    numeros.append(num)
# Análisando e filtrando os números pares e ímpares
pares = [num for num in numeros if num % 2 == 0]
ímpares = [num for num in numeros if num % 2 != 0]
# Cálculos estatísticos
soma_total = sum(numeros)
media = soma_total / len(numeros)
maior_valor = max(numeros)
menor_valor = min(numeros)
# Exibindo o relatório analítico
print("\n=== RELATÓRIO ANALÍTICO NUMÉRICO ===")
print(f"Todos os números informados: {numeros}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {ímpares}")
print(f"Soma de todos os valores: {soma_total}")
print(f"Média dos valores: {media:.2f}")
print(f"Maior valor: {maior_valor}")
print(f"Menor valor: {menor_valor}")
------------------------------------------------------------
# Questão 12 — Cadastro e inventário de produtos em estoque
estoque = []
# Leitura dos 5 produtos
print("=== CADRASTO DO ESTOQUE ===")
for i in range(1,6):
    print(f"\nProduto {i}º:")
    nome = input(f"Nome do produto: ").strip()
    preco = float(input("Preço unitário (R$): "))
    quantidade = int(input("Quantidade em estoque: "))

    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    estoque.append(produto)

# Exibindo todos os produtos cadastrados
print("\n" + "="*40)
print("=== INVENTÁRIO DO ESTOQUE ===")
for prod in estoque:
    subtotal = prod["preco"] * prod["quantidade"]
    print(f"Produto: {prod['nome']} | Preço: R$ {prod['preco']:.2f} | "
          f"Qtd: {prod['quantidade']} | Subtotal: R$ {subtotal:.2f}")
# Calculando o valor total do estoque
valor_total_estoque = sum(prod["preco"] * prod["quantidade"] for prod in estoque)

# Identificando o produto com maior preço unitário
produto_mais_caro = max(estoque, key=lambda p: p["preco"])

# Exibição dos resultados finais
print("="*40)
print(f"Valor total investido no estoque: R$ {valor_total_estoque:.2f}")
print(f"Produto mais caro: {produto_mais_caro['nome']} (R$ {produto_mais_caro['preco']:.2f})")
-------------------------------------------------------------------------------------------------
# Questão 13 — Agenda de contatos com funcionalidade de consulta
agenda = []
# Cadastro de 5 contatos
print("=== CADRASTO De CONTATOS ===")
for i in range(1,6):
    print(f"\nContato {i}º:")
    nome = input(f"Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("E-mail: ").strip()

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }
    agenda.append(contato)
# Funcionalidade de consulta
print("\n" + "="*40)
print("=== CONSULTA DE CONTATO ===")
nome_busca = input("Digite o nome da pessoa para buscar: ").strip()
# Busca do contato (ignorando diferenças entre maiúsculas e minúsculas)
contato_encontrado = None
for contato in agenda:
    if contato["nome"].lower() == nome_busca.lower():
        contato_encontrado = contato
        break
# Exibição dos resultados
print("="*40)
if contato_encontrado:
    print("Contato encontrado!")
    print(f"Nome:     {contato_encontrado['nome']}")
    print(f"Telefone: {contato_encontrado['telefone']}")
    print(f"E-mail:   {contato_encontrado['email']}")
else:
    print("Contato não encontrado.")
-----------------------------------------------------------------------------------------
# Questão 14 — Sistema de gerenciamento de notas de turma
def cadastrar_estudante(id_estudante):
    """Lê as informações de um estudante, calcula sua média e retorna um dicionário."""
    print(f"\nEstudante {id_estudante}:")
    nome = input("Nome: ").strip()
    
    notas = []
    for j in range(1, 4):
        nota = float(input(f"Nota {j} (0 a 10): "))
        notas.append(nota)
    
    media = sum(notas) / len(notas)
    
    return {
        "nome": nome,
        "notas": notas,
        "media": media
    }

def obter_estatisticas(turma):
    """Calcula e retorna estatísticas e contagens do desempenho da turma."""
    maior = max(turma, key=lambda e: e["media"])
    menor = min(turma, key=lambda e: e["media"])
    
    aprovados = sum(1 for e in turma if e["media"] >= 7.0)
    recuperacao = sum(1 for e in turma if 5.0 <= e["media"] < 7.0)
    reprovados = sum(1 for e in turma if e["media"] < 5.0)
    
    return maior, menor, aprovados, recuperacao, reprovados

def exibir_relatorio(turma):
    """Exibe o relatório final consolidado com os resultados da turma."""
    maior, menor, aprovados, recuperacao, reprovados = obter_estatisticas(turma)
    
    print("\n" + "="*40)
    print("--- RELATÓRIO DE DESEMPENHO DA TURMA ---")

    print("\n1. Médias individuais:")
    for e in turma:
        print(f"• {e['nome']}: {e['media']:.2f}")

    print("\n2. Destaques:")
    print(f"• Maior média: {maior['nome']} ({maior['media']:.2f})")
    print(f"• Menor média: {menor['nome']} ({menor['media']:.2f})")

    print("\n3. Situação final:")
    print(f"• Aprovados (média ≥ 7): {aprovados}")
    print(f"• Em recuperação (5 ≤ média < 7): {recuperacao}")
    print(f"• Reprovados (média < 5): {reprovados}")
    print("="*40)

def main():
    turma = []
    print("--- CADASTRO DE ESTUDANTES ---")
    for i in range(1, 6):
        estudante = cadastrar_estudante(i)
        turma.append(estudante)
    
    exibir_relatorio(turma)

# Execução do programa
if __name__ == "__main__":
    main()
----------------------------------------------------------------------------------------
# Questão 15 — Cadastro e análise populacional de cidades
def cadastrar_cidade(indice):
    """Lê os dados de uma cidade e retorna um dicionário."""
    print(f"\nCidade {indice}:")
    nome = input("Nome da cidade: ").strip()
    estado = input("Estado (sigla UF, ex: SP): ").strip().upper()
    populacao = int(input("População estimada: "))
    
    return {
        "nome": nome,
        "estado": estado,
        "populacao": populacao
    }

def main():
    cidades = []
    
    print("--- CADASTRO DE CIDADES ---")
    for i in range(1, 6):
        cidades.append(cadastrar_cidade(i))
    
    # Processamento estatístico
    cidade_maior_pop = max(cidades, key=lambda c: c["populacao"])
    cidade_menor_pop = min(cidades, key=lambda c: c["populacao"])
    populacao_total = sum(c["populacao"] for c in cidades)
    media_populacional = populacao_total / len(cidades)
    
    # Exibição do relatório final
    print("\n" + "="*50)
    print("--- RELATÓRIO DE ANÁLISE POPULACIONAL ---")
    
    print("\n1. Dados completos das cidades cadastradas:")
    for c in cidades:
        print(f"• Cidade: {c['nome']} - {c['estado']} | População: {c['populacao']:,} habitantes".replace(",", "."))
    
    print("\n2. Estatísticas populacionais:")
    print(f"• Maior população: {cidade_maior_pop['nome']} - {cidade_maior_pop['estado']} ({cidade_maior_pop['populacao']:,} hab.)".replace(",", "."))
    print(f"• Menor população: {cidade_menor_pop['nome']} - {cidade_menor_pop['estado']} ({cidade_menor_pop['populacao']:,} hab.)".replace(",", "."))
    print(f"• População total: {populacao_total:,} habitantes".replace(",", "."))
    print(f"• Média populacional: {media_populacional:,.2f} habitantes".replace(",", "X").replace(".", ",").replace("X", "."))
    print("="*50)

if __name__ == "__main__":
    main()
--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Questão 16 — Sistema interativo com menu de opções
def main():
    numeros = []
    
    while True:
        print("\n================================")
        print("    GERENCIAMENTO DE NÚMEROS    ")
        print("================================")
        print("1 - Cadastrar número")
        print("2 - Listar números")
        print("3 - Exibir maior número")
        print("4 - Exibir menor número")
        print("5 - Calcular média")
        print("0 - Encerrar programa")
        print("================================")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            try:
                num = float(input("Digite um número: "))
                numeros.append(num)
                print("Número cadastrado com sucesso!")
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
                
        elif opcao == "2":
            if numeros:
                print("\nLista de números cadastrados:")
                for i, n in enumerate(numeros, 1):
                    print(f"  {i}. {n}")
            else:
                print("\nNenhum número cadastrado.")
                
        elif opcao == "3":
            if numeros:
                print(f"\nMaior número cadastrado: {max(numeros)}")
            else:
                print("\nNenhum número cadastrado.")
                
        elif opcao == "4":
            if numeros:
                print(f"\nMenor número cadastrado: {min(numeros)}")
            else:
                print("\nNenhum número cadastrado.")
                
        elif opcao == "5":
            if numeros:
                media = sum(numeros) / len(numeros)
                print(f"\nMédia dos números: {media:.2f}")
            else:
                print("\nNenhum número cadastrado.")
                
        elif opcao == "0":
            print("\nPrograma encerrado.")
            break
            
        else:
            print("\nOpção inválida! Escolha uma opção presente no menu.")

if __name__ == "__main__":
    main()
--------------------------------------------------------------------------------------
# Questão 17 — Cálculos matemáticos com o módulo math
import math
def main():
    try:
        num = float(input("Digite um número real: "))
        # 1. Raiz Quadrada (apenas para números não negativos)
        if num >= 0:
            raiz = math.sqrt(num)
            print(f"Raiz quadrada: {raiz:.2f}")
        else:
            print("Raiz quadrada: não existe raiz quadrada real de número negativo.")

        # 2. Valor Absoluto (Módulo)
        absoluto = math.fabs(num)
        print(f"• Valor absoluto (módulo): {absoluto}")
        
        # 3. Arredondamento para cima (Teto)
        teto = math.ceil(num)
        print(f"• Arredondamento para cima (teto): {teto}")
        
        # 4. Arredondamento para baixo (Piso)
        piso = math.floor(num)
        print(f"• Arredondamento para baixo (piso): {piso}")
        
        # 5. Fatorial (somente se for inteiro e não negativo)
        if num.is_integer() and num >= 0:
            fatorial = math.factorial(int(num))
            print(f"• Fatorial: {fatorial}")
        else:
            print("• Fatorial: Não aplicável (o número precisa ser um inteiro não negativo).")
            
    except ValueError:
        print("Entrada inválida. Digite um número válido.")

if __name__ == "__main__":
    main()
----------------------------------------------------------------------------------------------------------
# Questão 18 — Simulação de lançamento de dados com análise estatística
import random

def lancar_dado():
    """Retorna um valor aleatório entre 1 e 6."""
    return random.randint(1, 6)

def main():
    print("=== PARTE 1 — LANÇAMENTO ÚNICO ===")
    dado1 = lancar_dado()
    dado2 = lancar_dado()
    soma_unica = dado1 + dado2
    
    print(f"• Dado 1: {dado1}")
    print(f"• Dado 2: {dado2}")
    print(f"• Soma dos valores: {soma_unica}")
    
    print("\n" + "="*40 + "\n")
    
    print("=== PARTE 2 — MÚLTIPLOS LANÇAMENTOS (10 VEZES) ===")
    somas_iguais_a_sete = 0
    
    for i in range(1, 11):
        d1 = lancar_dado()
        d2 = lancar_dado()
        soma = d1 + d2
        
        # Incrementa o contador se a soma for igual a 7
        if soma == 7:
            somas_iguais_a_sete += 1
            
        print(f"Lançamento {i:2d}: Dado 1 = {d1} | Dado 2 = {d2} | Soma = {soma}")
    
    print("\n" + "-"*40)
    print(f"Quantidade de vezes em que a soma foi igual a 7: {somas_iguais_a_sete}")

if __name__ == "__main__":
    main()
---------------------------------------------------------------------------------------------------------
# Questão 19 — Análise linguística completa de uma frase
def main():
    frase_original = input("Digite uma frase: ")
    
    # Tratamento dos espaços nas extremidades e entre palavras
    frase_limpa = " ".join(frase_original.split())
    
    if not frase_limpa:
        print("Nenhuma frase válida foi digitada.")
        return
        
    letra_busca = input("Digite uma letra para contar as ocorrências: ").strip()
    
    # 1. Métodos de string e manipulações
    total_caracteres = len(frase_original)
    palavras = frase_limpa.split()
    total_palavras = len(palavras)
    primeira_palavra = palavras[0]
    ultima_palavra = palavras[-1]
    
    # Contagem de ocorrências (considera maiúsculas e minúsculas)
    if letra_busca:
        qtd_letra = frase_original.lower().count(letra_busca[0].lower())
    else:
        qtd_letra = 0
        
    frase_maiuscula = frase_original.upper()
    frase_minuscula = frase_original.lower()
    
    # Exibição dos resultados
    print("\n" + "="*45)
    print("--- ANÁLISE LINGUÍSTICA DA FRASE ---")
    print("="*45)
    print(f"• Total de caracteres (com espaços): {total_caracteres}")
    print(f"• Quantidade de palavras: {total_palavras}")
    print(f"• Primeira palavra: {primeira_palavra}")
    print(f"• Última palavra: {ultima_palavra}")
    if letra_busca:
        print(f"• Ocorrências da letra '{letra_busca[0]}': {qtd_letra}")
    print(f"• Em maiúsculas: {frase_maiuscula}")
    print(f"• Em minúsculas: {frase_minuscula}")
    print("="*45)

if __name__ == "__main__":
    main()
------------------------------------------------------------------------------------
# Questão 20 — Sistema completo de gerenciamento acadêmico
import sys

# Estrutura principal de dados: lista de dicionários
turma = []

def calcular_situacao(media):
    """Retorna a situação acadêmica baseada na média."""
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperação"
    else:
        return "Reprovado"

def cadastrar_estudante():
    """Lê as informações de um novo estudante e adiciona à turma."""
    print("\n--- CADASTRO DE ESTUDANTE ---")
    
    nome = input("Nome completo: ").strip()
    if not nome:
        print("Erro: O nome não pode ser vazio.")
        return

    try:
        idade = int(input("Idade: "))
        if idade <= 0:
            print("Erro: A idade deve ser um inteiro positivo.")
            return
    except ValueError:
        print("Erro: Entrada inválida para a idade.")
        return

    curso = input("Curso: ").strip()

    # Coleta e validação das três notas
    notas = []
    for i in range(1, 4):
        try:
            nota = float(input(f"Nota {i} (0 a 10): "))
            if 0.0 <= nota <= 10.0:
                notas.append(nota)
            else:
                print("Erro: A nota deve estar entre 0 e 10.")
                return
        except ValueError:
            print("Erro: Entrada inválida para a nota.")
            return

    # Cálculos automáticos
    media = sum(notas) / len(notas)
    situacao = calcular_situacao(media)

    # Armazenamento em Dicionário (Notas guardadas em Tupla para imutabilidade)
    estudante = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "notas": tuple(notas),
        "media": media,
        "situacao": situacao
    }

    turma.append(estudante)
    print(f"\nEstudante '{nome}' cadastrado(a) com sucesso!")

def listar_estudantes():
    """Exibe todos os estudantes cadastrados com seus dados."""
    print("\n--- LISTA DE ESTUDANTES ---")
    if not turma:
        print("Nenhum estudante cadastrado.")
        return

    for idx, e in enumerate(turma, 1):
        print(f"\n[{idx}] {e['nome']} - Curso: {e['curso']} | Idade: {e['idade']}")
        print(f"    Notas: {e['notas'][0]:.1f}, {e['notas'][1]:.1f}, {e['notas'][2]:.1f}")
        print(f"    Média: {e['media']:.2f} | Situação: {e['situacao']}")

def buscar_estudante_por_nome(nome_busca):
    """Busca um estudante na lista ignorando maiúsculas e minúsculas."""
    for e in turma:
        if e["nome"].lower() == nome_busca.lower():
            return e
    return None

def consultar_estudante():
    """Consulta e exibe os dados de um estudante específico."""
    print("\n--- CONSULTA DE ESTUDANTE ---")
    if not turma:
        print("Nenhum estudante cadastrado.")
        return

    nome_busca = input("Digite o nome do estudante para consulta: ").strip()
    estudante = buscar_estudante_por_nome(nome_busca)

    if estudante:
        print("\nDados do estudante:")
        print(f"• Nome: {estudante['nome']}")
        print(f"• Idade: {estudante['idade']}")
        print(f"• Curso: {estudante['curso']}")
        print(f"• Notas: {estudante['notas']}")
        print(f"• Média Final: {estudante['media']:.2f}")
        print(f"• Situação Acadêmica: {estudante['situacao']}")
    else:
        print("Estudante não encontrado.")

def alterar_dados():
    """Permite a edição dos campos de um estudante existente."""
    print("\n--- ALTERAR DADOS DO ESTUDANTE ---")
    if not turma:
        print("Nenhum estudante cadastrado.")
        return

    nome_busca = input("Digite o nome do estudante a ser alterado: ").strip()
    estudante = buscar_estudante_por_nome(nome_busca)

    if not estudante:
        print("Estudante não encontrado.")
        return

    print(f"\nAlterando dados de: {estudante['nome']} (pressione Enter para manter o valor atual)")

    # Alteração do nome
    novo_nome = input(f"Novo nome [{estudante['nome']}]: ").strip()
    if novo_nome:
        estudante["nome"] = novo_nome

    # Alteração da idade
    nova_idade_str = input(f"Nova idade [{estudante['idade']}]: ").strip()
    if nova_idade_str:
        try:
            nova_idade = int(nova_idade_str)
            if nova_idade > 0:
                estudante["idade"] = nova_idade
        except ValueError:
            print("Idade inválida! Mantida a anterior.")

    # Alteração do curso
    novo_curso = input(f"Novo curso [{estudante['curso']}]: ").strip()
    if novo_curso:
        estudante["curso"] = novo_curso

    # Alteração das notas
    alterar_notas = input("Deseja alterar as notas? (S/N): ").strip().lower()
    if alterar_notas == 's':
        novas_notas = []
        for i in range(1, 4):
            try:
                n = float(input(f"Nova Nota {i} [{estudante['notas'][i-1]}]: "))
                if 0.0 <= n <= 10.0:
                    novas_notas.append(n)
                else:
                    print("Nota inválida! Mantendo as notas anteriores.")
                    return
            except ValueError:
                print("Entrada inválida! Mantendo as notas anteriores.")
                return

        estudante["notas"] = tuple(novas_notas)
        estudante["media"] = sum(novas_notas) / len(novas_notas)
        estudante["situacao"] = calcular_situacao(estudante["media"])

    print("\nDados atualizados com sucesso!")

def remover_estudante():
    """Exclui um estudante do sistema com confirmação."""
    print("\n--- REMOVER ESTUDANTE ---")
    if not turma:
        print("Nenhum estudante cadastrado.")
        return

    nome_busca = input("Digite o nome do estudante a ser removido: ").strip()
    estudante = buscar_estudante_por_nome(nome_busca)

    if estudante:
        confirmacao = input(f"Tem certeza que deseja remover '{estudante['nome']}'? (S/N): ").strip().lower()
        if confirmacao == 's':
            turma.remove(estudante)
            print("Estudante removido com sucesso!")
        else:
            print("Operação cancelada.")
    else:
        print("Estudante não encontrado.")

def gerar_relatorio():
    """Gera o relatório estatístico consolidado da turma."""
    print("\n--- RELATÓRIO DA TURMA ---")
    total = len(turma)
    if total == 0:
        print("Nenhum estudante cadastrado para gerar relatório.")
        return

    # Maior e menor média
    maior_estudante = max(turma, key=lambda e: e["media"])
    menor_estudante = min(turma, key=lambda e: e["media"])

    # Média geral
    media_geral = sum(e["media"] for e in turma) / total

    # Contagem de situações
    aprovados = sum(1 for e in turma if e["situacao"] == "Aprovado")
    recuperacao = sum(1 for e in turma if e["situacao"] == "Recuperação")
    reprovados = sum(1 for e in turma if e["situacao"] == "Reprovado")

    # Exibição das estatísticas
    print(f"• Total de estudantes: {total}")
    print(f"• Maior média: {maior_estudante['nome']} ({maior_estudante['media']:.2f})")
    print(f"• Menor média: {menor_estudante['nome']} ({menor_estudante['media']:.2f})")
    print(f"• Média geral da turma: {media_geral:.2f}")
    print(f"• Aprovados: {aprovados} ({(aprovados/total)*100:.1f}%)")
    print(f"• Em Recuperação: {recuperacao} ({(recuperacao/total)*100:.1f}%)")
    print(f"• Reprovados: {reprovados} ({(reprovados/total)*100:.1f}%)")

def main():
    """Loop do menu principal do sistema."""
    while True:
        print("\n========================================")
        print("           SISTEMA ACADÊMICO            ")
        print("========================================")
        print("1 - Cadastrar estudante")
        print("2 - Listar estudantes")
        print("3 - Consultar estudante")
        print("4 - Alterar dados")
        print("5 - Remover estudante")
        print("6 - Gerar relatório da turma")
        print("0 - Encerrar sistema")
        print("========================================")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_estudante()
        elif opcao == "2":
            listar_estudantes()
        elif opcao == "3":
            consultar_estudante()
        elif opcao == "4":
            alterar_dados()
        elif opcao == "5":
            remover_estudante()
        elif opcao == "6":
            gerar_relatorio()
        elif opcao == "0":
            print("\nEncerrando o sistema acadêmico... Até logo!")
            sys.exit()
        else:
            print("\nOpção inválida! Escolha um número de 0 a 6.")

if __name__ == "__main__":
    main()
-----------------------------------------------------------------------------------
