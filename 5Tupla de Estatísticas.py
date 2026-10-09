produtos = [["Caderno", 15.00, "Papelaria"], ["Arroz", 5.50, "Alimento"], ["Feijão", 7.00, "Alimento"]]

precos = []
for p in produtos:
    precos.append(p[1])

menor = min(precos)
maior = max(precos)
media = sum(precos) / len(precos)

estatisticas = (menor, maior, media)

print(f"Menor Preço: R$ {estatisticas[0]}")
print(f"Maior Preço: R$ {estatisticas[1]}")
print(f"Média de Preços: R$ {estatisticas[2]:.2f}")