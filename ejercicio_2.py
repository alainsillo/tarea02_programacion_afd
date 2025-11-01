'''
Ejercicio 2 - El gatito de los tres pasos
Aquí se construye un AFD que acepte cadenas cuya longitud sea múltiplo de 3. Esto significa que el autómata regresará al estado inicial cada vez que haya leído tres símbolos, sin importar si son 'a' o 'b'.
Σ = {a, b}
L = {ε, aaa, bbb, aab, abb, …}
'''


adf={
    'estados':{ '1', '2', '3', '4', '5'},
    'alfabeto':{ 'a', 'b'} ,
    'transiciones': { 
                    '1':{ 'a': '2', 'b': '3'},
                    '2':{ 'a': '4', 'b': '5'},
                    '3':{ 'a': '5', 'b': '4'},
                    '4':{ 'a': '1', 'b': '1'},                                          
                    '5':{ 'a': '1', 'b': '1'}
    },
    'estado_inicial': '1',
    'estados_finales': { '1'}
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

cadena="aab"
print(f"Procesando la cadena { cadena}")
resultado=evaluacion(adf, cadena)
print(f"Se acepto?, {resultado}")