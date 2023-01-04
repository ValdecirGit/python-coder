a = 5
b = 3.5
print(a + b)


text = 'Valdecir'
idade = 45

#interpolação de valores
print(f"{text} sua idade é {idade} anos") 

# multiplicando a mensagem
print(3 * ' Bom Dia ') 

# multiplicando com varivel sem aspas 
saudacao = "Bom Tarde "
print(3 * saudacao) 

PI = 3.14
raio = float(input("informe o raio do círculo:"))

area = PI * raio * raio
print(f'A àrea da circunferência: {raio} é de {area} m2')

print('cálculo área usando potência:')
area = PI * pow(raio, 2) # calculo usando potência
print(f'A àrea da circunferência: {raio} é de {area} m2')