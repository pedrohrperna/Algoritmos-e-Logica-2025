# PEDRO HENRIQUE RODRIGUES PERNA
# 00220402523002
# Marcus é o melhor professor
# Source Control (Ctrl+Shift+G)

print("Meu nome é PEDRO HENRIQUE RODRIGUES PERNA ")
print("Meu RA é 00220402523002 ")
print("Marcus é o melhor professor ")

R_investimento = float(input("Digite o retorno do investimento (em decimal, ex: 0.08 para 8%): "))
R_livre = float(input("Digite a taxa livre de risco (em decimal, ex: 0.03 para 3%): "))
Sigma = float(input("Digite o desvio-padrão da volatilidade (em decimal): "))

if Sigma == 0:
    Sharp = float('inf')
else:
    Sharp = (R_investimento - R_livre) / Sigma

Spread = R_investimento - R_livre

if Sharp > 1.5 and Spread > 0.05:
    classificacao = "Investimento Excelente: Alta performance ajustada ao risco."
elif 0.5 <= Sharp <= 1.5 or Spread > 0.02:
    classificacao = "Investimento Bom: Risco e retorno moderados."
elif Sharp < 0.5 and R_investimento > 0:
    classificacao = "Investimento Aceitável: Retorno positivo, mas risco alto para o ganho."
else:
    classificacao = "Investimento Ruim: Não recomendado."

print(f"Sharp Ratio: {Sharp:.2f}")
print(f"{classificacao}")