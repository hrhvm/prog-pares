import time
class JuegoPar():
    puntaje=0
    limite=500
    def incrementar(self):
        
        self.puntaje=self.puntaje+1
        if self.puntaje > 500:
            self.puntaje=0
        return ' El Resultado es {}'.format( self.puntaje)
    

juego = JuegoPar()

for i in range(juego.limite):
    print(juego.incrementar())
    