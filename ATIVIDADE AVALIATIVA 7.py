pureza = float(input("Digite a pureza do lote (ex: 0.95 para 95%): "))
massa_total = float(input("Digite a massa total (em kg): "))
taxa_contaminacao = float(input("Digite a taxa de contaminação (ex: 0.02 para 2%): "))

FD = (pureza * 100) - (taxa_contaminacao * 50)

if massa_total > 1000:
    P_base = 10.00
else:
    P_base = 12.50

if FD > 90 and pureza > 0.98:
    print("Classificação: PREMIUM (Venda Imediata)")
    P_final_kg = P_base * 1.50
elif 70 <= FD <= 90 and taxa_contaminacao < 0.05:
    print("Classificação: PADRÃO (Venda Normal)")
    P_final_kg = P_base * 1.10
elif FD < 70 or pureza < 0.90:
    print("Classificação: REPROVADO (Descarte ou Re-processamento)")
    P_final_kg = P_base * 0.25
else:
    print("Classificação: ACEITÁVEL (Margem Mínima)")
    P_final_kg = P_base * 0.90

Preco_Total_Final = P_final_kg * massa_total

print(f"Preço Base por kg: R$ {P_base:.2f}")
print(f"Preço Final Total do lote: R$ {Preco_Total_Final:.2f}")