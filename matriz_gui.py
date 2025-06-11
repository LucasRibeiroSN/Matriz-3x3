import tkinter as tk
from tkinter import messagebox, font

# Função para calcular o determinante de uma matriz 3x3
def calcular_determinante_3x3(matriz):
    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]

    determinante = (a * (e * i - f * h) -
                    b * (d * i - f * g) +
                    c * (d * h - e * g))
    return determinante

# Função chamada ao clicar no botão
def calcular():
    try:
        matriz = []
        for i in range(3):
            linha = []
            for j in range(3):
                valor = entradas[i][j].get()
                linha.append(float(valor))
            matriz.append(linha)

        # Exibir matriz digitada
        matriz_str = "\n".join(
            ["[  " + "  ".join(f"{int(num)}" if num.is_integer() else f"{num:.2f}".rstrip("0").rstrip(".")
                               for num in linha) + "  ]"
                                for linha in matriz]
        )
        matriz_label.config(text=f"Matriz Digitada:\n{matriz_str}")

        # Calcular determinante
        determinante = calcular_determinante_3x3(matriz)
        formata_texto = (
            f"Determinante: {int(determinante)}"
            if determinante.is_integer()
            else f"Determinante: {determinante:.4f}"
        )

        resultado_label.config(
            text= formata_texto,
            # text=f"Determinante: {determinante:.4f}",
            font=font.Font(size=26, weight="bold"),
            fg="darkblue"
        )

    except ValueError:
        messagebox.showerror("Erro", "Todos os campos devem conter números válidos.")

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora de Determinante 3x3")
janela.geometry("800x850")  # Tela grande

# Instrução
instrucoes = tk.Label(janela, text="Digite os elementos da matriz 3x3:", font=("Arial", 20))
instrucoes.pack(pady=20)

# Frame das entradas
entrada_frame = tk.Frame(janela)
entrada_frame.pack(pady=20)

# Entradas da matriz
entradas = []
for i in range(3):
    linha = []
    for j in range(3):
        entrada = tk.Entry(entrada_frame, width=10, font=("Arial", 24), justify="center", borderwidth=2, relief="solid")
        entrada.grid(row=i, column=j, padx=15, pady=15)
        linha.append(entrada)
    entradas.append(linha)

# Botão para calcular
botao = tk.Button(janela, text="Calcular Determinante", font=("Arial", 18, "bold"), bg="#0066cc", fg="white", padx=20, pady=10, command=calcular)
botao.pack(pady=30)

# Exibição da matriz digitada
matriz_label = tk.Label(janela, text="", font=("Courier New", 20), justify="left")
matriz_label.pack(pady=10)

# Resultado do determinante
resultado_label = tk.Label(janela, text="Determinante:", font=("Arial", 22))
resultado_label.pack(pady=30)

# Executar janela
janela.mainloop()

if __name__ == "__main__":
    matriz_label()