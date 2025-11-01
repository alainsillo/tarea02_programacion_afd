''''
Ejercicio 1 - El perrito guardián
En este ejercicio se pide diseñar un AFD que acepte todas las cadenas sobre {a,b} que contienen la subcadena 'aba'. Es decir, el autómata debe reconocer cuando la secuencia 'aba' aparece en cualquier parte de la cadena. Este patrón permite que el AFD avance de un estado a otro conforme detecta las letras hasta completar la subcadena.
Σ = {a, b}
L = {aba, abab, baba, aabaa, ababa, …}
'''

adf={
    'estados':{ '1', '2', '3', '4'},
    'alfabeto':{ 'a', 'b'} ,
    'transiciones': { 
                    '1':{ 'a': '2', 'b': '1'},
                    '2':{ 'a': '2', 'b': '3'},
                    '3':{ 'a': '4', 'b': '1'},                    
                    '4':{ 'a': '4', 'b': '4'}
    },
    'estado_inicial': '1',
    'estados_finales': { '4'}
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

cadena="abab"
print(f"Procesando la cadena { cadena}")
resultado=evaluacion(adf, cadena)
print(f"Se acepto?, {resultado}")