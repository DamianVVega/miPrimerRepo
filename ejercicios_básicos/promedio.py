#Crea un programa donde se ingresen 5 numeros y devuelva su promedio#
lista=[]
for i in range(5):
    numero=int(input(f"Ingrese el numero {i+1}: "))
    lista.append(numero)
promedio=sum(lista)/len(lista)
print(f"El promedio es :{promedio}")