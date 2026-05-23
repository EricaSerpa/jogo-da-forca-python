# Jogo da Forca em Python 🎮

Este projeto consiste em um jogo da forca interativo executado via terminal, desenvolvido como solução técnica para a disciplina de Programação de Computadores. O objetivo principal foi consolidar os conceitos teóricos do percurso formativo em uma aplicação real e funcional.

---

## 🚀 O que aprendi e apliquei neste projeto

### 1. Lógica Algorítmica e Controle de Fluxo
*   **Motor do Jogo:** Utilização do laço de repetição `while` estruturado com múltiplas condições de parada (fim das tentativas ou descoberta total da palavra).
*   **Validação de Entradas:** Implementação de filtros com condicionais (`if/else`, `.isalpha()` e `len()`) para blindar o sistema contra caracteres inválidos, espaços em branco ou digitações duplas.

### 2. Modelagem de Dados Estratégica
*   **Listas (`list`):** Uso de uma lista mutável e ordenada para representar a palavra mascarada (`_`). A estrutura preserva os índices exatos de cada caractere, permitindo a substituição visual na posição correta assim que o jogador acerta um palpite.
*   **Conjuntos (`set`):** Implementação de um conjunto para gerenciar o histórico de palpites. A escolha do `set` foi estratégica devido à propriedade de **unicidade** (ignora letras duplicadas automaticamente) e à **alta eficiência computacional** (busca em tempo constante utilizando o operador `in` através de tabelas de dispersão internas).

### 3. Modularização de Código e Boas Práticas
*   Divisão do programa em funções com responsabilidades isoladas (`inicializar_jogo`, `processar_tentativa` e `jogar`), mantendo o fluxo principal limpo, enxuto e fácil de dar manutenção.
*   Nomeação de variáveis e funções seguindo o padrão padrão `snake_case` e escrita de documentações internas (*docstrings*) para cada função.

### 4. Resiliência e Ambiente de Desenvolvimento
*   Uso da biblioteca nativa `random` (método `random.choice()`) para garantir o sorteio pseudoaleatório das palavras de forma eficiente.
*   Resolução prática de problemas de ambiente, utilizando a execução visual via **IDLE do Python** para contornar limitações físicas de hardware (teclado).

---

## 🛠️ Como rodar o projeto

Caso queira testar o jogo na sua máquina:

1. Baixe o arquivo `jogo_forca.py`.
2. Abra o terminal ou o IDLE do Python na pasta do arquivo.
3. Execute o comando:
```bash
   python3 jogo_forca.py
