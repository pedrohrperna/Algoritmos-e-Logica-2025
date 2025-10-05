# PEDRO HENRIQUE RODRIGUES PERNA
# 00220402523002
# Marcus melhor professor

print("Meu nome é PEDRO HENRIQUE RODRIGUES PERNA ")
print("Meu RA é 00220402523002 ")
print("Marcus é o melhor professor ")

valor = float(input("Qual o valor da glicose em jejum? (mg/dL) "))

if valor < 100:
    print("Glicemia Normal.")
elif valor >= 100 and valor <= 125:
    print("Pré-diabetes: Risco Moderado.")
else:
    print("Diabetes: Nível Alto.")