from produto import Produto

produtos = {
    "coca-cola": Produto("Coca-Cola", 7.00, 5),
    "salgadinho": Produto("Salgadinho", 5.50, 4),
    "chocolate": Produto("Chocolate", 6.50, 3),
}

def listar_produtos():
    print("\n📦 Produtos cadastrados:")
    for chave, p in produtos.items():
        print(f"- {chave} | qtd: {p.quantidade} | R$ {p.preco:.2f}")

def escolher_produto():
    listar_produtos()
    chave = input("\nDigite o nome do produto: ").lower()
    if chave not in produtos:
        print("❌ Produto não encontrado.")
        return None
    return produtos[chave]

while True:
    print('''\n===== MENU ESTOQUE =====
1 - Listar produtos
2 - Mostrar estoque
3 - Vender produto
4 - Repor estoque
0 - Sair
''')

    opcao = input("Escolha: ")

    if opcao == "1":
        listar_produtos()

    elif opcao == "2":
        produto = escolher_produto()
        if produto:
            produto.mostrar_estoque()

    elif opcao == "3":
        produto = escolher_produto()
        if produto:
            qtd = int(input("Quantidade para vender: "))
            produto.remover_estoque(qtd)

    elif opcao == "4":
        produto = escolher_produto()
        if produto:
            qtd = int(input("Quantidade para repor: "))
            produto.adicionar_estoque(qtd)

    elif opcao == "0":
        print("Saindo do sistema...")
        break

    else:
        print("❌ Opção inválida.")
