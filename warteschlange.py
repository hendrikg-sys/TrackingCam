# %%

class Warteschlange(object):
    def __init__(self, anzahl_plaetze):
        
        self.liste = []
    
        self.anzahl = 0

        self.anzahl_plaetze = anzahl_plaetze
    
    
    def ankommen(self, objekt):

        if self.anzahl == self.anzahl_plaetze:

            print("abgewiesen")

        else:
        
            self.liste.append(objekt)
        
            self.anzahl = self.anzahl+1

    
    def verlassen(self):
        
        if self.anzahl > 0 :

            
            objekt = self.liste.pop(0) 
        
            self.anzahl = self.anzahl-1
        
            return objekt
        
        else:
            
            return None
            
    def ausgabe(self):

       
        return self.liste



# %%

ws1 = Warteschlange(2)

ws1.ankommen("test")

ws1.ankommen("test")

ws1.ankommen("test")

ws1.ausgabe()

# %%
