numeros = int(input("Ingrese la cantidad de numeros:"))
pares = 0
suma = 0

while numeros > 0:
	n = int(input("Ingrese el numero: "))
	if n % 2 == 0:
		pares+=1
		suma += n
	numeros -=1
	else:
		impares = impares + 1
		print(f"El total de pares es: {impares}")

if pares > 0:
	promedio = suma / pares
	print(promedio)
else:
	print("No es par")
