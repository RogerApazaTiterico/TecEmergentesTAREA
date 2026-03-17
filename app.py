print("hola mundo desde python")

#Entero
edad=20
#float
precio= 50.2
#str
nombre="Bruce Wayne"
#boolean
Bandera= True

#salida
print("Nombre: ",nombre)
print("Edad: ",edad)
print("Precio: "+str(precio))
print("Nombre: ",nombre)

#entrada
nombre= input("introduce tu nombre: ")
print("hola ",nombre)
#________________________

num1 = input("ingrese num 1") #son str
num2 = input("ingrese num 2") #son str
suma= num1+num2 # se concatena
print("la suma es: ",suma)

#convertir int, str, float 
num1 = input("ingrese num 1") #son str
num2 = input("ingrese num 2") #son str
suma= int(num1)+int(num2) # son enteros
print("la suma es: ",suma)
 

#__________________________
curso= "python para iniciantes"

#metodos
print(curso.upper())
print(curso)
print(curso.lower())
print(curso.capitalize())

#busquedas
print(curso.find("h"))
print(curso.find("ini"))

#reeemplazos
print(curso.replace("para","FOR"))
print(curso)

#operador
print("para" in curso)
print("PARA" in curso)
#__________________________#

#Operadores matematicos

print(15 + 5)
print(15 - 5)
print(15 * 5)
print(15 / 5) #presenta un valor float
#Division entera
print(15 // 5)
#Modulo - residuo
print(15 % 7)
#Exponente
print(2 ** 5)

x = 10
x = x+5
print(x)

#operador de asignacion compacto
y = 20
y *= 5
print(y)

#precedencia
x = 10 + 3 * 2
print(x)

#___________________________#

#Expresions booleanas true, false
#>,<, >=,<=, ==, !=

x = 3 > 2
print(x)

x=5 ==3
print(x)

x=5 != 3
print(x)

#operadores logicos
#and, or, not

precio=25
print(precio>10 and precio<30)

precio=5
print(precio>20 or precio<30)

print(not precio>10)

#sentencia if

temperatura = int(input("indice de temperatura: "))
if(temperatura >21):
    print("Hace calorcito")
elif temperatura >20:
    print("es un dia agradble")
elif temperatura>10:
    print("es un dia agradblemente frio ")
else: 
    print("hace alalau")
  
 #___________________________#       
#bucles
contador=12
while(contador <= 20 ):
    print(contador)
    contador += 1

i=1
while(i <=10):
    print(i*"+")
    i+=1
      

#listas
frutas=["manzana","piña","pera","lima"]
print(frutas)
print(frutas[1])
print(frutas[-1])
print(frutas[1:4])

#________________________#
#metodos de listas
numeros =[1,2,3,4,5]

numeros.append(6)
print(numeros)
#insertar elementos de una poscion determinada
numeros.insert(0,-1)
print(numeros)
numeros.insert(1,0)
print(numeros)
 
#eliminar numeros
numeros.remove(0)
print(numeros)

#verificar su un eleneto esta en la lista
print(8 in numeros)

#tamaño de la lista
print(len(numeros))

#eliminar el contenido de una lista
numeros.clear()
print(numeros)
#________________________________

#Objeto range
#numeros =list(range(3))
#print(numeros)
numeros = range(5)
print(numeros)

for item in numeros:
    print(item)

for item in range(5,10):
    print(item)
    
for item in range(10,20,3):
    print(item)
#____________________________
#TUPLAS
numeros=(1,2,3,5,4,5,6,7)
print(numeros[3])
print(numeros.count(5))

print(numeros.index(2))
print(numeros.index(3))

#___________________________________________
#Diccionarios -> almacena a pares de clave - valor
mi_diccionario={'nombre': 'bruno diaz', 'eded':'27','ciudad':'E l Alto'}
print(mi_diccionario)

#acceder aun valor
print(mi_diccionario['nombre'])
print(mi_diccionario['ciudad'])

#agragar elementos
mi_diccionario['profesion']='Ingeñero'
print(mi_diccionario)

#eliminar elemento
del mi_diccionario['ciudad']
print(mi_diccionario)

#obtenr clases del diciconario
print(mi_diccionario.keys())

#obtenr valoes del diciconario
print(mi_diccionario.values())

#verificar si una clave existe

if 'ciudad' in mi_diccionario:
    print("clave hallada")
    
#recorido de un diccionario
for clave, valor in mi_diccionario.items():
    print("[Clave:] ",clave,"[Valor:] ",valor)
   
#funciones -> son bloques de codigo que realiza una tarea en especifico
#y que son reutilizables


#funcion sin para metros ni devolucionde valor
def saludar():
    print("hola esto es python")
#llamada de funcion
saludar()

#funxion con parametros
def saludo(nombre):
    print("Hola "+nombre+" bienvanido a clases")
    
#llamada de funcion
saludo("Bruce Wayne")
saludo("Dick Grayson")

#establecer valore por defecto para parametros
def bienvenida(nombre="Estudiante"):
    print("Biemvenido ", nombre)
    
#llamada a la funcion
bienvenida()
bienvenida("susan")

#funcion que devuelve valor
def suma(a, b):
    return a+b

#llamda de funcion
resultado=suma(15,26)
print("la suma es: ",resultado)

#funsion con argumentos vaariables
def sumador(*args):
    return sum(args)
#llamada a la funcion
print(sumador(1,2,3,4,5))
print(sumador(4,5,6))
