
class Joc:
    # atributele clasei => statice
    GOL = 
    NR_LINII = 0
    NR_COLOANE = 0        
    JMIN = 
    JMAX = 
    SIMBOLURI_JUC = 

    # reprezentam tabla de joc ca matrice (lista de liste) 
    def __init__(self, tabla=None):
        self.matr = tabla or [[Joc.GOL for j in Joc.NR_COLOANE] for i in Joc.NR_LINII]


    def final(self):
        # Returneaza fie simbolul jucatorului care a castigat jocul, fie „remiza”, fie False daca jocul nu s-a terminat inca.


    def mutari_joc(self, jucator):
        succesori = []
        # Returneaza toate configuratiile de joc valide ca succesori


    def estimeaza_scor(self, adancime):
        if self.final is not False: # configuratie finala
            # mai multe situatii
        else:
            # (sansele de castig pentru JMAX) – (sansele de castig pentru JMIN)


    def __str__(self):
        str = ""
        for i in range(NR_LINII):
            for j in range(NR_COLOANE):
                str += self.matr[i][j] + " "
            str += "\n"
        return str

class Stare:
    ADANCIME_MAX = 0

    def __init__(self, tabla_joc, j_curent, adancime, parinte=None, scor=None):
        self.tabla_joc = tabla_joc # un obiect de tip Joc => „tabla_joc.matr”
        self.j_curent = j_curent # simbolul jucatorului curent
        
        # adancimea in arborele de stari scade cu cate o unitate din „tata” in „fiu”
        self.adancime = adancime
        
        # scorul starii (daca e finala, adica frunza a arborelui)
        # sau scorul celei mai bune stari-fiice (pentru jucatorul curent)
        self.scor = scor
        
        # lista de mutari posibile din starea curenta
        self.mutari_posibile = [] # lista va contine obiecte de tip Stare
        
        # cea mai buna mutare din lista de mutari posibile pentru jucatorul curent
        self.stare_aleasa = None 


    def jucator_opus(self):
        if self.j_curent == Joc.JMIN:
            return JMAX
        return JMIN


    def mutari_stare(self):
        # toti fiii posibili ai nodului curent „self” in arborele de cautare
        stari = []
        return stari


    def __str__(self):
        str = "Configuratia curenta:\n"
        
        return str

