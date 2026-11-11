# Cidadão Seguro - Monitor de ocorrências da rua

import os
from datetime import date

# listas
ruas = []
tipos = []
dias = []

# tipos de ocorrência
TIPOS_VALIDOS = ["Poste apagado", "Bueiro entupido", "Alagamento", "Árvore caída"]


# limpar o terminal
def limpar_tela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# pausa antes de voltar ao menu
def pausar():
    input("\nPressione Enter para voltar ao menu...")


# validação de número inteiro
def ler_inteiro_positivo(mensagem):
    valor = input(mensagem).strip()
    while not valor.isdigit():
        print("Valor inválido! Digite apenas números inteiros, sem sinal.")
        valor = input(mensagem).strip()
    return int(valor)


# classificação do risco
def classificar(tipo, dias_em_aberto):
    if tipo == "Alagamento" and dias_em_aberto >= 2:
        return "Crítico"
    elif dias_em_aberto > 7:
        return "Crítico"
    elif dias_em_aberto >= 4:
        return "Atenção"
    else:
        return "Normal"


# cálculo da média
def calcular_media(lista_dias):
    soma = 0
    for d in lista_dias:
        soma += d
    return soma / len(lista_dias)


# cadastro de ocorrência
def cadastrar():
    print("--- NOVA OCORRÊNCIA ---")

    # entrada de dados
    rua = input("Rua ou ponto de referência: ").strip()
    while rua == "":
        print("A rua não pode ficar em branco.")
        rua = input("Rua ou ponto de referência: ").strip()

    qtd_tipos = len(TIPOS_VALIDOS)
    print("Tipo de ocorrência:")
    for i in range(qtd_tipos):
        print(f"  {i + 1} - {TIPOS_VALIDOS[i]}")
    opcao_tipo = ler_inteiro_positivo(f"Escolha o tipo (1 a {qtd_tipos}): ")
    while opcao_tipo < 1 or opcao_tipo > qtd_tipos:
        print(f"Opção inválida! Escolha um número de 1 a {qtd_tipos}.")
        opcao_tipo = ler_inteiro_positivo(f"Escolha o tipo (1 a {qtd_tipos}): ")
    tipo = TIPOS_VALIDOS[opcao_tipo - 1]

    dias_em_aberto = ler_inteiro_positivo("Há quantos dias o problema está em aberto? ")

    # armazenamento nas listas
    ruas.append(rua)
    tipos.append(tipo)
    dias.append(dias_em_aberto)

    # saída de dados
    print(f"Ocorrência registrada! Status: {classificar(tipo, dias_em_aberto)}")


# relatório
def mostrar_relatorio():
    total = len(ruas)
    if total == 0:
        print("Nenhuma ocorrência cadastrada ainda. Use a opção 1 primeiro.")
        return

    hoje = date.today()
    print(f"========== RELATÓRIO - VILA AURORA - {hoje.day}/{hoje.month}/{hoje.year} ==========")

    # tabela de ocorrências
    print(f"{'Nº':<4}{'Rua':<25}{'Tipo':<18}{'Dias':<6}Status")
    for i in range(total):
        status = classificar(tipos[i], dias[i])
        print(f"{i + 1:<4}{ruas[i]:<25}{tipos[i]:<18}{dias[i]:<6}{status}")

    # contagem por status
    qtd_normal = 0
    qtd_atencao = 0
    qtd_critico = 0
    for i in range(total):
        status = classificar(tipos[i], dias[i])
        if status == "Crítico":
            qtd_critico += 1
        elif status == "Atenção":
            qtd_atencao += 1
        else:
            qtd_normal += 1

    # ocorrência mais antiga
    posicao_maior = 0
    for i in range(total):
        if dias[i] > dias[posicao_maior]:
            posicao_maior = i

    # indicadores
    print("\n--- INDICADORES ---")
    print(f"Total de ocorrências: {total}")
    print(f"Média de dias em aberto: {calcular_media(dias):.1f} dias")
    print(f"Ocorrência mais antiga: {tipos[posicao_maior]} na {ruas[posicao_maior]} "
          f"({dias[posicao_maior]} dias)")
    percentual_critico = qtd_critico / total * 100
    print(f"Normal: {qtd_normal} | Atenção: {qtd_atencao} | Crítico: {qtd_critico}")
    print(f"Percentual de ocorrências críticas: {percentual_critico:.1f}%")

    # contagem por tipo
    print("Quantidade por tipo:")
    for tipo in TIPOS_VALIDOS:
        contador = 0
        for t in tipos:
            if t == tipo:
                contador += 1
        print(f"  {tipo}: {contador}")

    # recomendação
    print("\n--- RECOMENDAÇÃO ---")
    if percentual_critico >= 50:
        print("SITUAÇÃO GRAVE: metade ou mais das ocorrências são críticas.")
        print("Recomenda-se um mutirão de manutenção no bairro e alerta aos moradores.")
    elif qtd_critico > 0:
        posicao_prioridade = -1
        for i in range(total):
            if classificar(tipos[i], dias[i]) == "Crítico":
                if posicao_prioridade == -1 or dias[i] > dias[posicao_prioridade]:
                    posicao_prioridade = i
        print(f"Há {qtd_critico} ocorrência(s) crítica(s).")
        print(f"Priorize: {tipos[posicao_prioridade]} na {ruas[posicao_prioridade]}, "
              f"aberta há {dias[posicao_prioridade]} dias.")
    elif qtd_atencao > 0:
        print("Nenhuma ocorrência crítica, mas há itens em Atenção.")
        print("Acompanhe para que não passem de 7 dias em aberto.")
    else:
        print("Bairro sob controle: todas as ocorrências estão dentro do prazo.")
    print("=" * 70)


# menu principal
opcao = ""
while opcao != "3":
    limpar_tela()
    print("=" * 50)
    print("   CIDADÃO SEGURO - Monitor de ocorrências da rua")
    print("=" * 50)
    print("1 - Cadastrar ocorrência")
    print("2 - Ver relatório")
    print("3 - Encerrar")
    opcao = input("Escolha uma opção: ").strip()

    limpar_tela()
    if opcao == "1":
        cadastrar()
        pausar()
    elif opcao == "2":
        mostrar_relatorio()
        pausar()
    elif opcao == "3":
        print("Programa encerrado. Obrigado por usar o Cidadão Seguro!")
    else:
        print("Opção inválida! Digite 1, 2 ou 3.")
        pausar()