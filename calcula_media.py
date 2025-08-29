# Lê 5 números que chegam na MESMA linha.
a, b, c, d, e = map(float, input().split())

# Soma os 5 valores e divide por 5 para obter a média
media = (a + b + c + d + e) / 5

# Mostra a média com 2 casas decimais (ajuste se quiser outro formato)
print(f"{media:.2f}")