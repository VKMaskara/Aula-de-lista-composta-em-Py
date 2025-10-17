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
            print("\nEncerrando o programa a pedido do usuário.")
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