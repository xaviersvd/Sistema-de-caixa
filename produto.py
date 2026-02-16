class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def mostrar_estoque(self):
        print(f'''
Produto: {self.nome}
Preço: R$ {self.preco:.2f}
Unidades em estoque: {self.quantidade}
''')

    def adicionar_estoque(self, qtd):
        if qtd <= 0:
            print("❌ Quantidade inválida.")
            return
        self.quantidade += qtd
        print(f'{qtd} unidades adicionadas ao estoque.')

    def remover_estoque(self, qtd):
        if qtd <= 0:
            print("❌ Quantidade inválida.")
            return

        if qtd > self.quantidade:
            print('❌ Erro: Estoque insuficiente!')
            return

        self.quantidade -= qtd
        print(f'{qtd} unidades removidas do estoque.')

        if self.quantidade <= 5:
            print('⚠️ Aviso: estoque baixo!')
