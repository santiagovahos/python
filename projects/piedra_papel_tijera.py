import random
round = 0
w = 0
l = 0
t = 0
while True:
    print("*" * 20)
    print('ROUND', round)
    print("*" * 20)
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Salir")
    opcion = int(input("Elige una opción: "))
    if opcion == 4:
        break
    elif opcion == 1:
        print("Elegiste piedra🗿")
    elif opcion == 2:
        print("Elegiste papel🧻")
    elif opcion == 3:
        print("Elegiste tijera✂️")
    else:
        print("Opción no válida")
        break
    megatron = random.randint(1, 3) # random.randint(a, b) genera un número aleatorio entre a y b
    if megatron == 1:
        print("🤖Megatron🤖 elige piedra🗿") 
    elif megatron == 2:
        print("🤖Megatron🤖 elige papel🧻")
    elif megatron == 3:
        print("🤖Megatron🤖 elige tijera✂️")
    if opcion == 1 and megatron == 3:
        print("Ganaste!")
        w += 1
    elif opcion == 2 and megatron == 1:
        print("Ganaste!")
        w += 1
    elif opcion == 3 and megatron == 2:
        print("Ganaste!")
        w += 1
    elif opcion == megatron:
        print("Empate!")
        t += 1
    else:
        print("Perdiste!")
        l += 1
    round += 1

print("*" * 25)
print(f'Tu número de victorias fue: {w}, es decir, ganaste el {(w/round)*100}% de las partidas')
print(f'Tu número de derrotas fue: {l}, es decir, perdiste el {(l/round)*100}% de las partidas')
print(f'El numero de empates fue: {t}, es decir, empataron el {(t/round)*100}% de las partidas')
print('*' * 25)
if w > l:
    print('¡Eres el ganador!')
elif l > w:
    print('¡El ganador es 🤖Megatron🤖!')
else:
    print('No hay ganador en este set')
print('*' * 25)
print("Gracias por jugar!")
print('*' * 25)