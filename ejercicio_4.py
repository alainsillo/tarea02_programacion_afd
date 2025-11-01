''''
Ejercicio 4 - El conejo que termina en 'bb'
En este caso, se diseña un AFD que acepte cadenas que terminen con la subcadena 'bb'. El autómata debe recordar las dos últimas letras leídas para determinar si coinciden con 'bb'.
Σ = {a, b}
L = {bb, abb, aabb, babb, …}
'''

adf={
    'estados':{ '1', '2', '3'},
    'alfabeto':{ 'a', 'b'} ,
    'transiciones': { 
                    '1':{ 'a': '1', 'b': '2'},
                    '2':{ 'a': '1', 'b': '3'},                  
                    '3':{ 'a': '1', 'b': '3'}
    },
    'estado_inicial': '1',
    'estados_finales': { '3'}
}
def evaluacion(adf, palabra):
    estado_actual= adf[ 'estado_inicial']
    for simbolo in palabra:
        if simbolo not in adf[ 'alfabeto']:
            print(f"Alguno de los caracteres{ simbolo}, no pertenece al alfabeto")
            return False
        estado_actual= adf[ 'transiciones'][estado_actual][simbolo]
        print(f"{ simbolo} > { estado_actual}")
    return estado_actual in adf[ 'estados_finales']

cadena="abb"
print(f"Procesando la cadena { cadena}")
resultado=evaluacion(adf, cadena)
print(f"Se acepto?, {resultado}")