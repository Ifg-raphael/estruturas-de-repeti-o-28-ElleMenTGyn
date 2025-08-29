soma = 0.0                 # variavel para acumular a soma dos números

for _ in range(5):         # leitura de 5 valores
    numero = float(input())  # lê um numero
    soma += numero           # adiciona à soma

media = soma / 5            # calcula a média(5)
print(f"{media:.2f}")       # imprime a média com 2 casas decimais