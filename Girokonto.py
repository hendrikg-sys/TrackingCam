class Konto:
    def __init__(self, inhaber, kontonummer, kontostand, max_tagesumsatz=1500):
        self.Inhaber = inhaber
        self.Kontonummer = kontonummer
        self.Kontostand = kontostand
        self.MaxTagesumsatz = max_tagesumsatz
        self.UmsatzHeute = 0

    def geldtransfer(self, ziel, betrag):
        if (
            betrag < 0
            or self.UmsatzHeute + betrag > self.MaxTagesumsatz > self.MaxTagesumsatz
            or ziel.UmsatzHeute + betrag > ziel.MaxTagesumsatz
        ):
            return False

        else:
            self.Kontostand -= betrag
            self.UmsatzHeute += betrag
            ziel.Kontostand += betrag
            ziel.UmsatzHeute += betrag
            return True

    def einzahlen(self, betrag):
        if betrag < 0 or self.UmsatzHeute + betrag > self.MaxTagesumsatz:

            return False
        else:
            self.Kontostand += betrag
            self.UmsatzHeute += betrag
            return True

    def auszahlen(self, betrag):
        if betrag < 0 or self.UmsatzHeute + betrag > self.MaxTagesumsatz:
            return False
        else:
            self.Kontostand -= betrag
            self.UmsatzHeute += betrag
            return True

    def zeige(self):
        print("Konto von {}".format(self.Inhaber))
        print("Aktueller Kontostand: {:.2f} Euro".format(self.Kontostand))
        print(
            "Heute schon {:.2f} von {} umgesetzt".format(
                self.UmsatzHeute, self.MaxTagesumsatz
            )
        )


class VerwalteterGeldbetrag:
    def __init__(self, anfangsbetrag):
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
        else:
            self.Betrag += betrag
            return True

    def zeige(self):
        print("Betrag: {:.2f}".format(self.Betrag))


# k1 = Konto("Hendrik", 5034354, 50000, 1500)
