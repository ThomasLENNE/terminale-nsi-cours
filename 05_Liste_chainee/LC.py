#listes chaînées bilan

class Cell:
    '''Cellule d'une liste chainee'''
    def __init__(self,valeur,suivant=None):
        self.valeur=valeur
        self.suivant=suivant

    def __str__(self):
        return str(self.valeur)

class Lc:
    '''Liste chaînée'''
    def __init__(self, tete=None):
        '''tete : lien vers la premiere cellule'''
        self.tete=tete
    
    def __str__(self):
        '''renvoie une forme lisible de Lc'''
        if self.tete is None:
            return '[]'
        else:
            cellule=self.tete
            valeurs=[cellule.valeur]
            while cellule.suivant is not None:
                cellule=cellule.suivant
                valeurs.append(cellule.valeur)

            return str(valeurs)
    
    
    def vide(self):
        '''renvoie True si la liste est vide
        False sinon'''
        return self.tete is None
    
    
    def __len__(self):
        '''renvoie la longueur de la liste'''
        n=0
        cellule=self.tete
        while cellule is not None:
            n=n+1
            cellule=cellule.suivant
        return n
    
    
    def __getitem__(self, index):
        '''renvoie l'élement  d'index donné,
           numéroté à partir de 0'''
        cellule=self.tete
        i = 0
        while i < index and cellule is not None:
            cellule=cellule.suivant
            i=i+1
        
        if cellule is None or index<0:
            return 'index error'
        
        return cellule.valeur
    
    
    def inserer(self,x,index):
        '''insere l'élément x dans la liste
        à l'index donné, numéroté à partir de 0'''
        i=0
        cellule=self.tete
        if cellule is None:
            self.tete=Cell(x,None)
            
        elif index == 0:
            self.tete=Cell(x,cellule)
        
        else :
            while i < index-1 :
                cellule=cellule.suivant
                i=i+1
            
            nouv_cellule=Cell(x,cellule.suivant)
            cellule.suivant=nouv_cellule
            
    
    def supprimer(self,index):
        ''' Supprime l'élément d'index donné
        numéroté  partir de 0, de la liste'''
        i=0
        cellule=self.tete

        if index==0:
            self.tete=cellule.suivant
        else:
            
            while i < index-1:
                cellule=cellule.suivant
                i=i+1
            cellule.suivant=cellule.suivant.suivant
        
    
    def last(self):
        '''renvoie la derniere cellule
        de la chaîne'''
        if self.tete is None:
            return None
       
        else:
            cellule=self.tete
            while cellule.suivant is not None:
                cellule=cellule.suivant
            
            return cellule
    
    
    def ajoute(self, nouvelle):
        '''ajoute la cellule nouvelle
        à la fin ce la chaîne'''
        if self.tete is None:
            self.tete=nouvelle
        
        else:
            cellule=self.tete
            while cellule.suivant is not None:
                cellule=cellule.suivant
            
            cellule.suivant=nouvelle
     
    
    def trouve(self,x):
        '''renvoie l'index compé à partir de 0
        de la première occurence de la valeur x'''
        if self.tete is None:
            return False
        else:
            cellule=self.tete
            index=0
            while cellule is not None:
                if cellule.valeur == x:
                    return index
                cellule=cellule.suivant
                index=index+1
            return False         
    
    
    
    def __eq__(self,L):
        '''renvoie True ssi les deux listes sont identiques'''
        cellule1=self.tete
        cellule2=L.tete
        
        if cellule1 is None and cellule2 is None:
            return True
        
        while (cellule1 is not None and cellule2 is not None) and (cellule1.valeur==cellule2.valeur):
            cellule1=cellule1.suivant
            cellule2=cellule2.suivant
        
        if cellule1 is None and cellule2 is None:
            return True
        else:
            return False

    
    def __add__(self,L):
        '''concatène deux listes dans une nouvelle liste'''
        if self.tete is None:
            return L
        else:
            resultat=Lc(Cell(self.tete.valeur))
            cellule=self.tete
            n_cellule=resultat.tete
            
            while cellule.suivant is not None: #on crée une copie de self
                n_cellule.suivant=Cell(cellule.suivant.valeur)
                cellule=cellule.suivant
                n_cellule=n_cellule.suivant
            
            n_cellule.suivant=L.tete
            
            return resultat
    
    
    def reverse(self):
        '''renverse la liste'''
        rev=Lc()
        while self.tete is not None:
            rev.tete=Cell(self.tete.valeur,rev.tete) 
            self.tete=self.tete.suivant
        
        self.tete=rev.tete #on pointe self vers la liste créée
        
            
