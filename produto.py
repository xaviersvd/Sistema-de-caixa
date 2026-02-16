class Produto:
      def __init__(self, nome, preco, quantidade):
            self.nome = nome
            self.preco = preco
            self.quantidade = quantidade
      def vender(self, qtd):
              pass
      def repor(self, qtd):
              pass
      def mostrar_estoque(self):
             print(f'''Produto: {self.nome}
preco: R${self.preco}
Unidades em estoque: {self.quantidade}''')
             
      def adicionar_estoque(self, qtd):
            self.quantidade + qtd
            print(f'{qtd} unidades adicionadas ao estoque')