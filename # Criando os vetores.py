# Criando os vetores
vetor1 = []
vetor2 = []
vetor3 = []

# Lendo os valores do primeiro vetor
print("Digite os 10 elementos do primeiro vetor:")
for i in range(10):
    valor = int(input(f"Elemento {i + 1}: "))
    vetor1.append(valor)

# Lendo os valores do segundo vetor
print("\nDigite os 10 elementos do segundo vetor:")
for i in range(10):
    valor = int(input(f"Elemento {i + 1}: "))
    vetor2.append(valor)

# Intercalando os elementos
for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

# Exibindo o terceiro vetor
print("\nVetor intercalado:")
print(vetor3)