# 🚉 Sistema de Operações de Monitoramento de Trens

Este projeto é um sistema de monitoramento contínuo para trens e infraestrutura, desenvolvido em Python. Ele permite iniciar o monitoramento, exibir status em tempo real, gerar relatórios de anomalias detectadas, registrar anomalias, criar novo arquivo json e atualizar arquivo existente.

## 📝 Funcionalidades

- **`iniciar_monitoramento`**: inicia o monitoramento contínuo e exibe os trens e infraestruturas monitoradas.
  
- **`exibir_status`**: mostra o status em tempo real dos trens operacionais e em manutenção.
  
- **`relatorio_anomalias`**: exibe um relatório de anomalias detectadas.

- **`registrar_anomalia`**: permite ao usuário registrar uma nova anomalia com detalhes sobre o trem, descrição e data.
  
- **`criar_novo_arquivo_json`**: cria um novo arquivo JSON para armazenar dados de anomalias.

- **`atualizar_arquivo_existente`**: atualiza um arquivo JSON existente com novos dados de anomalias.

- **`encerrar_sistema`**: finaliza o sistema e salva os dados coletados até o momento.

## 🛠️ Como Usar

1. Clone o repositório e execute o código em um terminal Python.
2. Ao iniciar o sistema, você verá o menu principal com as opções:
   
    ```plaintext
   ┌────────────────────────────────────────┐
   │           SISTEMA DE OPERAÇÕES         │
   ├────────────────────────────────────────┤
   │              MENU PRINCIPAL            │
   ├────────────────────────────────────────┤
   │ [1] Iniciar Monitoramento Contínuo     │
   │ [2] Exibir Status em Tempo Real        │
   │ [3] Relatório de Anomalias             │
   │ [4] Registrar Nova Anomalia            │
   │ [5] Criar Novo Arquivo JSON            │
   │ [6] Atualizar Arquivo Existente        │
   │ [7] Encerrar Sistema                   │
   └────────────────────────────────────────┘
3. Selecione uma das opções digitando o número correspondente e pressionando Enter.
