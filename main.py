from produto import Produto
import json

ARQUIVO = "estoque.json"


def salvar_produtos(produtos: dict):
    dados = {}
    for chave, p in produtos.items():
        dados[chave] = {
            "nome": p.nome,
            "preco": p.preco,
            "quantidade": p.quantidade
        }

    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)


def carregar_produtos() -> dict:
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            dados = json.load(f)

        produtos = {}
        for chave, info in dados.items():
            produtos[chave] = Produto(info["nome"], info["preco"], info["quantidade"])
        return produtos

    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "coca-cola": Produto("Coca-Cola", 7.00, 5),
            "salgadinho": Produto("Salgadinho", 5.50, 4),
            "chocolate": Produto("Chocolate", 6.50, 3),
        }



def listar_produtos(produtos):
    print("\n📦 Produtos cadastrados:")
    for chave, p in produtos.items():
        print(f"- {chave} | qtd: {p.quantidade} | R$ {p.preco:.2f}")


def escolher_produto(produtos):
    listar_produtos(produtos)
    chave = input("\nDigite o nome do produto: ").strip().lower()

    if chave not in produtos:
        print("❌ Produto não encontrado.")
        return None

    # retorna (produto, chave) pra bater com: produto, _ = res
    return produtos[chave], chave


# carrega antes do menu
produtos = carregar_produtos()

while True:
    print('''\n===== MENU ESTOQUE =====
1 - Listar produtos
2 - Mostrar estoque
3 - Vender produto
4 - Repor estoque
5 - Cadastrar novo produto
0 - Sair
''')


    opcao = input("Escolha: ").strip()

    if opcao == "1":
        listar_produtos(produtos)

    elif opcao == "2":
        res = escolher_produto(produtos)
        if res:
            produto, _ = res
            produto.mostrar_estoque()

    elif opcao == "3":
        res = escolher_produto(produtos)
        if res:
            produto, _ = res
            try:
                qtd = int(input("Quantidade para vender: "))
                antes = produto.quantidade
                produto.remover_estoque(qtd)
                if produto.quantidade != antes:
                    salvar_produtos(produtos)
            except ValueError:
                print("❌ Digite um número inteiro válido.")

    elif opcao == "4":
        res = escolher_produto(produtos)
        if res:
            produto, _ = res
            try:
                qtd = int(input("Quantidade para repor: "))
                antes = produto.quantidade
                produto.adicionar_estoque(qtd)
                if produto.quantidade != antes:
                    salvar_produtos(produtos)
            except ValueError:
                print("❌ Digite um número inteiro válido.")

    elif opcao == "5":
        nome = input("Nome do novo produto: ").strip()
        chave = nome.lower()

        if chave in produtos:
            print("❌ Produto já existe no estoque.")
        else:
            try:
                preco = float(input("Preço do produto: R$ "))
                quantidade = int(input("Quantidade inicial: "))

                produtos[chave] = Produto(nome, preco, quantidade)
                salvar_produtos(produtos)

                print(f"✅ Produto '{nome}' cadastrado com sucesso!")

            except ValueError:
                print("❌ Erro: Digite valores numéricos válidos.")


    elif opcao == "0":
        salvar_produtos(produtos)
        print("👋 Saindo... (estoque salvo)")
        break

    else:
        print("❌ Opção inválida.")
