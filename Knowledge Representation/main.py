

class Elev:
    contor = 0
    activitate_curenta = None
    timp_executat_activ = 0

    def __init__(self, nume=None, sanatate=90, inteligenta=20, oboseala=0, buna_dispozitie=100):
        self.nume = nume
        self.sanatate = sanatate
        self.inteligenta = inteligenta
        self.oboseala = oboseala
        self.buna_dispozitie = buna_dispozitie

        if self.nume is None:
            self.contor += 1
            self.nume = "Necunoscut_" + str(self.contor)


    def afis(self):
        print(self.nume)
        print(self.sanatate)
        print(self.inteligenta)
        print(self.oboseala)
        print(self.buna_dispozitie)


    def desfasoara_activitate(self, activitate):
        activitate_curenta = activitate
        timp_executat_activ = 0


    def trece_ora(self, ora):
        self.timp_executat_activ += ora
        factor_inteligenta = self.activitate_curenta.factor_inteligenta
        durata = self.activitate_curenta.durata
        factor_oboseala = self.activitate_curenta.factor_oboseala
        factor_dispozitie = self.activitate_curenta.factor_dispozitie
        factor_sanatate = self.activitate_curenta.factor_sanatate

        if self.oboseala == 100:
            self.inteligenta += factor_inteligenta / durata / 2
            self.oboseala += factor_oboseala / durata / 2
            self.buna_dispozitie += factor_dispozitie / durata / 2
            self.sanatate += factor_sanatate / durata / 2
        else:
            if ora >= 22 and ora <= 6:
                self.sanatate -= 1
            else:
                self.sanatate += factor_inteligenta / durata

            self.inteligenta += factor_inteligenta / durata
            self.oboseala += factor_oboseala / durata
            self.buna_dispozitie += factor_dispozitie / durata

            if self.sanatate == 0 or self.buna_dispozitie == 0:
                return False
            if self.inteligenta == 100:
                print("Felicitari pentru nivelul maxim de inteligenta!")

        if durata - self.timp_executat_activ == 0:
            return True
        return False


    def testeaza_final(self):
        if self.activitate_curenta.durata - self.timp_executat_activ == 0:
            return True
        return False


    def afiseaza_raport(self):
        sir = self.activitate_curenta.nume + ": " + str(self.activitate_curenta.durata)
        return(sir)


    def __repr__(self):
        sir = "Se afiseaza:\n"
        for (k, v) in self.__dict__.items():
            sir += "{} = {}\n".format(k, v)
        return (sir)



class Activitate:
    def __init__(self, nume, factor_sanatate, factor_inteligenta, factor_oboseala, factor_dispozitie, durata):
        self.nume = nume
        self.factor_sanatate = factor_sanatate
        self.factor_inteligenta = factor_inteligenta
        self.factor_oboseala = factor_oboseala
        self.factor_dispozitie = factor_dispozitie
        self.durata = durata

    def __repr__(self):
        sir = "Activitate:\n"
        for (k, v) in self.__dict__.items():
            sir += "{} = {}\n".format(k, v)
        return (sir)


def porneste_simulare(elev, activitate):
    elev.activitate_curenta = activitate
    ora = 9
    comanda = input("comanda =")
    if comanda == "gata":
        print("Gata")
        return 0
    elif comanda == "continua":
        print("Raport: " + elev.afiseaza_raport())
    else:
        for i in range(0, int(comanda)):
            ora = ora + 1
            if ora > 24:
                ora = 1
            print("Ora " + str(ora))
            elev.trece_ora(ora)
            if elev.testeaza_final() == False:
                    print(repr(elev))
            print()


if __name__ == "__main__":
    f = open("fisier.txt", "r")
    citire_activitati = f.readlines()
    # print(activitati)

    elev1 = Elev("Elevul1")
    # print(repr(elev1))
    elev2 = Elev("Elevul2", 95, 80, 30, 90)
    elev3 = Elev("Elevul3", 5, 70, 50, 60)
    elev4 = Elev("Elevul4", 90, 70, 98, 80)
    elev5 = Elev("Elevul5", 85, 98, 70, 75)

    elevi = []
    elevi.append(elev1)
    elevi.append(elev2)
    elevi.append(elev3)
    elevi.append(elev4)
    elevi.append(elev5)

    activitati = []
    for i in range(1, len(citire_activitati)):
        linie = citire_activitati[i].split(" ")
        a = Activitate(linie[0], int(linie[1]),int(linie[2]),int(linie[3]), int(linie[4]), int(linie[5].strip()))
        activitati.append(a)
        # print(a)

    for activitate in activitati:
        porneste_simulare(elev1, activitate)
