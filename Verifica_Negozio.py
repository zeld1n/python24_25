#Senza l'uso di risorsa

class Articolo:
  def __init__(self, codice, fornitore, marca,prezzo, quantita):
    self.codice=codice
    self.fornitore=fornitore
    self.marca=marca
    self.prezzo=prezzo
    self.quantita=quantita

  def scheda_articolo(self):
    return str(f"\n\tCodice: {self.codice} \n\tFornitore: {self.fornitore} \n\tMarca: {self.marca} \n\tPrezzo: {self.prezzo} \n\tQuantità: {self.quantita}")
    #2 Ritorna una stringa contenente gli attributi dell'articolo
    

  def modifica_scheda(self):
    scelta=int(input("Modifica Scheda:\n"
            "1 - Codice\n"
            "2 - Fornitore\n"
            "3 - Marca\n"
            "4 - Prezzo\n"
            "5 - Quantità\n"
        "Cosa Desideri modificare?"))
    if scelta==1:
        self.codice=int(input("Inserisci codice: "))
    elif scelta==2:
      self.fornitore=(input("Inserisci fornitore: "))
    elif scelta==3:
      self.marca=(input("Inserisci la marca: "))
    elif scelta==4:
      self.prezzo=int(input("Inserisci prezzo: "))
    elif scelta==5:
      self.quantita=int(input("Inserisci quantità: "))
#09:22

class Televisore(Articolo):
    def __init__(self, codice, fornitore,marca,prezzo,quantita,pollici,tipo):
        super().__init__(codice, fornitore,marca,prezzo,quantita)
        self.pollici=pollici
        self.tipo=tipo
      

    def scheda_articolo(self):
        return(str(f"\nScheda televisore:{super().scheda_articolo()}\n\tPollici: {self.pollici} \n\tTipo: {self.tipo}\n"))
      
class Frigorifero(Articolo):
    def __init__(self, codice, fornitore,marca,prezzo,quantita,dimensioni,modello):
        super().__init__(codice, fornitore,marca,prezzo,quantita)
        self.dimensioni=dimensioni
        self.modello=modello
      

    def scheda_articolo(self):
        return(str(f"\nScheda frigorifero:{super().scheda_articolo()}\n\tDimensioni: {self.dimensioni} \n\tModello: {self.modello}\n"))
#09:39
class Ordine():
  def __init__(self,codice,data, piva,indirizzo):
    self.codice=codice
    self.data=data
    self.piva=piva
    self.indirizzo=indirizzo
    self.arrayArticoli=[]
    self.sommaT=0
    self.sommaF=0

  def aggiungi_articolo(self,articolo):
    if isinstance(articolo,Televisore):
      for i in self.arrayArticoli:
         if(i.codice==articolo.codice):
            print("L'articolo già presente nella lista")
            return
      self.arrayArticoli.append(articolo)

    elif isinstance(articolo,Frigorifero):
      for i in self.arrayArticoli:
         if(i.codice==articolo.codice):
            print("L'articolo già presente nella lista")
            return
      self.arrayArticoli.append(articolo)
    #9 Completa il metodo aggiungendo l'oggetto alla lista e stampando il messaggio opportuno

  def rimuovi_articolo(self,articolo):
    if isinstance(articolo,Televisore):
      for i in self.arrayArticoli:
         if(i==articolo):
            self.arrayArticoli.remove(i)
            return
      print("Prodotto non presente nella lista") 
    elif isinstance(articolo,Frigorifero):
        for i in self.arrayArticoli:
         if(i==articolo):
            self.arrayArticoli.remove(i)
            return
        print("Prodotto non presente nella lista") 

  def importo_ordine(self):
    for i in self.arrayArticoli:
      print(f"Importo articolo con codice:{i.codice} con l'importo:{i.quantita*i.prezzo}")


  def dettaglio_ordine(self):
    for i in self.arrayArticoli:
      if isinstance(i,Televisore):
        self.sommaT+=i.quantita*i.prezzo
     
    for i in self.arrayArticoli:
      if isinstance(i,Frigorifero):
        self.sommaF+=i.quantita*i.prezzo

    return([self.sommaT,self.sommaF,self.sommaT+self.sommaF])
