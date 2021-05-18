
class VerwalteterGeldbetrag:
    def __init__(self, anfangsbetrag) -> None:
        self.Betrag = anfangsbetrag
    def einzahlenMoeglich(self, betrag):
        return True
    def auszahlenMoeglich(self, betrag):
        return True
    def einzahlen(self, betrag):
        if betrag < 0 or not self.einzahlenMoeglich(betrag):
            return False
        else:
            self.Betrag += betrag
            return True

    def auszahlen(self, betrag):
        if betrag < 0 or not self.auszahlenMoeglich(betrag):
            return False

    def zeige(self):
        print("Betrag: {:.2f}".format(self.Betrag))

class AllgemeinesKonto(VerwalteterGeldbetrag):
    def __init__(self, kundendaten, konotostand) -> None:
        super().__init__(konotostand)
        self.Kundendaten = kundendaten
    
    def geldtransfer(self, ziel, betrag):
        if self.auszahlenMoeglich(betrag) and ziel.einzahlenMoeglich(betrag):
            self.auszahlen(betrag)
            ziel.einzahlen(betrag)
            return True
        else:
            return False
    def zeige(self):
        self.Kundendaten.zeige()
        VerwalteterGeldbetrag.zeige(self)

class AllmeinesKontoMitTagesumsatz(AllgemeinesKonto):
    def __init__(self, kundendaten, konotostand, max_tagesumsatz=1500) -> None:
        super().__init__(kundendaten, konotostand)
        self.MaxTagesumsatz = max_tagesumsatz
        self.UmsatzHeute = 0,0
    def transferMoeglich(self, betrag):
        return (self.UmsatzHeute + betrag <=self.MaxTagesumsatz)

    def auszahlenMoeglich(self, betrag):
        return self.transferMoeglich(betrag)

    def einzahlenMoeglich(self, betrag):
        return self.transferMoeglich()
    def einzahlen(self, betrag):
        if AllgemeinesKonto.einzahlen(self, betrag):
            self.UmsatzHeute += betrag
            return True
        else:
            return False
    def auszahlen(self, betrag):
        if AllgemeinesKonto.auszahlen(self, betrag):
            self.UmsatzHeute += betrag
            return True
        else:
            return False

    def zeige(self):
        AllgemeinesKonto.zeige(self)
        print("Heute schon {:.2f} von {:.2f} Euro umgesetzt".format(self.UmsatzHeute, self.MaxTagesumsatz))

class GiroKontoKundendaten:
    def __init__(self, inhaber, kontonummer) -> None:
        self.Inhaber = inhaber
        self.Kontonummer = kontonummer
    def zeige(self):
        print("Inhaber:", self.Inhaber)
        print("Kontonummer:", self.Kontonummer)

class GiroKontoMitTagesumsatz(AllmeinesKontoMitTagesumsatz):
    def __init__(self, inhaber, kontonummer, kontostand, max_tagesumsatz=1500) -> None:
        kundendaten = GiroKontoKundendaten(inhaber, kontonummer)
        super().__init__(kundendaten, kontostand, max_tagesumsatz=max_tagesumsatz)
    
class VerwalteterBargeldbetrag(VerwalteterGeldbetrag):
    def __init__(self, bargeldbetrag) -> None:
        if bargeldbetrag < 0:
            bargeldbetrag = 0      
        super().__init__(bargeldbetrag)

    def auszahlenMoeglich(self, betrag):
        return (self.Betrag >= betrag)

class Geldboerse(VerwalteterBargeldbetrag):
    # TODO: Spezielle Methoden fuer eine Geldboerse
    pass

class Tresor(VerwalteterBargeldbetrag):
    # TODO: Spezielle Methoden fuer eine Tresor
    pass

