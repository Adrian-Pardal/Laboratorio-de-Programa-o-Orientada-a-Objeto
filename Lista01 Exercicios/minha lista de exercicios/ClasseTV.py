class Tv:

    def __init__(self):
        self.canal = 0
        self.volume = 0
        self.estado = "desligado"


    def setCanal (self , canal):
        self.canal = canal

    def getCanal (self):

        return self.canal

    def setVolume (self , quantidade):

        self.volume = quantidade        

    def getVolume (self):

        return self.volume

    def setEstado (self , estado):

        self.estado = estado

    def getEstado (self):

        return self.estado    
    
    
    
    
    
    
    
    
    #   METODOS    #
    def ligar (self):

        self.estado = "ligado"

    def desligar (self):

        self.estado = "desligado"

    
    def aumentarVolume (self , quantidade):#
      if self.estado == "ligado":   
        self.aumentar = quantidade
        if self.volume < 100 :
            if quantidade <= 100 :
                if quantidade <= 0:
                    self.volume = self.volume

                if self.aumentar >= 0 :    
                    self.volume += quantidade

    def diminuirVolume (self , quantidade):
      if self.estado == "ligado":  
        self.diminuir = quantidade
        if self.volume <= 100:
            if self.diminuir <= 0 :
           
                self.volume = self.Volume

            if  self.diminuir >=  0 :
             
                self.volume -= quantidade

tv = Tv()

tv.ligar()
tv.aumentarVolume(15)

print(tv.getVolume())

tv.diminuirVolume(15)

print(tv.getVolume())
tv.aumentarVolume(50)
tv.aumentarVolume(50)

tv.aumentarVolume(1)

tv.diminuirVolume(50)
print(tv.getVolume())
