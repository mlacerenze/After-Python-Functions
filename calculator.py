# CALCULADORA EN PYTHON
# Qué son las funciones? -> Trozos de código que usamos cuando queremos

# 1 Parte - Crear funciones aritméticas
def sumar(n1=0, n2=0):
  return n1 + n2

def restar(n1=0, n2=0):
  return n1 - n2

def multiplicar(n1=0, n2=0):
  return n1 * n2 

def dividir(n1=0, n2=0):
  return n1 / n2

def potencia(n1=0, n2=0):
  #          2 a la 3 
  return pow(n1, n2)

def raiz_cuadrada(n1=0):
  return n1 ** 0.5

print('BIENVENIDO A LA CALCULADORA DE PYTHON')
# 2 Parte - Crear menú de opciones
def menu(): # el usuario ve las opciones que puede realizar
  print('ELIJA UNA OPCIÓN')
  print('1- Sumar')
  print('2- Restar')
  print('3- Multiplicar')
  print('4- Dividir')
  print('5- Potencia')
  print('6- Raíz Cuadrada')
  print('7- Salir')


# 3 Parte - Ingreso números
def ingresar_numeros():
  n1 = int(input('Ingrese primer numero: '))
  n2 = int(input('Ingrese segundo numero: '))
  return n1, n2

def ingresar_numero():
  n1 = int(input('Ingrese numero: '))
  return n1


# 4 Parte - Creación del main (el que maneja todo)
def main():
  menu()
  opcion = 's' # opción para salir del programa
  while opcion == 's': # mientras la opción sea 's' que siga corriendo
    eleccion = input('Ingrese opción: ')
    if eleccion == '1':
      n1, n2 = ingresar_numeros()
      print('SUMA:', sumar(n1, n2))
    elif eleccion == '2':
      n1, n2 = ingresar_numeros()
      print('RESTA:', restar(n1, n2))
    elif eleccion == '3':
      n1, n2 = ingresar_numeros()
      print('MULTIPLICACION:', multiplicar(n1, n2))
    elif eleccion == '4':
      n1, n2 = ingresar_numeros()
      print('DIVISION:', dividir(n1, n2))
    elif eleccion == '5':
      n1, n2 = ingresar_numeros()
      print('POTENCIA:', potencia(n1, n2))
    elif eleccion == '6':
      n1 = ingresar_numero()
      print('RAIZ CUADRADA:', raiz_cuadrada(n1))
    elif eleccion == '7':
      print('Gracias por utilizar esta calculadora, vuelva prontos!')
      break
    else:
      print('Opción inválida!!')
      continue

    opcion = input('Quiere hacer otra operación? (s/n)')
    if opcion == 's':
      menu()
    else:
      print('Gracias, compre mi programa así puedo comer...')
      break

main()