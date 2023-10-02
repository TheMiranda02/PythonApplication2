
#PRACTICA 02
#JOSE ELIAS GUZMAN MIRANDA

NUM = 8
NUMS=[0]*NUM
total=0

for i in range (NUM):
    NUMS [i]=int(input("Introduzca un numero: "))
    total+=NUMS[i]

print("El total de la suma es: ",total)