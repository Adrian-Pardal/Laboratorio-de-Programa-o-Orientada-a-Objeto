class Pessoa:
    def __init__(self , nome ):
        self.nome = nome

    def setNome(self , nome ):
        self.nome = nome 
    def getNome(self):
        return self.nome
    
class Cliente(Pessoa):
    def __init__(self  , nome , cpf):
        Pessoa.__init__(self , nome)
        self.cpf = cpf

    def setCPF(self , cpf):
        self.cpf = cpf

    def getCPF(self):
        return self.cpf

class Fornecedor(Pessoa):
    def __init__(self , nome , cnpj):
        self.cnpj = cnpj
        Pessoa.__init__(self , nome)
    
    def setCNPJ(self , cnpj):
        self.cnpj = cnpj

    def getCNPJ(self):
        return self.cnpj
    
class Transacao():
    def __init__(self , dataTrasacao , produto , qtde):
        self.dataTransacao = dataTrasacao
        self.qtde = qtde
        
    def setDataTransacao(self , data):
        self.dataTransacao = data
    
    def getDataTransacao(self):
        return self.dataTransacao
    
    def setQtde(self , quantidade):
        self.qtde = quantidade

    def getQtde(self):
        return self.qtde
    
    def setNome(self , nome):
        self.nome = nome

    def getNome(self):
        return self.nome

class Venda(Transacao):
    
    def setCliente(self , cliente):
        self.cliente = cliente

    def getCliente(self):
        return self.cliente
    
    # METODOS #
    def __init__(self , dataVenda , cliente , produto , qtdeVendida):
        Transacao.__init__(self , dataVenda , produto , qtdeVendida)
        self.cliente = cliente
        
    def vender(self , produto ,qtdeVendida):
        if produto.verificarEstoqueInsufiente(qtdeVendida):
            print("Estoque insuficiente")
            return False
        else : 
            produto.debitarEstoque(qtdeVendida)
            print(qtdeVendida * produto.getPrecoUnit())
            if produto.verificarEstoqueBaixo():
                print("Estoque baixo")
            return True

class Compra(Transacao):

    def __init__(self , dataCompra , produto , fornecedor , qtdeCompra ):
        Transacao.__init__(self , dataCompra , produto , qtdeCompra)
        self.fornecedor = fornecedor
        
    
    def setPrecoUnit(self , precoUnit):
        self.precoUnit = precoUnit
    
    def getPrecoUnit(self):
        return self.precoUnit

    def setFornecedor(self , fornecedor):
        self.fornecedor = fornecedor
    
    def getFornecedor(self):
        return self.fornecedor

    # Metodos #

    def comprar(self , produto , qtdeCompra):
        if produto.verificarEstoqueExcedente(qtdeCompra):
            print("Estoque Exedente")
            return False
        else :
            produto.registrarHistorico(compra)
            produto.creditarEstoque(qtdeCompra)
            return True
        
class Produto():

    def __init__(self , nome , qtdeEstoque , precoUnit , estoqueMinimo , estoqueMaximo):
        self.nome = nome
        self.qtdeEstoque = qtdeEstoque
        self.precoUnit = precoUnit
        self.estoqueMinimo = estoqueMinimo
        self.estoqueMaximo = estoqueMaximo
        self.historico = []

    def setNome(self , nome ):
        self.nome = nome
    
    def getNome (self ):
        return self.nome
    
    def setQtdeEstoque (self , quantidade):
        self.qtdeEstoque = quantidade

    def getQtdeEstoque(self):
        return self.qtdeEstoque

    def setPrecoUnit(self , preco):
        self.precoUnit = preco

    def getPrecoUnit(self):
        return self.precoUnit

    def setEstoqueMininmo(self , minimo):
        self.estoqueMinimo = minimo

    def getEstoqueMinimo(self):
        return self.estoqueMinimo
    
    
    def setEstoqueMaximo(self  , maximo):
        self.estoqueMaximo = maximo

    def getEstoqueMaximo(self):
        return self.estoqueMaximo

    def setHistorico(self , historico):
        self.historico = historico

    def getHistorico(self):
        return self.historico

    # METODOS #
    # Letra A
    def debitarEstoque(self , quantidade):
        self.qtdeEstoque -= quantidade
    # Letra B
    def creditarEstoque(self , quantidade ):
        self.qtdeEstoque += quantidade
    # Letra C
    def verificarEstoqueBaixo(self):
            return self.qtdeEstoque < self.estoqueMinimo
    # Letra D 
    def verificarEstoqueInsufiente(self , quantidade):
            return   quantidade > self.qtdeEstoque
    # Letra E 
    def verificarEstoqueExcedente(self , quantidade):
        return self.qtdeEstoque + quantidade > self.estoqueMaximo
    
    def calcularValorVenda(self , quantidade):
        preco = self.precoUnit * quantidade
        return preco

    def registrarHistorico(self , transacao):
        self.historico.append(transacao)

    def exibirHistorico(self):
        for transacao in self.historico:
            print(f'{transacao.dataTransacao} , {self.getNome()} , {transacao.qtde}')
    

produto = Produto("caneta" , 100 , 2.0 , 50 , 200)
cliente = Cliente("Adrian" , 123) 
venda = Venda("08/06/2024" , cliente , produto , 60)
venda.vender(produto , 60)

produto1 = Produto("lapis" , 20 , 2.0 , 50 , 200)
fornecedor = Fornecedor("Jorge" , 458)
compra = Compra("08/06/2024" , fornecedor , produto1 , 150)
compra.comprar(produto1 , 150)
produto.registrarHistorico(venda)
produto.exibirHistorico()
produto1.registrarHistorico(compra)
produto1.exibirHistorico()













