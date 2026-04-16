print("--- Simulador de Função de 1º Grau ---")

a = float(input("Digite o valor do coeficiente angular (a): "))
b = float(input("Digite o valor do coeficiente linear (b): "))

if a == 0:
    print("Se 'a' é zero, a função é constante.")
else:
    raiz = -b / a
    print(f"A função modelada é: f(x) = {a}x + {b}")
    print(f"A raiz da função (ponto onde a reta corta o eixo x) é: {raiz}")

# Representação de pares ordenados para visualização
print("\nGerando coordenadas para o gráfico:")
for x in range(-2, 3):
    y = a * x + b
    print(f"Para x = {x}, y = {y} -> Ponto ({x}, {y})")