class Produto:

    def __init__(self):

        self.nome = ""
        self.preco = 0.0
        self.quantidadeEstoque = 0
        self.categoria = ""


    def setNome(self , nome ):
        self.nome = nome

    def getNome(self):

        return self.nome

    def setPreco (self , preco):
        self.preco = preco   

    def getPreco(self):

        return self.preco


    def setQuantidadeEstoque(self , quantidadeEstoque):
        self.quantidadeEstoque = quantidadeEstoque

    def getQuantidadeEstoque(self):

        return self.quantidadeEstoque

    def setCategoria (self , categoria):

        self.categoria = categoria

    def getCategoria (self):

        return self.categoria



    def adionarEstoque(self , quantidade):
        self.quantidadeEstoque += quantidade  


    def removerEstoque(self , quantidade):
       if quantidade <= self.quantidadeEstoque: 
        self.quantidadeEstoque -= quantidade  

    def aplicarDesconto(self , percentual):
        if percentual >= 0 and percentual <= 100:  
            self.preco = self.preco * ((100 - percentual) / 100) 

produto = Produto()

produto.setPreco(50)
produto.aplicarDesconto(10)

print(produto.getPreco())