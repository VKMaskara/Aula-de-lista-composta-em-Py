

import random
import sys # função de finalizar o código e sair do loop
import os
import time
from datetime import datetime



# Tela de Login e Cadastro

# --- VARIÁVEIS DE CONFIGURAÇÃO (Credenciais) ---
usuario_correto = "kaique"
senha_correta = "1245"
tentativas_maximas = 3


def fazer_cadastro():
    global usuario_correto, senha_correta
    print("\n--- TELA DE CADASTRO ---")
    novo_usuario = input('Insira o nome de usuario que deseja registrar ').strip()
    nova_senha = input('Insira a senha').strip()

    usuario_correto = novo_usuario
    senha_correta = nova_senha

    print("Cadastro realizado com sucesso! Você será levado ao menu principal.")
    return True
def fazer_login():

    tentativas = tentativas_maximas

    while tentativas > 0:
        
        # 1. Solicita as credenciais
        usuario = input(f"Usuário ({usuario_correto}): ").strip() 
        senha = input(f"Senha ({senha_correta}): ").strip()
        
        # 2. Verifica as credenciais
        if usuario == usuario_correto and senha == senha_correta:
            print("\n====================================")
            print("Login bem-sucedido! Acesso liberado.")
            print("====================================\n")
            return True  # Login OK
        else:
            tentativas -= 1
            if tentativas > 0:
                print(f"\nErro: Usuário ou senha incorretos.")
                print(f"Você tem mais {tentativas} tentativa(s).\n")
            else:
                print("\n====================================")
                print("Número máximo de tentativas excedido.")
                print("====================================")
                return False # Login Falhou

def tela_inicial_com_menu():
    
    # Loop 'while True' para repetir o menu até que um 'return' seja executado
    while True:
        print("\n====================================")
        print("      SIMULADOR DE DADOS - MENU     ")
        print("====================================")
        
        # O menu de opções que você criou:
        print('Escolha uma das opções abaixo:')
        print('  (L) - Login')
        print('  (C) - Cadastro')
        print('  (E) - Encerrar Programa')

        # Armazena a escolha do usuário
        escolha = input('Digite sua opção: ').strip().upper()
        
        # --- Estrutura IF/ELIF/ELSE ---
        
        if escolha == 'L':
            # Se escolher 'L', chama a função de login.
            # Se o login_sucesso for True, a função 'tela_inicial_com_menu' termina e retorna True.
            if fazer_login():
                return True 
            # Se o login falhar (retornar False), o loop 'while True' repete e o menu reaparece.
            
        elif escolha == 'C':
            # Se escolher 'C', chama a função de cadastro.
            fazer_cadastro()
            # Volta para o início do loop e exibe o menu novamente.
            
        elif escolha == 'E':
            # Se escolher 'E', encerra o programa
            print("\nEncerrando o programa a pee" \
            "dido do usuário.")
            sys.exit()
            return False
            
        else:
            # Se digitar qualquer outra coisa
            print(f"Opção inválida ('{escolha}'). Por favor, digite L, C ou E.")
# ----------------------------------------------------------------------
# ESTRUTURA PRINCIPAL (Isto faz o código rodar)
# ----------------------------------------------------------------------

if tela_inicial_com_menu():
    # O restante do programa de simulação de dados começaria aqui
    print("Acesso concedido. Preparando para a simulação de dados...")
else:
    print("Acesso negado. Fechando o programa.")



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

