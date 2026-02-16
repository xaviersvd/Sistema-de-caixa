class Produto:
      def __init__(self, nome, preco, quantidade):
            self.nome = nome
            self.preco = preco
            self.quantidade = quantidade
      def vender(self, qtd):
            self.remover_estoque(qtd)
      def repor(self, qtd):
            self.adicionar_estoque(qtd)
      def mostrar_estoque(self):
                  print(f'''Produto: {self.nome}
preco: R${self.preco}
Unidades em estoque: {self.quantidade}''')

             
      def adicionar_estoque(self, qtd):
            self.quantidade += qtd
            print(f'{qtd} unidades adicionadas ao estoque')
      def remover_estoque(self, qtd):
            if qtd > self.quantidade:
                  print('❌ Erro: Estoque Insuficiente!!')
            else:
                  self.quantidade -= qtd
                  print(f'{qtd} Unidades removidas do estoque.')
            if self.quantidade <= 5:
                  print('⚠️  Aviso estoque baixo!')

p1 = Produto('Coca-Cola', 7.00, 5)
p2 = Produto('Salgadinho', 5.50, 4)
p3 = Produto('Chocolate', 6.50, 3)

p2.vender(1)
p2.mostrar_estoque()

p3.vender(2)
p3.mostrar_estoque()

p3.repor(5)
p3.mostrar_estoque()

