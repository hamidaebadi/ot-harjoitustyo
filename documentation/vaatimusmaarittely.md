# Vaatimusmäärittely

### Sovelluksen perustiedot(päivittyy jatkuvasti)
 - *Aihe*: Varastonhallintajärjestelmä
 - *Versio*: 0.0.1
 - *Ohjelmointikieli*: Python ^3.8
 - *Toteutuksen tilanne*: Perusverion toteutus aloitettu
 - *Lisätiedot*: Projektin alussa yritetään suunnitella ja toteuttaa persuverion
		 käyttöön, minkä jälkeen toteutetaan jatkokehityksen tavoitteita. 
#### Sovelluksen Käyttötarkoitus
  Tämän sovelluksen pääkäyttötarkoitus on halinnoida varastotilan tietoa. Esimerkiksi 
	varastossa olevien tuotteiden ylläpito / päivittäminen, uusien tuotteiden rekisteröinti
	varastoon lisättäessä sekä varastosta pois vietyjen tuotteiden merkitseminen poistetuksi
	ja varastotilan päivittäminen jatkoylläpitoa varten.

#### Sovelluksen eri käyttäjäroolit
	Perusveriossa on vain yhdenlainen käyttäjä, jolla on ylläpitäjäoikeus. Hänellä on
	kaikki tarvittavat oikeudet varastotilan tietojen muokkaamiseksi ja ylläpitämiseksi.

#### Perusversion tarjoamat toiminnallisuudet
##### Funktionaaliset toiminnallisuudet	
- Varastonylläpitäjän on oltava kirjautunut sisään, jotta pääsisi hyödyntämään
 sovelluksen ominaisuuksia.
  - Ylläpitäjä kirjautuu sisään antamalla käyttäjätunnusta ja salasanaa
  - Jos kirjautuminen onnistuu, ylläpitäjä näkee sovelluksen päänäykymän, muuten
	häne näkee virheilmoitusta virheellisistä annetuista tiedoista.

- Kirjautunut varatonylläpitäjä näkee päänäkymässä kaikki varaston hyllypaikat
  - Jokaisella hyllyllä on oma tunniste
  - Jokaiseen hyllyyn kuuluu joukkoja tuotteita
- Ylläpitäjä voi lisätä uusia tuotteita tiettyyn hyllyyn
- Ylläpitäjä voi poistaa/myydä tuotteita tietystä hyllystä
- Ylläpitäjä voi etsia tiettyä tuotteetta koko varastosta

##### Ei-funktionaaliset toiminnallisuudet
- Sovelluksen tulee toimia OSX ja Linux-käyttöjärjestelmissä
- Sovelluksen data talletetaan sqlite-tietokantaan
- Sovelluksen tulee toimia myös oppilaitoksen koneella
- Sovelluksen pääohjelmointikieli on Python ^3.8
- Sovellukselle on suunniteltava graafinen käyttöliittymä

#### Jatkokehityksen ideoita
- Järjestelmään lisätään automaattinen raportointi varaston tilataphtumista viikon aikana
  - Lisättyjen tuotteiden tilastot
  - Poistettujen tuotteiden tilastot
- Tuotteiden filteröinti erilaisten ominaisuuksien perusteella
  - Filteröinti tietyn kategorian perusteella
  - Filteröinti hinnan perusteella
  - Filteröinti ajan perusteella
    - Tietyn ajanjakson aikana lisättyjen/poistettujen tuotteiden tiedot

