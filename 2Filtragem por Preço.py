produtos = [["Arroz", 5.50, "Alimento"], ["Feijão", 7.00, "Alimento"], ["Caderno", 15.00, "Papelaria"]]

print("\n=== Filtro de Preços ===")
valor = float(input("Digite o valor de referência: R$ "))
condicao = input("Deseja ver produtos (1) Acima ou (2) Abaixo deste valor? (Digite 1 ou 2): ")

print("\n--- Resultados ---")
for p in produtos:
    if condicao == '1' and p[1] > valor:
        print(f"{p[0]} - R$ {p[1]:.2f}")
    elif condicao == '2' and p[1] < valor:
        print(f"{p[0]} - R$ {p[1]:.2f}")