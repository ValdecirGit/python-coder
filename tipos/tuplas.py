nomes = ("Valdecir", "Neia", "Caue", "Erick", "Pingo", "Lilica")

print("Tipo de variável tupla:")
print(type(nomes))
print(nomes)

print("Valida se o nome Bia esta contido na tupla nomes")
print("Bia" in nomes)

print("Valida se o nome Erick esta contido na tupla nomes")
print("Erick" in nomes)

print("Acessando primeito elemento")
print(nomes[0])

print("Acessando primeito elemento 1 sem incluir o segundo")
print(nomes[1:2])

print("Acessando elemento 1 incluindo o segundo")
print(nomes[1:3])

print("Acessando todos os elementos a partir do segundo elemento")
print(nomes[1:])

print("Não necessariamente pq tem parenteses quer dizer que é um tupla")
x = ('Bia')
print(type(x))

print("Não necessariamente pq tem parenteses quer dizer que é um tupla, mas se tiver mais uma virgula após o valor ae sim é uma tupla")
x = ('Bia',)
print(type(x))

print("Quantidades de elementos da tupla")
print(len(nomes))