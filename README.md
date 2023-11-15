# Mutantes
Julieta Sena
 - julietaasena@gmail.com
 - DNI: 40561630
#Desarrollo

#Caso 1 : Mutante
Ingreso las siguientes filas de instrucciones:

ATGCGA
CACTGT
TCATTG
CATATC
TGAGGG
CCTGAA

Se encuentran 2 secencias diagonales: la primera comienza en la fila 1 columna 1 con la letra A y desciende a la derecha, la segunda comienza en la fila 1 columna 4 y desciende a la izquierda.

#Caso 2 : Mutante
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

#Caso 3 : Mutante
Ingreso las siguientes filas de instrucciones:

GTCAAT
TTGACT
TTTAGC
GAAAAC
CAGTGC
CCCATG

Se encuentran 2 secuencias: una horizontal en la fila 4 y una vertical en la columna 4.

#Caso 4 : No Mutante
Ingreso las siguientes filas de instrucciones:

GTCAAC
TTGACC
TTTAGT
GccAAG
CAGTGA
CCCATG

Se encuentra únicamente una secuencia en la columna 4.
