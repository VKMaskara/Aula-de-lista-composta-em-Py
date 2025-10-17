# TELA DO PROGRAMA
# JOGO DO DADO

import random
import os
import time
from datetime import datetime

# tela do programa

# Função para limpar a tela do terminal
def limpar_tela():
    """
    Limpa a tela do terminal.
    windows: cls
    linux/mac: clear
    """
    print("\n" * 100)
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela do terminal de acordo com o sistema operacional

def tela_inicial():
    print("=-"*50)
    print("*     JOGO DO DADO - V1.0       *".center(100))
    print("=-"*50)
    time.sleep(2)


while True:
    limpar_tela()
    tela_inicial()
    jogadas = []  # lista para armazenar os resultados dos lançamentos
    contador = [0,0,0,0,0,0] #contador para cada face do dado
    
    print("Lançando o dado 50 vezes...\n")
    for c in range(1,51):
        dado = random.randint(1,6)
        jogadas.append(dado)
        contador[dado-1] += 1
        print(f"Lançamento {c}: {dado}", end='\r')
        time.sleep(0.1)  
    time.sleep(1)


    total_jogadas = sum(contador)
    for i in range(6):
        porcentagem = (contador[i] / total_jogadas) * 100
        print(f"A face {i+1} apareceu {contador[i]} vezes ({porcentagem:.1f}%)")

    print("\nResultados dos lançamentos:")
    print("+" + "-"*68 + "+")  # Top border of the table
    for i in range(0, len(jogadas), 10):  # Percorre a lista de jogadas de 10 em 10
        linha = " |  ".join(f"{n:3}" for n in jogadas[i:i+10])  # Formata uma linha com até 10 jogadas
        print("| " + linha.center(66) + " |")  # Imprime a linha formatada
        print("+" + "-"*68 + "+")  # Bottom border of each row

    while True:
        resposta = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
        if resposta == "n":
            break
        elif resposta == "s":
            break
        else:
            print("Resposta inválida. Digite 's' para sim ou 'n' para não.")

    if resposta == "n":
        break
        

limpar_tela()

# tela de encerramento 

# animação rápida de encerramento
for i in range(4):  # Loop para criar uma animação de encerramento
    print(f"Encerrando{'.' * i}".ljust(40), end='\r')  # Imprime "Encerrando" com pontos que aumentam a cada iteração
    time.sleep(0.25)  # Pausa de 0.25 segundos entre as iterações
limpar_tela()  # Limpa a tela após a animação

width = 72  # Define a largura da tela para formatação
print("=" * width)  # Imprime uma linha de "=" na largura definida
print("FIM DO JOGO DO DADO".center(width))  # Imprime o título centralizado
print("=" * width)  # Imprime outra linha de "="
print(f"Data/Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}".center(width))  # Imprime a data e hora atual centralizada
print("-" * width)  # Imprime uma linha de "-" para separação

# resumo das estatísticas (se disponíveis)
try:
    total = sum(contador)  # Calcula o total de lançamentos
    print(f"Total de lançamentos: {total}".center(width))  # Imprime o total centralizado
    print()  # Linha em branco
    for i in range(6):  # Loop para imprimir estatísticas de cada face do dado
        pct = (contador[i] / total * 100) if total else 0.0  # Calcula a porcentagem de cada face
        line = f"Face {i+1}: {contador[i]:3} vezes — {pct:5.1f}%"  # Formata a linha com a face, contagem e porcentagem
        print(line.center(width))  # Imprime a linha centralizada
except NameError:  # Captura erro se 'contador' não estiver definido
    print("Resumo de jogadas indisponível.".center(width))  # Mensagem de erro centralizada

print("-" * width)  # Imprime uma linha de "-" para separação

# créditos formatados
print("Créditos".center(width))  # Imprime o título "Créditos" centralizado
credits = [  # Lista de créditos com nomes e funções
    ("Kaique Sousa", "Tela de Login"),
    ("Vitor Kauê", "Lógica / Programa"),
    ("Dennys Cavessana", "Encerramento")
]
max_name = max(len(n) for n, _ in credits)  # Encontra o comprimento máximo dos nomes
for name, role in credits:  # Loop para imprimir cada crédito
    print(f"{name.ljust(max_name)}  ·  {role}".center(width))  # Imprime o nome e função centralizados

print("\n" + "Obrigado por jogar! Até a próxima.".center(width) + "\n")  # Mensagem de agradecimento centralizada
time.sleep(2)  # Pausa de 2 segundos antes de encerrar

