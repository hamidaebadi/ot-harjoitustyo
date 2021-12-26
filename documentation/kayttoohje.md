## Käyttöohje
Lataa projektin viimeisimmän releasin lähdekoodi [täältä](https://github.com/hamidaebadi/ot-harjoitustyo/releases/tag/loppupalautus) kohdasta Assets valitsemalla Source Code.

#### Ohjelman Asennus
Ennen ohjelman käynnistämistä asenna kaikki riippuvuudet komennolla:

    poetry install

sen jälkeen alustaa tietokantaa komennolla:

    peotry run invoke build

### Ohjelman käynnistys
 ohjelma voidaan nyt käynnistää komennolla:
 
      poetry run invoke start

### Sisään kirjautuminen
  Sovelluksen käynnistyessä login-sivu tulee ilmi.
  
   <img width="610" alt="login_view" src="https://user-images.githubusercontent.com/65080068/146022399-1e736efc-bb07-4338-a046-3eb9dd161620.png">

Kirjaudu sisään seuraavilla tiedoilla:
 * Käyttäjätunnus: adminTest
 * Salasana: 1234

### Tuotteen lisääminen
   Tuotteet saadaan lisättyä kohdasta **lisää tuote**
   Määrittele kaikille sopiva arvo
   paina lopuksi **lisää varastoon** nappi.
   Muutokset näkyvät heti, kun tiedot saadaan talletettua tietokannalle.
    
   <img width="361" alt="product_addition_view" src="https://user-images.githubusercontent.com/65080068/146022531-79cc4449-9abd-4ea4-9c5e-865ebe20a777.png">

    

### Tuotteen etsiminen
  Voi etsiä tiettyä tuotetta varastosta kohdasta **Etsi Tuote** .
  Syötä tuotteen nimi tai QR-koodi
  lopuksi paina *Löydä tuote* nappia
    
   <img width="361" alt="produt_search_view" src="https://user-images.githubusercontent.com/65080068/146022601-9fbf34bd-8472-4a83-8d19-58bb7662af7b.png">


### Uuden kategorian lisääminen
  Uusien kategorioiden lisääminen onnistuu helposti kohdasta **lisää kategoria**.
  Syötetään sopiva kategorian nimi ja klikkataan sitten *lisää varastoon* nappia.
  Muutokset näkyvät heti, kun uusi kategoria on lisätty onnistuneesti tietokantaan.
    
   <img width="361" alt="category_import_view" src="https://user-images.githubusercontent.com/65080068/146022786-8e12b93d-66a1-4c7f-95c9-dda660d4d196.png">
