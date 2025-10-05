# PEDRO HENRIQUE RODRIGUES PERNA
# 00220402523002
# Marcus melhor professor

print("Meu nome é PEDRO HENRIQUE RODRIGUES PERNA ")
print("Meu RA é 00220402523002 ")
print("Marcus é o melhor professor ")

peso = float(input("Digite o peso da encomenda (em kg): "))
distancia = float(input("Digite a distância de entrega (em km): "))

custo_base = (peso * 1.5) + (distancia * 0.25)

if custo_base > 200:
    custo_final = custo_base * 0.90
elif 50 <= custo_base <= 200:
    custo_final = custo_base
else:
    custo_final = custo_base + 5.00

print(f"Custo base: R$ {custo_base:.2f}")
print(f"Custo final: R$ {custo_final:.2f}")