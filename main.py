def isMutant(adn):
  secuencia=0
  #HORIZONTAL
  for i in adn:
    for j in range(2):
      if i[j]==i[j+1] and i[j]==i[j+2] and i[j]==i[j+3]:
        secuencia=secuencia+1
  #VERTICAL
  for i in range(2):
    if adn[i][0]==adn[i+1][0] and adn[i][0]==adn[i+2][0] and adn[i][0]==adn[i+3][0]:
      secuencia=secuencia+1
  #DIAGONAL 
  for i in range(2):
    if adn[i][0]==adn[i+1][1] and adn[i][0]==adn[i+2][2] and adn[i][0]==adn[i+3][3]:
      secuencia=secuencia+1
  #DIAGONAL 2
  for i in range(2):
    if adn[i][3]==adn[i+1][2] and adn[i][3]==adn[i+2][1] and adn[i][3]==adn[i+3][0]:
      secuencia=secuencia+1
      
  return secuencia>1

def validar(i):
  print(f"Ingrese la fila {i} de genes:")
  gen=input().upper()
  if gen.count("A")+gen.count("T")+gen.count("C")+gen.count("G")!=6:
    print("Fila inválida")
    gen=validar(i)

  return gen

adn=[]
for i in range(6):  
    adn.append(validar(i+1))

if isMutant(adn):
  print("El ADN es mutante")
else:
  print("El ADN no es mutante")