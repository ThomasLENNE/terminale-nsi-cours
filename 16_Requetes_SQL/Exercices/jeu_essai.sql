
-- les clients
insert into CLIENT(refCli,nomCli, prenomCli,adresseCli) values
	(1,'BANAZIAI','Jules','Grenoble'),
	(2,'DONGEPLI','Armelle','Limoges'),
	(3,'BOBAINO','Julie','Nimes'),
	(4,'BOUTIDICHT','Maxime','Grenoble');

-- les produits
insert into PRODUIT(refProd,nomProd,puProd) values 
	(1, 'Sucre',1.2),
	(2, 'Cereales',1.3),
	(3, 'Biscottes',1.15),
	(4, 'Poudre petit dejeuner',2.3),
	(5, 'Cafe',2.50),
	(6, 'The',3.1);

-- les factures 
insert into FACTURE(refFac, dateFac, refCli) values
	(1, STR_TO_DATE('14/6/2019','%d/%m/%Y'),2),
	(2, STR_TO_DATE('26/12/2019','%d/%m/%Y'),2),
	(3, STR_TO_DATE('14/3/2019','%d/%m/%Y'),1);

-- les lignes de factures 
insert into DETAIL(refFac, refProd, qte) values
	(1,2,8),
	(1,3,2),
	(2,6,7),
	(3,1,2),
	(3,3,2),
	(3,5,9);
