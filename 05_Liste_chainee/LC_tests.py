#liste chînées tests

#???? ?? ????? ?

#Tests liste vide
print('__Liste_vide__')
L=Lc(Cell(1,Cell(1,Cell(2,Cell(3,Cell(5,None))))))
print(L, L.vide())

L1=Lc()
print(L1, L1.vide())
print()

#Tests longueur de la liste
print('__Longueur__')
L=Lc(Cell(1,Cell(1,Cell(2,Cell(3,Cell(5,None))))))
print(L, len(L))

L1=Lc()
print(L1, len(L1))
print()

#Tests accès aux éléments
print('__acces_elements__')
L=Lc(Cell(1,Cell(1,Cell(2,Cell(3,Cell(5,None))))))
print(L, L[0], L[5])

L1=Lc()
print(L1, L1[0])
print()

#Tests insertion d'élément
print('__insertion__')
#insérer dans une liste vide
L1=Lc()
print(L1)
L1.inserer(1,0)
print(L1)

#génération de la liste 1,1,3,5
L=Lc(Cell(1,Cell(1,Cell(3,Cell(5,None)))))
print(L)

#insérer au début de la liste
L.inserer(0,0)
print(L)

#inserer dans la liste
L.inserer(2,3)
print(L)

#insérer à la fin de la liste
L.inserer(8,len(L))
print(L)
print()

#Tests suppression d'élément
print('__suppression__')
#génération de la liste 1,1,3,5
L=Lc(Cell(1,Cell(1,Cell(1,Cell(2,Cell(3,Cell(5,None)))))))
print(L)

#supprimer au début de la liste
L.supprimer(0)
print(L)

#supprimer dans la liste
L.supprimer(2)
print(L)
L.supprimer(2)
print(L)
L.supprimer(2)
print(L)

#supprimer à la fin de la liste
L.supprimer(len(L)-1)
print(L)

#supprimer le seul élément de la liste
L.supprimer(0)
print(L)
print()

#Tests dernière cellule
print('__derniere__cellule')
L=Lc()
print(L.last()) #None

L=Lc(Cell(0))
print(L.last()) #0

L=Lc(Cell(1,Cell(1,Cell(2,Cell(3,Cell(5,Cell(8,None)))))))
print(L.last()) #5
print()

#tests ajoute
print('__ajouter_une_cellule__')
L=Lc()
print(L)
L.ajoute(Cell(1))
print(L)
L.ajoute(Cell(1))
print(L)
L.ajoute(Cell(2))
print(L)
L.ajoute(Cell(3))
print(L)
L.ajoute(Cell(5))
print(L)
print()

#Tests trouve élément
print('__trouve_element__')
L=Lc()
print(L.trouve(2)) #False

L=Lc(Cell(0))
print(L.trouve(0)) #0
print(L.trouve(1)) #False

L=Lc(Cell(1,Cell(1,Cell(2,Cell(3,Cell(5,Cell(8,None)))))))
print(L.trouve(1)) #0
print(L.trouve(3)) #3
print(L.trouve(8)) #5
print(L.trouve(7)) #False
print()

#Tests identiques
print('__identiques__')
L1=Lc()
L2=Lc()
print(L1==L2) # True

L1=Lc(Cell(0))
L2=Lc(Cell(1))
print(L1==L2) # False


L1=Lc(Cell(1,Cell(1,Cell(2,Cell(3,Cell(5,Cell(8,None)))))))
L2=Lc(Cell(1,Cell(1,Cell(2,Cell(3,Cell(5,Cell(8,None)))))))
L3=Lc(Cell(1,Cell(2,Cell(3,Cell(5,Cell(8,None))))))
print(L1==L2) #True
print(L2==L1) #True
print(L1==L3) #False
print()

#Tests concaténation
print('__concatenation__')
L1=Lc()
L2=Lc()
print(L1+L2) #[]

L3=Lc(Cell(0))
L4=Lc(Cell(1))
print(L3+L4) #[0,1]
print(L4+L3) #[1,0]
print(L3+Lc()) #[0]

L5=Lc(Cell(1,Cell(1,Cell(2,Cell(3,Cell(5,Cell(8,None)))))))
L6=Lc(Cell(13,Cell(21,Cell(34,None))))
L7=Lc()
print(L5+L6) # [1,1,2,3,5,8,13,21,34]
print(L6+L5) # [13,21,34,1,1,2,3,5,8]
print(L5+L7) # [1,1,2,3,5,8]
print()

#Tests renverser
print('__renverser__')
L=Lc(Cell(1,Cell(2,Cell(3,None))))
L.reverse()
print(L) #[3,2,1]
L.reverse()
print(L)#[1,2,3]

L=Lc()
L.reverse()
print(L) #[]
