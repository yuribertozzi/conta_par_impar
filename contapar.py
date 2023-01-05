print()

terminou = False

p = i = 0


while terminou == False:

	print()
	
	n = int(input("Digite um número para aumentar de um a quantidade de pares ou ímpares: "))

	if n == 0:

		terminou = True

	else:

		if n % 2 == 0:

			p = p + 1

		else:

			i = i + 1

print()

print("p =", p)


print()

print("i =", i)