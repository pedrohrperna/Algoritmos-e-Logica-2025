# PEDRO HENRIQUE RODRIGUES PERNA
# 00220402523002
# Marcus melhor professor

print("Meu nome é PEDRO HENRIQUE RODRIGUES PERNA ")
print("Meu RA é 00220402523002 ")
print("Marcus é o melhor professor ")

C_inicial = float(input("Digite o custo inicial do material: "))
Q = int(input("Digite a quantidade de itens produzidos: "))
Dias = int(input("Digite o número de dias de atraso: "))
Defeito = float(input("Digite o percentual de defeitos (ex: 0.05 para 5%): "))

if Q > 1000 and C_inicial > 5000:
    F_comp = 1.15
else:
    F_comp = 1.05

C_corrigido = C_inicial * F_comp

if Defeito > 0.10 or Dias > 5:
    print("Penalidade Alta: 20% de redução no lucro.")
    C_final = C_corrigido * 1.25
elif 0.05 <= Defeito <= 0.10 and Dias > 0:
    print("Penalidade Média: 10% de redução no lucro.")
    C_final = C_corrigido * 1.10
else:
    print("Sem penalidade. Custo final apenas com correção.")
    C_final = C_corrigido

print(f"Custo Base Corrigido: R$ {C_corrigido:.2f}")
print(f"Custo final: R$ {C_final:.2f}")