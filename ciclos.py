# ciclo white 
# WHile Exp_bool: True 

i = 0
num = 7
while i <= 10:
    print(f"{ num } * { i } = { num * i}")
    i += 1
else:
  print ("ciclo terminado")

# Ciclo inifinito
while True:
    # rompemos con break
    break

# El for recorre interables
# Un interable es algo que se puede recorrer 

# for variable in interable:
my_string = "Hola"

for letra in my_string:
    print(letra, end=", ")

lista = ["uno", "dos", "tres", "cuatro"] 
for item in lista:
    print(item)   

# function range 
# range(end)
for i in range(10):
   print(1, end=', ')
print()
# range(ini, end)
for i in range(10, 20):
    print(i, end=', ')
print()
# range(ini, end, step)
for i in range(10, 20, 2):
    print(i, end=', ')
print()