import random

class robot:
    name = "machine3"
    game = [["-","-","-"],["-","-","-"],["-","-","-"]]
    
    def playing(self):
        fila = random.choice([0,1,2])
        columna = random.choice([0,1,2])
        resultat = self.game[fila][columna]
        
        if resultat == "-":
            self.game[fila][columna] = "x"  
            return (fila, columna)  
        else:
            return self.playing()  
    
    def mostrar_tauler(self):
        for fila in self.game:
            print(" ".join(fila))
            print("------")