class Livro:

    def __init__(self):
        self.titulo = ""
        self.autor = ""
        self.anoPublicacao = 0
        self.numeroPaginas = 0
        self.genero = ""
        self.estado = "Fechado"
        self.PaginaAtual = 0

    def setTitulo (self , titulo):
        self.titulo = titulo 

    def getTitulo (self):

        return self.titulo

    def setAutor (self , autor):
        self.autor = autor

    def getAutor (self):

        return self.autor

    def setAnoPublicacao (self , anoPublicacao):
        self.anoPublicacao = anoPublicacao

    def getAnoPublicacao (self):

        return self.anoPublicacao

    def setNumeroPaginas (self , numeroPaginas):
        self.numeroPaginas = numeroPaginas

    def getNumeroPaginas (self):

        return self.numeroPaginas

    def setGenero (self , genero):
        self.genero = genero 

    def getGenero (self):

        return self.genero    
    
    def setEstado (self , estado):
        self.estado = estado

    def getEstado (self):

        return self.estado
    
    def setPaginaAtual (self , pagina ):
        self.PaginaAtual = pagina

    def getPaginaAtual (self):

        return self.PaginaAtual  



    def abrir (self):
        self.estado = "Aberto"

        return print("Livro Aberto")

    def fechar (self):
        self.estado = "Fechado"

        return print("Livro Fechado")

    def MarcarPagina (self , pagina):
       if self.estado == "Aberto": 
        if pagina <= self.numeroPaginas:
            self.PaginaAtual = pagina

    def AvancarPagina (self):
      if self.estado == "Aberto":
          if self.PaginaAtual < self.numeroPaginas:         
             self.PaginaAtual += 1

    def RetrocederPagina (self):
       if self.estado ==  "Aberto" :
          if self.PaginaAtual > 1:
             self.PaginaAtual -= 1          


livro = Livro()

livro.abrir()
livro.fechar()
livro.abrir()

livro.fechar()

livro.setNumeroPaginas(80)
livro.MarcarPagina(79)
print(livro.getPaginaAtual())

livro.AvancarPagina()
print(livro.getPaginaAtual())
livro.AvancarPagina()
print(livro.getPaginaAtual())

livro.abrir()

livro.MarcarPagina(2)
print(livro.getPaginaAtual())
livro.RetrocederPagina()
print(livro.getPaginaAtual())
livro.RetrocederPagina()
print(livro.getPaginaAtual())
livro.RetrocederPagina()
print(livro.getPaginaAtual())

livro.fechar()