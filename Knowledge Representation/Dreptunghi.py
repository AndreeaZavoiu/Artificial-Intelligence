class Dreptunghi:
    """O clasa care memoreaza un dreptunghi format din caractere"""
    #atribute de clasa (statice)
    liniiSeparatoare=True
    simbolSeparator="-"
    dimLinieSeparatoare=15
    
    
    def __init__(self, inaltime, latime, simbolContinut, simbolContur=None):
        #atribute de instanta
        self.inaltime = inaltime
        self.latime = latime
        self.simbolContinut = simbolContinut
        self.simbolContur = "#" if simbolContur is None else simbolContur
        
    def arie(self):
        return self.inaltime*self.latime
    
    @classmethod
    def afisSimbolContur(cls):
        print('Simbol separator: '+ cls.simbolSeparator)

    @classmethod
    def afisNumeClasa(cls):
        print('Nume clasa:\n'+ cls.__name__)

    
    @classmethod
    def afisDoc(cls):
        print('Informatii clasa:\n'+ cls.__doc__)
        
        

        
        
    @staticmethod
    def afisLinie(n,simbol):
        print(n*simbol)

        
    #operatori
    
    def __eq__(self, dr):
        return (self.inaltime==dr.inaltime and self.latime==dr.latime)
    
    #observati ca nu trebuie sa ne raportam la aceleasi criterii, chiar daca in general nu este indicat
    def __lt__(self, dr):
        return self.arie()<dr.arie()
        

    def __lte__(self, dr):
        return self.arie()<=dr.arie()
        
    def __gt__(self, dr):
        return self.arie()>dr.arie()        
        
        
        
        
        
    #definesc ce va returna repr(obiect)
    def __repr__(self):
        # sir="Prop clasa:\n"
        # for (k,v) in self.__class__.__dict__.items() :
        #     sir+="{} = {}\n".format(k,v)

        sir="Prop instanta:\n"
        for (k,v) in self.__dict__.items() :
            sir+="{} = {}\n".format(k,v)
        return(sir)
        
    #definesc ce va returna str(obiect)    
    def __str__(self):
        sir=self.simbolContur*self.latime+"\n";
        for i in range(self.inaltime-2):
            sir+=self.simbolContur+self.simbolContinut*(self.latime-2)+self.simbolContur+"\n"
        sir+=self.simbolContur*self.latime+"\n"
        return(sir)
        
    def afis(self):
        if (self.liniiSeparatoare):
            self.afisLinie(self.dimLinieSeparatoare,self.simbolSeparator)
        print(d)
        if (self.liniiSeparatoare):
            self.afisLinie(self.dimLinieSeparatoare,self.simbolSeparator)




if __name__=="__main__":
    d1=Dreptunghi(5,10,'.')
    print("Am creat dreptunghiul d1=Dreptunghi(5,10,'.')")
    ##########################################
    print("Ce afiseaza print(d1)")
    print(d1)
    ##########################################
    print("Ce afiseaza print(str(d1))")
    print(str(d1))
    ##########################################
    print("Ce afiseaza print(repr(d1))")
    print(repr(d1))
    ##########################################
    d2=Dreptunghi(4,4,'.')
    ##########################################
    Dreptunghi.afisSimbolContur()
    Dreptunghi.afisNumeClasa()
    Dreptunghi.afisDoc()

