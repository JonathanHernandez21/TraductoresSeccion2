def ValidarAlfabeto(cadena):
    if cadena.lower():
      return 'la palabra esta en minusculas'  
    else:
      return 'la palabra es mayusculas' 

cadenas = raw_input('intruduzca la cadena de caracteres: ')
print ValidarAlfabeto(cadenas) 