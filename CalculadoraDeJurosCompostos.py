def calcula_juros_compostos(principal, taxa_juros, tempo):
    """
    Calcula o valor final de um investimento com base no principal, 
    na taxa de juros e no tempo.

    Args:
        principal (float): Valor inicial do investimento.
        taxa_juros (float): Taxa de juros anual.
        tempo (int): Tempo de investimento em anos.

    Returns:
        float: Valor final do investimento.
    """
    return principal * (1 + taxa_juros / 100) ** tempo

def main():
    print("Calculadora de Juros Compostos")
    print("-----------------------------")

    principal = float(input("Digite o valor inicial do investimento (R$): "))
    taxa_juros = float(input("Digite a taxa de juros anual (%): "))
    tempo = int(input("Digite o tempo de investimento em anos: "))

    valor_final = calcula_juros_compostos(principal, taxa_juros, tempo)

    print(f"\nO valor final do investimento é: R${valor_final:.2f}")

if __name__ == "__main__":
    main()