import json
import os


# Funções auxiliares para lidar com JSON
def carregar_dados_json(arquivo):
    """
    Carrega os dados de um arquivo JSON.
    Se o arquivo não existir, retorna uma lista vazia.
    """
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            return json.load(f)
    return []


def salvar_dados_json(arquivo, dados):
    """
    Salva os dados em um arquivo JSON, sobrescrevendo o conteúdo atual.
    """
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)


# Dados simulados
trens_operacionais = ["Trem 1", "Trem 2", "Trem 3"]
trens_manutencao = ["Trem 4"]
anomalias = carregar_dados_json('anomalias.json')


def menu():
    """
    Exibe o menu principal do sistema para o usuário escolher a opção desejada.
    """
    print("┌────────────────────────────────────────┐")
    print("│           SISTEMA DE OPERAÇÕES         │")
    print("├────────────────────────────────────────┤")
    print("│              MENU PRINCIPAL            │")
    print("├────────────────────────────────────────┤")
    print("│ [1] Iniciar Monitoramento Contínuo     │")
    print("│ [2] Exibir Status em Tempo Real        │")
    print("│ [3] Relatório de Anomalias             │")
    print("│ [4] Registrar Nova Anomalia            │")
    print("│ [5] Criar Novo Arquivo JSON            │")
    print("│ [6] Atualizar Arquivo Existente        │")
    print("│ [7] Encerrar Sistema                   │")
    print("└────────────────────────────────────────┘")


def obter_opcao_usuario():
    """
    Solicita ao usuário a escolha de uma opção no menu e retorna a opção selecionada.
    Caso a entrada seja inválida, solicita novamente.
    """
    while True:
        try:
            escolha = int(input('Selecione uma opção: '))
            if escolha in range(1, 8):  
                return escolha
            else:
                print('Opção inválida. Escolha entre 1 e 7.')
        except ValueError:
            print('Entrada inválida. Insira um número.')


def iniciar_monitoramento(trens, infraestrutura):
    """
    Inicia o monitoramento contínuo dos trens e infraestruturas, imprimindo informações relevantes.
    """
    print("\nIniciando monitoramento contínuo de trens e infraestruturas...")
    print(f"• Trens monitorados: {', '.join(trens)}")
    print(f"• Infraestruturas críticas: {infraestrutura} monitoradas")
    print("Monitoramento contínuo ativo! Todos os dados estão sendo registrados em tempo real.\n")
    return True


def exibir_status(trens_operacionais, trens_manutencao):
    """
    Exibe o status em tempo real dos sistemas, incluindo trens operacionais e em manutenção.
    """
    print("\nStatus em Tempo Real de Todos os Sistemas:")
    print(f"• Trens operacionais: {len(trens_operacionais)}")
    print(f"• Trens em manutenção: {len(trens_manutencao)}")
    print("• Infraestruturas críticas: 5 monitoradas")
    print("• Última verificação de trilhos: 5 minutos atrás")
    print("Todos os sistemas estão funcionando dentro dos parâmetros normais.\n")

def relatorio_anomalias(anomalias):
    """
    Exibe um relatório com as anomalias registradas no sistema.
    """
    print("\nRelatório de Anomalias Detectadas:")
    if anomalias:
        for anomalia in anomalias:
            print(f"• Trem: {anomalia['trem']}, Data: {anomalia['data']}, Descrição: {anomalia['descricao']}")
        print(f"• Total de anomalias no último mês: {len(anomalias)}")
    else:
        print("Nenhuma anomalia registrada.")
    print("Relatório completo disponível para download e análise detalhada.\n")


def encerrar_sistema():
    """
    Encerra o sistema, pausando todas as operações de monitoramento e salvando os dados coletados.
    """
    print("\nEncerrando sistema. Todas as operações de monitoramento serão pausadas.")
    print("Os dados coletados até agora foram salvos para futuras análises.")
    print("Sistema encerrado com sucesso. Até logo!")
    return False


def registrar_anomalia(trem, descricao, data):
    """
    Registra uma nova anomalia e salva no arquivo JSON.
    """
    # Cria um novo dicionário de anomalia
    anomalia = {"trem": trem, "descricao": descricao, "data": data}

    # Adiciona a anomalia à lista existente
    anomalias.append(anomalia)

    # Salva os dados atualizados no arquivo JSON
    salvar_dados_json('anomalias.json', anomalias)

    # Confirma que a anomalia foi registrada
    print(f"\nAnomalia registrada: {anomalia['trem']} - {anomalia['descricao']}")


def criar_novo_arquivo_json(nome_arquivo):
    """
    Cria um novo arquivo JSON, se o arquivo ainda não existir.
    """
    try:
        if os.path.exists(nome_arquivo):
            print(f"O arquivo '{nome_arquivo}' já existe. Não será criado novamente.")
        else:
            with open(nome_arquivo, 'w') as f:
                json.dump([], f, indent=4)  # Cria um arquivo vazio
            print(f"Novo arquivo '{nome_arquivo}' criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar o arquivo: {e}")


def atualizar_arquivo_existente(nome_arquivo):
    """
    Atualiza um arquivo JSON existente, adicionando uma nova anomalia.
    """
    try:
        if not os.path.exists(nome_arquivo):
            print(f"O arquivo '{nome_arquivo}' não existe. Não é possível atualizar.")
            return

        dados_atualizados = carregar_dados_json(nome_arquivo)
        print(f"Arquivo '{nome_arquivo}' carregado com sucesso!")

        # Capturando os dados da anomalia com input.
        trem = input("\nDigite o nome do trem com a anomalia: ")
        descricao = input("Descrição da anomalia: ")
        data = input("Data da anomalia (DD/MM/AAAA): ")
        anomalia = {"trem": trem, "descricao": descricao, "data": data}

        dados_atualizados.append(anomalia)

        # Salva os dados atualizados no arquivo
        salvar_dados_json(nome_arquivo, dados_atualizados)
        print(f"Arquivo '{nome_arquivo}' atualizado com a nova anomalia!")
    except Exception as e:
        print(f"Erro ao atualizar o arquivo: {e}")


# Menu Principal
executando = True
while executando:
    menu()
    escolha = obter_opcao_usuario()

    if escolha == 1:
        # Iniciar Monitoramento
        iniciar_monitoramento(trens_operacionais, infraestrutura=5)
    elif escolha == 2:
        # Exibir Status em Tempo Real
        exibir_status(trens_operacionais, trens_manutencao)
    elif escolha == 3:
        # Relatório de Anomalias
        relatorio_anomalias(anomalias)
    elif escolha == 4:
        # Registrar Nova Anomalia
        try:
            trem = input("\nDigite o nome do trem com a anomalia: ")
            descricao = input("Descrição da anomalia: ")
            data = input("Data da anomalia (DD/MM/AAAA): ")
            registrar_anomalia(trem, descricao, data)
        except Exception as e:
            print(f"Erro ao registrar anomalia: {e}")
    elif escolha == 5:
        # Criar Novo Arquivo JSON
        nome_arquivo = input("Digite o nome do novo arquivo JSON (ex: novo_arquivo.json): ")
        criar_novo_arquivo_json(nome_arquivo)
    elif escolha == 6:
        # Atualizar Arquivo Existente
        nome_arquivo = input("Digite o nome do arquivo JSON para atualizar (ex: anomalias.json): ")
        atualizar_arquivo_existente(nome_arquivo)
    elif escolha == 7:
        # Encerrar Sistema
        executando = encerrar_sistema()
