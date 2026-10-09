produtos = [["Caderno", 15.00, "Papelaria"], ["Arroz", 5.50, "Alimento"], ["Feijão", 7.00, "Alimento"]]

lista_categorias = []
for p in produtos:
    lista_categorias.append(p[2])

categorias_unicas = set(lista_categorias)

print("Categorias disponíveis no sistema:", categorias_unicas)