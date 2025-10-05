# PEDRO HENRIQUE RODRIGUES PERNA
# 00220402523002
# Marcus melhor professor

print("Meu nome é PEDRO HENRIQUE RODRIGUES PERNA ")
print("Meu RA é 00220402523002 ")
print("Marcus é o melhor professor ")

preco_custo = float(input("Qual o valor de custo do produto? "))
preco_venda = float(input("Qual o valor de venda do produto? "))

lucro_absoluto = (preco_venda - preco_custo)
margem = (lucro_absoluto / preco_custo) *100

if margem >30:
    print("Margem Excelente! ")
elif margem>10 and margem<30:
    print("Margem Satisfatória! ")
else:
    print("Margem baixa! Avaliar preço de venda. ")