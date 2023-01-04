nums = [1, 2, 3]

print("Valida se o o numero 4 esta contido na lista nums")
print(nums)
print(4 in nums)

print("Valida se o o numero 3 esta contido na lista nums")
print(nums)
print(3 in nums)


#tipo de lista
print(type(nums))

#adicionar elemento da lista
print('adicionar elemento da lista:')
nums.append(3)
nums.append(7)
print(nums)

#ver quando elementos tem a lista
print('ver quando elementos tem a lista')
print(len(nums))

# alterar valor da lista
print('alterar valor da lista, acesso indice que começa pelo zero')
nums[3] = 100
print(nums)

# inserir dados na lista
print('inserir dados na lista indicar posicao do indice')
nums.insert(0, -250)  
print(nums)

# acessar um numero a partir do elemento
print('acessar um numero a partir do elemento')
print(nums[5])

# capturando o ultimo elemento vindo de tras pra frente
print('capturando o ultimo elemento vindo de tras pra frente')
print(nums[-1])

# capturando penúltimo elemento vindo de tras pra frente
print('capturando o ultimo elemento vindo de tras pra frente')
print(nums[-2])


