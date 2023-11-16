# Mutantes
Julieta Sena
 - julietaasena@gmail.com
 - Legajo: 51646

# Desarrollo
Se desarrollo un programa para determinar si una cadena de ADN es mutante o no. El ADN se representa como una lista de cadenas, donde cada cadena es una fila de genes. Primero defino la función isMutant(), la cual busca y cuenta la cantidad de secuencias encontradas en el adn ingresado. Luego, defino la función validar() para absorber algunos posibles errores del usuario. Por último, encontramos el código dónde se utiliza las funciones mencionas y, dependiendo del resultado, anuncia si es o no mutante.
## Función isMutant(adn)
Para empezar, se inicializa una variable "secuencia" que sirve para contar cuantas secuencias se encontraron en el adn. En caso de ser mayor a 1 la función devuelve True, caso contrario False.
Luego utilizo 2 bucles for para cada validación de secuencia:
 - horizontal: el primer bucle recorre filas y el segundo recorre las 3 posibles columnas para el inicio de secuencia, al tener secuencias de tamaño 4 no podria comenzar en la columna 4. Para verificar utilizo un if que compare la igualdad de las letras, aumentando en uno el valor de secuenca en caso de encontrar alguna coincidencia.
 - vertical: análogo a horizontal, el primer bucle recorre las columnas y el segundo recorre las 3 posibles filas para el inicio de secuencia.
 - diagonal hacia abajo: los bucle recorren las 3 posibles filas y columnas de inicio de secuencia. Para verificar utilizo un if que compare la igualdad de las letras entre las casillas en diagonal, , aumentando en uno el valor de secuenca en caso de encontrar alguna coincidencia.
 - diagonal hacia arriba: funciona de igual manera que diagonal hacia abajo con la diferencia que recorre las ultimas 3 filas y las casillas en diagonal van decreciendo.
## Función validar(i)
Esta funcion se desarrollo para abarcar posibles errores del usuario. Por un lado, corrobora que la cantidad y el tipo de letras ingresadas sean las correctas, caso contrario pide ingresar nuevamente la fila. Por el otro, abarca la posibilidad del uso de minúsculas.

# Casos

## Caso 1 : Mutante
Ingreso las siguientes filas de instrucciones:

ATGCGA

CACTGT

TCATTG

CATATC

TGAGGG

CCTGAA

Se encuentran 2 secencias diagonales: la primera comienza en la fila 1 columna 1 con la letra A y desciende a la derecha, la segunda comienza en la fila 1 columna 4 y desciende a la izquierda.

## Caso 2 : Mutante
En este caso probaremos la validación del ingreso equivocado de genes.

aTgcGA  -> acepta ingresos de minúsculas por lo que continúa con el programa

CACTGTT -> al ingresar una letra demás (o de menos) vuelve a pedir la fila

CACTGT

TCATTr  -> al ingresar una letra que no corresponde vuelve a pedir la fila

TCATTT

CATATC

TGAGGG

CCTGAA

Al ser la misma matriz del caso 1 se encuentran 2 secencias diagonales.

## Caso 3 : Mutante
Ingreso las siguientes filas de instrucciones:

GTCAAT

TTGACT

TTTAGC

GAAAAC

CAGTGC

CCCATG

Se encuentran 2 secuencias: una horizontal en la fila 4 y una vertical en la columna 4.

## Caso 4 : No Mutante
Ingreso las siguientes filas de instrucciones:

GTCAAC

TTGACC

TTTAGT

GccAAG

CAGTGA

CCCATG

Se encuentra únicamente una secuencia en la columna 4.
