import time


numero_inicial = int(input("Digite um número para iniciar a contagem regressiva: "))

print("Iniciando contagem... ")


for segundo in range(numero_inicial, 0, -1):
    print(f"{segundo}...")

    time.sleep(1)

print("Lançar! 🚀")