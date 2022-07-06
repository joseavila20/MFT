print("==============")
print("Bienvenido")
print("==============")
print("\n¿Numero par ó impar?")


while True:
	try:

		numero = int(input("\nIntroduzca un numero: "))
	except ValueError:
		print("\nDebes escribir un numero.")
		continue
	if numero < 0:
		print("\nDebes escribir un numero mayor que cero")
		continue
	else:
		break

respuesta = (numero % 2)

if respuesta == 0:
	print("\nEl numero", numero, "es par.")
else:
	print("\nEl numero", numero, "es impar.")

print("\n\nFIN")