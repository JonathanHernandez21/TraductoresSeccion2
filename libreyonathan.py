def ValidaPalabra(pala):
    if pala.isspace():
       return 'la palabra contiene espacio en su escritura' 
    elif not pala.isspace():
       return 'la palabra no posee espacio en su escritura'
    else:
       return 'lol' 

pala = raw_input('introduza la palabra: ')
print ValidaPalabra(pala) 