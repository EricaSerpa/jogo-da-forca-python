"""
Experiência Prática 3: Desenvolvimento de Jogo Educativo (Jogo da Forca)
Disciplina: Programação de Computadores
Autor: Aluna em Aprendizagem
Descrição: Um jogo da forca simplificado que integra funções, controle de fluxo,
           listas e conjuntos para um ambiente interativo no terminal.
"""

import random


def inicializar_jogo():
    """Escolhe uma palavra aleatória e prepara as lacunas iniciais do jogo.

    Retorna:
        tuple: A palavra_secreta (str) e a lista de letras_descobertas (list).
    """
    # Banco de palavras padronizado em maiúsculas e sem acentos
    lista_palavras = ["PYTHON", "PROGRAMACAO", "ESTRUTURA", "COMPUTADOR", "ALGORITMO"]

    # Utilização da biblioteca random para garantir o comportamento aleatório
    palavra_secreta = random.choice(lista_palavras)

    # Uso de LISTA para armazenar as lacunas: estrutura mutável e ordenada
    # que preserva os índices exatos de cada caractere na palavra
    letras_descobertas = ["_"] * len(palavra_secreta)

    return palavra_secreta, letras_descobertas


def processar_tentativa(letra, palavra_secreta, letras_descobertas):
    """Varre a palavra secreta para verificar se o palpite do jogador está correto

    e atualiza o painel de lacunas caso encontre correspondências.

    Parâmetros:
        letra (str): O palpite atual do usuário.
        palavra_secreta (str): A palavra que deve ser adivinhada.
        letras_descobertas (list): A lista contendo o status atual das lacunas.

    Retorna:
        bool: True se o palpite for correto, False caso contrário.
    """
    acertou = False

    # Percorre a palavra usando enumerate() para obter o índice e o caractere
    for indice, caractere in enumerate(palavra_secreta):
        if caractere == letra:
            letras_descobertas[indice] = letra  # Modifica a lista na posição exata
            acertou = True

    return acertou


def jogar():
    """Função principal que orquestra o fluxo do jogo através do laço while."""
    # Inicialização do estado do jogo a partir da função modularizada
    palavra_secreta, letras_descobertas = inicializar_jogo()

    # Uso de CONJUNTO (set) para rastrear o histórico de palpites do jogador.
    # Justificativa: Garante a unicidade dos elementos (não permite letras duplicadas)
    # e possui alta eficiência computacional na busca com o operador 'in'.
    letras_tentadas = set()

    tentativas_restantes = 6

    print("=========================================")
    print("      BEM-VINDO AO JOGO DA FORCA!        ")
    print("=========================================")

    # Laço de repetição (while) que atua como o motor central da partida
    while tentativas_restantes > 0 and "_" in letras_descobertas:
        # Exibição do status atual formatado de maneira amigável ao usuário
        palavra_formatada = " ".join(letras_descobertas)
        print(f"\nPalavra atual: {palavra_formatada}")
        print(f"Letras já tentadas: {list(letras_tentadas)}")
        print(f"Tentativas restantes: {tentativas_restantes}")

        # Coleta e padronização da entrada de dados (limpeza de espaços e caixa alta)
        palpite = input("Digite uma letra: ").strip().upper()

        # Validação para garantir que o usuário digitou apenas uma letra válida
        if len(palpite) != 1 or not palpite.isalpha():
            print("⚠️ Entrada inválida! Por favor, digite apenas uma letra.")
            continue

        # Tratamento de redundâncias: impede o gasto de vidas com letras repetidas
        if palpite in letras_tentadas:
            print(f"⚠️ Ops! Você já tentou a letra {palpite} antes. Tente outra!")
            continue

        # Adiciona o palpite inédito ao conjunto de controle
        letras_tentadas.add(palpite)

        # Processamento e ramificação de feedbacks baseado nas condicionais
        if processar_tentativa(palpite, palavra_secreta, letras_descobertas):
            print("✨ Muito bem! Você acertou uma letra!")
        else:
            print("❌ Letra incorreta! Você perdeu 1 tentativa.")
            tentativas_restantes -= 1

    # Encerramento do jogo e verificação do status final (Vitória ou Derrota)
    print("\n=========================================")
    if "_" not in letras_descobertas:
        print(
            f"🎉 PARABÉNS! Você venceu ao descobrir a palavra secreta '{palavra_secreta}'!"
        )
    else:
        print(
            f"☠️ Fim de jogo! Suas tentativas acabaram. A palavra era: '{palavra_secreta}'"
        )
    print("=========================================")


# Ponto de entrada padrão para execução do script em Python
if __name__ == "__main__":
    jogar()