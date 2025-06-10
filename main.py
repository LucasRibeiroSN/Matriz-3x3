# Solicita os elementos da matriz ao usuario
def matriz_3x3_usuario_input():
    matriz = []
    print("Digite os elementos da matriz 3x3: ")

    for i in range(3):
        linha = []
        for j in range(3):
            while True:
                try:
                    elemento = float(input(f"Elemento [{i+1}][{j+1}]: "))
                    linha.append(elemento)
                    break
                except ValueError:
                    print("Entrada Invalida, Tente novamente.")
        matriz.append(linha)
    return matriz

# exibe a matriz ja formatada
def exibir_matriz(matriz, nome = "Matriz"):
    if not matriz or not all(len(linha) == len(matriz[0]) for linha in matriz):
        print(f"{nome} invalida para exibição")
        return

    print(f"{nome}:")
    for linha in matriz:
        print("[", end ="")
        for elemento in linha:
            print(f" {elemento:5.2f} ", end="")
        print("]")
    print()

# calcula a determinante da matriz
def calcular_determinante_3x3(matriz):
    if len(matriz) != 3 or any(len(linha) != 3 for linha in matriz):
        raise ValueError("Matriz invalida para calcular o determinante, tem que ser uma matriz 3x3.")

    a,b,c = matriz[0]
    d,e,f = matriz[1]
    g,h,i = matriz[2]

    determinate = (a * (e * i - f * h) -
                   b * (d * i - f * g) +
                   c * (d * h - e * g))
    return determinate

# Função principal para executar o programa
def main():
    print("Calculadora de Determinante de Matriz 3x3")
    print("=====================================")

    # Obtem a matriz do usuario
    matriz_usuario = matriz_3x3_usuario_input()

    # exibe a matriz do usuario
    exibir_matriz(matriz_usuario, "Matriz do Usuario")

    # calcula e exibe o determinante da matriz
    try:
        det = calcular_determinante_3x3(matriz_usuario)
        print(f"O determinante da matriz é: {det:.4f}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
