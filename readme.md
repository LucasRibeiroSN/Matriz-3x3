# Calculadora de Determinante 3x3

Uma aplicação gráfica em Python para calcular o determinante de matrizes 3x3 usando interface Tkinter.

## 📋 Descrição

Este projeto implementa uma calculadora visual para determinantes de matrizes 3x3. A aplicação possui uma interface gráfica amigável onde o usuário pode inserir os valores da matriz e obter o resultado do determinante instantaneamente.

## 🚀 Acesso ao Vivo

Você pode visualizar o projeto em funcionamento no seguinte link:

### ➡️ [**Visitar o Portfólio**](https://lucas-ribeiro.vercel.app/)

## ⚡ Funcionalidades

- Interface gráfica intuitiva com campos de entrada para matriz 3x3
- Cálculo automático do determinante usando a regra de Sarrus
- Exibição formatada da matriz digitada
- Validação de entrada com tratamento de erros
- Resultado destacado com formatação visual
- Suporte a números decimais e inteiros

## 🚀 Como usar

### Pré-requisitos

- Python 3.x instalado
- Biblioteca Tkinter (geralmente incluída com Python)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/AdelirioAlexandre/Matriz-3x3.git
```

2. Navegue até o diretório do projeto:
```bash
cd Matriz-3x3
```

3. Execute o programa:
```bash
python main.py
```

### Como utilizar a interface

1. **Insira os valores**: Digite os 9 elementos da matriz 3x3 nos campos correspondentes
2. **Clique em "Calcular Determinante"**: O programa processará os dados
3. **Visualize o resultado**: A matriz digitada e o determinante serão exibidos na tela

## 📸 Exemplo de uso

```
Matriz exemplo:
[  1  2  3  ]
[  4  5  6  ]
[  7  8  9  ]

Determinante: 0
```

## 🧮 Fórmula utilizada

O determinante é calculado usando a fórmula:

```
det(A) = a(ei - fh) - b(di - fg) + c(dh - eg)
```

Onde a matriz A é:
```
[ a  b  c ]
[ d  e  f ]
[ g  h  i ]
```