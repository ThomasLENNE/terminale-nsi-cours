# -*- coding: utf8 -*-
##
## Ce fichier est un module Python permettant de manipuler des arbres
## créé pour le DIU 2019 à l'Université d'Orléans
## très inspiré du module créé par Laurent Signac (28/03/2012)
## Laurent.Signac@univ-poitiers.fr
## régi par la licence CeCILL-C

import subprocess

class Arbre :
    """ Classe pour représenter des arbres """

    def __init__(self, label, enfants=None) :
        """
        Crée un arbre à partir d'un label qui ne DOIT PAS être None.
        Exemples :
        a = Arbre('A')
        c = Arbre('C', enfants = [a, Arbre('B')])
        """
        assert(label!=None)
        self.label = label
        self.enfants = enfants or []

    # ==================================================================
    # Une fonctionnalité facile à comprendre  ==========================
    # ==================================================================
    
    def ajoute(self,*a) :
        """ 
        Ajoute un ou plusieurs arbres a comme enfant(s) de la racine
        (en fin de liste)
        """
        self.enfants.extend(list(a))
        
        
    # ==================================================================
    # Redéfinir ce qu'affiche le print
    # ==================================================================
    
    def __str__(self) :
        """ Renvoie une représentation lisible de l'objet sous
        forme de chaîne de caractères
        """
        affiche=[]
        for noeud in self.enfants:
            affiche.append(str(noeud))
        affiche=",".join(affiche)
        if affiche!="" : 
            return ""+str(self.label)+"--["+affiche+"]"
        else : 
            return str(self.label)           

    # ==================================================================
    # Fonctionnalités d'affichage avec Graphviz et ImageMagick =========
    # qu'il est inutile de regarder                            =========
    # ==================================================================
                
    def _innerdot(self) :
        stri=""
        for a in self.enfants :
            stri+="{0} -> {1} [label=\"\"];\n".format(id(self),id(a))
        col="white"
        infos=str(self.label)
        attr="fillcolor=\"#888888ff\""
        stri+='\"{label}\"  [label=\"{infos}\", style = filled, peripheries = 1, \
                fillcolor = {col}, color = black];\n'.format(label=id(self),infos=infos,col=col)
        for a in self.enfants :
            stri+=a._innerdot()
        return stri

    def dot(self,printinfos=True) :
        """ Crée une chaîne de caractère contenant une
        description de l'arbre pour le programme dot (graphviz)
        """
        return "digraph g {\n"+self._innerdot()+"}\n"


    def save(self,filename='graphout.png') :
        """ Sauvegarde une image de l'arbre dans un fichier (Graphviz nécessaire)"""
        try :
            pipe=subprocess.Popen(['dot','-Tpng','-o',filename],stdin=subprocess.PIPE)
            pipe.stdin.write(self.dot().encode('ascii') + b'\n')
            pipe.stdin.close()
            pipe.wait()
        except OSError as e :
            print("Impossible de Tracer le graphe...")

    def view(self) :
        """ Affiche l'arbre (Graphviz et ImageMagick nécessaires)
        """
        try :
            pipe=subprocess.Popen(['dot','-Tpng'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
            pipe.stdin.write(self.dot().encode('ascii') + b'\n')
            pipe.stdin.close()
            l=pipe.stdout.read()
            pipe.wait()
            pipe=subprocess.Popen(['display'],stdin=subprocess.PIPE)
            pipe.stdin.write(l)
            pipe.stdin.close()
        except OSError as e :
            print("Impossible de Tracer le graphe...")



