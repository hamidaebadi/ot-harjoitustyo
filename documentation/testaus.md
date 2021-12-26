## Testausdokumentti
Ohjelmaa on testattu sekä automatisoiduin yksikkö- ja integraatiotestein unittestilla sekä manuaalisesti tapahtunein järjestelmätason testein.

### Yksikkö- ja Integraatiotestaus
Ohjelman testaus jakautuu kahteen osaan.

##### Sovelluslogiikan testaus

Ohjelman sovelluslogiikan testauksella varmistettiin ohjelman sovelluslogiikan toimivan kunnolla. Sovelluslogiikasta
vastaavat luokat LoginServices, ImportServices ja StorageServices testataan luokilla TestLoginServices,
TestImportServices ja TestStorageServieces. 
Kaikissa luokissa injektoidaan tarvittavat riippuvuudet ennen jokaisen testin suorittamista setUp-metodissa.


##### Tietokannan kanssa kommunikoivan koodin testaus

Ohjelman testauksen toinen osa varmistaa ohjelman toiviman tietokannan kanssa ilman virheitä. Testauksessa varmistetaan
ohjelman keskeisen toiminnan eli tuotteiden lisääminen toiminta toimivan kunnolla. 
Repository-kansion luokan ProductRepository toimintaa testattiin ja varmistettiin toimivaksi.
Tietokannan koodiin kohdistuvat testit suoritetaan testitietokannssa kuin ohjelman päätietokanta.


### Testikattavuus

Ohjelman lopullinen testikattavuus on noin 75%. Testikattavuudesta on jätetty pois käyttöliitymän koodi
hakemistossa src/views. 

<img width="1156" alt="Screenshot 2021-12-26 at 10 55 51" src="https://user-images.githubusercontent.com/65080068/147403814-702e770b-9052-4a96-8ccf-d09dd5df504a.png">


### Järjestelmätestaus

Järjestelmä kokonaisuudessaan testattiin manuaalisesti.

##### Asennus ja konfigurointi

Ohjelma ladattiin ja asennettiin käyttöohjen mukaan suorittmalla käyttöohjessa mainitut komennot sekä MacOS- että linux-koneessa. 
Ohjelmassa testattiin manuaalisesti myös tilanne, jossa käyttäjä yrittää lisätä tuotete tyhjillä syötteillä.


#### Sovelluksen laatuongelmat
Sovellus ei anna tällä hetkellä järkeviä virheilmoituksia, seuraavissa tilanteissa:

- Käyttäjä syöttaa jo olemassa olevaa tuotetta
- SQLite tietokantaa ei ole alustettu, eli python -m poetry run invoke build-komentoa ei ole suoritettu