#10:12
class Ordini():
  def __init__(self,nome_negozio,codice_negozio):
   self.nome_negozio=nome_negozio
   self.codice_negozio=codice_negozio
   self.listaOrdini=[]
   self.totT=0
   self.totF=0
   self.tot=0

   
  def aggiungi_ordine(self,ordine):
      for i in self.listaOrdini:
        if(i==ordine):
          print("Ordine già presente nella lista")
          return
      self.listaOrdini.append(ordine)

    
  def rimuovi_ordine(self,ordine):
    for i in self.listaOrdini:
      if(i==ordine):
        self.listaOrdini.remove(i)
        return
    print("Ordine non presente nella lista ")

  def totale_ordini(self):
    cont=0
    for i in self.listaOrdini:
        if isinstance(i,Ordine):
          cont+=1
          self.totT+=i.sommaT
          self.totF+=i.sommaF

      
    return ([self.totT,self.totF,self.totT+self.totF])





t1 = Televisore(1,"Fornitore 1","Sony",700,10,40,"Schermo piatto")
t1.modifica_scheda()
t2 = Televisore(2,"Fornitore 2","Samsung",1000,5,80,"Schermo curvo")
f1 = Frigorifero(3,"Fornitore 3","Bosch",750,12,'790x2000x600','Ultra')
f2 = Frigorifero(4,"Fornitore 4","Ariston",550,10,'590x1600x500','Medium')
print(t1.scheda_articolo())
print(t2.scheda_articolo())
print(f1.scheda_articolo())
print(t2.scheda_articolo())
print("--------------------------")
ordine1=Ordine(1,"24/02/2022",'213143','Via della consegna 1')
ordine1.aggiungi_articolo(t1)
ordine1.aggiungi_articolo(t2)
ordine1.aggiungi_articolo(f1)
ordine1.aggiungi_articolo(f2)
ordine1.aggiungi_articolo(f2)

ordine1.rimuovi_articolo(f2)
ordine1.rimuovi_articolo(f2)
print("--------------------------")
ordine1.importo_ordine()




print("--------------------------")
print("\n\n")
ordini_negozio=Ordini("Megastore vendita ",1)
ordini_negozio.aggiungi_ordine(ordine1)
ordini_negozio.rimuovi_ordine(ordine1)
ordini_negozio.rimuovi_ordine(ordine1)

ordini_negozio.aggiungi_ordine(ordine1)



importi=ordine1.dettaglio_ordine()

print(f"\nImporto televisori= {importi[0]}")
print(f"\nImporto frigoriferi= {importi[1]}")
print(f"\nImporto totale= {importi[2]}")
print("--------------------------")
t3 = Televisore(5,"Fornitore 5","LG",600,4,70,"Schermo curvo")
f3 = Frigorifero(6,"Fornitore 6","Bosch",450,10,'490x1000x400','Small')
ordine2=Ordine(2,"25/02/2022",'213113','Via della consegna 2')
ordine2.aggiungi_articolo(t3)
ordine2.aggiungi_articolo(f3)
print(t3.scheda_articolo())
print(f3.scheda_articolo())
ordine2.rimuovi_articolo(f3)

ordini_negozio.aggiungi_ordine(ordine2)


importi2=ordine2.dettaglio_ordine()

print(f"\nImporto televisori= {importi2[0]}")
print(f"\nImporto frigoriferi= {importi2[1]}")
print(f"\nImporto totale= {importi2[2]}")
print("--------------------------")

importiTotali=ordini_negozio.totale_ordini()
print(f"\nImporto totale televisori= {importiTotali[0]}")
print(f"\nImporto totale frigoriferi= {importiTotali[1]}")
print(f"\nImporto totale tutti gli ordini= {importiTotali[2]}")
print("--------------------------")