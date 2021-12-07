## Ohjelmistotekniikka
#### Ohjelmistotekniikan harjoitustyö
Kurssilla ohjelmistotekniikka-syksy 2021 toteutetaan harjoitustyönä yksi vapaavalintainen
sovellus, minkä tarkoituksena on soveltaa kurssilla **Ohjelmoinnin perusteet** ja
**Ohjelmoinnin jatkokurssin** opittuja asoita. 
Aihe on *vapaa valintainen*

## Varastonhallintajärjestelmä
Varastonhallintajärjestelmän avulla seurataan mitä tuotteita on ostettu ja lisätty varastoon, sekä
mitä tuotteita on myyty/poistettu varastosta. Varastonhallintajärjestelmään kirjautuu sisään vain
varaston ylläpitäjä.

### Dokumentaatio
 * [Käyttöohje](https://github.com/hamidaebadi/ot-harjoitustyo/blob/master/documentation/kayttoohje.md)
 * [Vaatimusmäärittely](https://github.com/hamidaebadi/ot-harjoitustyo/blob/master/documentation/vaatimusmaarittely.md)
 * [Työaikakirjanpito](https://github.com/hamidaebadi/ot-harjoitustyo/blob/master/documentation/tyoaikakirjanpito.md)
 * [Arkkitehtuurikuvaus](https://github.com/hamidaebadi/ot-harjoitustyo/blob/master/documentation/arkkitethtuuri.md)
 * [Viikko5-release](https://github.com/hamidaebadi/ot-harjoitustyo/releases/tag/viikko5)


### Asennus
###### Asenna riippuvuudet komennolla:
     poetry install

###### Alusta ohjelman tietokanta
    poetry run invoke build
      
###### Käynnistä sovellus komennolla:
     poetry run invoke start


### Komentorivitoiminnnot
###### Ohjelman suorittaminen
    poetry run invoke start

###### Ohjelman Testaaminen
    poetry run invoke test

###### Ohjelman testikattavuus
    peotry run invoke coverage-report

###### Ohjelman koodin ladunarviointi Pylintin avulla
    poetry run invoke lint
