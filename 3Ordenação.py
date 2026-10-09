produtos = [["Caderno", 15.00, "Papelaria"], ["Arroz", 5.50, "Alimento"], ["Feijão", 7.00, "Alimento"]]

produtos.sort(key=lambda x: x[1])
print("Lista Crescente:")
for p in produtos:
    print(f"{p[0]} - R$ {p[1]:.2f}")

produtos_decrescentes = sorted(produtos, key=lambda x: x[1], reverse=True)
print("\nLista Decrescente:")
for p in produtos_decrescentes:
    print(f"{p[0]} - R$ {p[1]:.2f}")