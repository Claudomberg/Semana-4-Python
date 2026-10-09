produtos = []

print("=== Cadastro de Produtos ===")
while True:
    nome = input("Digite o nome do produto (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
        
    preco = float(input(f"Digite o preço de {nome}: R$ "))
    categoria = input(f"Digite a categoria de {nome}: ")
    
    produtos.append([nome, preco, categoria])

print("\nProdutos cadastrados:", produtos)