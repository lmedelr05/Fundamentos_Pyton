# funciones en Python
# def name_function(params):
# codigo
# return

# Funcion sin parametros y sin retorno 
def saludos():
    print("Hola a to2")

saludos()    

# Funciones con un parametro
def get_age_in_future(age):
    print (f"En 3 años tendras {age + 3} años")


get_age_in_future(39)

# funciones con 2 parametros sin retorno

def suma (num1, num2):
    print(f"{ num1 } + { num2} = { num1 + num2 }")

    suma(12, 35)

# funuciones con parametros opcionales 

def get_heroes(h1 = "ironman", h2 = "spiterman"):
    print([h1, h2])

get_heroes()
get_heroes("batman")
get_heroes("batman", "spiterman")

# funciones con retorno
def tittle(texto):
    return texto.title()

text_changed = tittle("HoLa A thO2")

print(text_changed)



