CREATE DATABASE IF NOT EXISTS QuiVendsTout DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE QuiVendsTout;

CREATE TABLE CLIENT (
  refCli int,
  nomCli varchar(15),
  prenomCli varchar(15),
  adresseCli varchar(20),
  PRIMARY KEY (refCli)
);

CREATE TABLE FACTURE (
  refFac int,
  dateFac date,
  refCli int,
  PRIMARY KEY (refFac)
);

CREATE TABLE DETAIL (
  refFac int,
  refProd int,
  qte int,
  PRIMARY KEY (refFac, refProd)
);

CREATE TABLE PRODUIT (
  refProd int,
  nomProd varchar(40),
  puProd decimal(6,2),
  PRIMARY KEY (refProd)
);

ALTER TABLE FACTURE ADD FOREIGN KEY (refCli) REFERENCES CLIENT (refCli);
ALTER TABLE DETAIL ADD FOREIGN KEY (refProd) REFERENCES PRODUIT (refProd);
ALTER TABLE DETAIL ADD FOREIGN KEY (refFac) REFERENCES FACTURE (refFac);

