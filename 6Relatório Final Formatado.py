produtos = [["Caderno", 15.00, "Papelaria"], ["Arroz", 5.50, "Alimento"], ["Feijão", 7.00, "Alimento"]]

precos = [p[1] for p in produtos] # Jeito rápido (List Comprehension) de pegar os preços
estatisticas = (min(precos), max(precos), sum(precos) / len(precos))
categorias = set([p[2] for p in produtos])

print("=" * 40)
print(f"{'RELATÓRIO DE PRODUTOS':^40}")
print("=" * 40)

print(f"Total de produtos cadastrados : {len(produtos)}")
print(f"Categorias únicas ({len(categorias)})        : {', '.join(categorias)}")
print("-" * 40)
print(f"Produto mais barato           : R$ {estatisticas[0]:.2f}")
print(f"Produto mais caro             : R$ {estatisticas[1]:.2f}")
print(f"Média geral de preços         : R$ {estatisticas[2]:.2f}")
print("-" * 40)

print("Listagem de Produtos (Ordem de Entrada):")
for p in produtos:
    print(f" -> {p[0]:<10} | {p[2]:<10} | R$ {p[1]:.2f}")
print("=" * 40)