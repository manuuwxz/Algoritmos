import random

def jogoNumeroBuscaBinaria():
    print("    Jogo: Adivinhe o Número    ")
    print("Pense em um número inteiro entre 1 e 100, e eu tentarei adivinhar!")
    input("Pressione Enter quando estiver pronto...")

    limiteInferior = 1
    limiteSuperior = 100
    tentativas = 0
    
    while True:
        tentativas += 1
        
        palpite = (limiteInferior + limiteSuperior) // 2
        
        print(f"\nMinha {tentativas}ª tentativa: O número é {palpite}?")
        
        resposta = input("Digite 'maior', 'menor' ou 'correto': ").lower()
        
        if resposta == 'correto':
            print(f"\nAcertei o número {palpite} em {tentativas} tentativas!")
            break
        elif resposta == 'maior':
            limiteInferior = palpite + 1
        elif resposta == 'menor':
            limiteSuperior = palpite - 1
        else:
            print("Resposta inválida. Por favor, digite 'maior', 'menor' ou 'correto'.")
            tentativas -= 1
        
        if limiteInferior > limiteSuperior:
            print("\nAlgo deu errado! Parece que suas dicas foram inconsistentes. Não consegui encontrar o número.")
            break

jogoNumeroBuscaBinaria()