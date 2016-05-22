def ValidarNumeros(a, b):
    if a < b:
      return 'el valor de a  es menor al de b' 
    elif a > b:
      return 'el valor de b  es menor al de a' 
    else:
      return 'ambos numeros son iguales' 

a = raw_input('ingrese el valor de a: ')
b = raw_input('ingrese el valor de b: ') 
print ValidarNumeros(a, b) 
 