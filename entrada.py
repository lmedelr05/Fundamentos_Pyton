# function input - retorna string

num_a = int(input ("Ingresa un numero: "))
num_b = int(input ("Ingresa un numero: "))

print(num_a + num_b)
name = input("ingresa tu nombre: ")
age = int(input("ingresa tu edad: "))
city = input("ingresa tu ciudad/pueblo: ")

#string format
"""
Hola, soy name, tengo age años y vivo en city
"""
greeting = "Hola, soy {} tengo {} años y vivo en {}"
greeting.format(name, age, city)

print (greeting.format(name, age, city))

greeting_2 = f"Hola, soy {name} tengo {age} años y vivo en {city}"

print (greeting_2)