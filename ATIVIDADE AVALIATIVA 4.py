# PEDRO HENRIQUE RODRIGUES PERNA
# 00220402523002
# Marcus melhor professor

print("Meu nome é PEDRO HENRIQUE RODRIGUES PERNA ")
print("Meu RA é 00220402523002 ")
print("Marcus é o melhor professor ")

P = int(input("Qual o valor inicial do investimento? "))
T = int(input("Qual o prazo do investimento (em meses)? "))

if T <6:
    taxa = P * 0.005
elif T >= 6 and T <= 12:
    taxa = P * 0.008
else:
    # T >12
    taxa = P * 0.012

rendimento_total = P * taxa * T
print(f"Sua taxa de juros mensal é {taxa} e o rendimento total é {rendimento_total:.2f}")