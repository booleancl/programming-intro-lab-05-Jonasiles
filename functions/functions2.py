##Nuestra Primera Funcion

def song():
    print('No te pares frente a mi')
    print('Con esa mirada tan hiriente')

song()

print(type(song))

##Las funcions se pued utilizar tambien dentro de otras funciones

def chorus():
    song()
    song()

chorus()
