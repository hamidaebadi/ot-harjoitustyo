## Testausdokumentti
Ohjelmaa on testattu sekä automatisoiduin yksikkö- ja integraatiotestein unittestilla sekä manuaalisesti tapahtunein järjestelmätason testein.

### Yksikkö- ja Integraatiotestaus
Ohjelman testaus jakautuu kahteen osaan.

###### Sovelluslogiikan testaus
Ohjelman sovelluslogiikan testauksella varmistettiin ohjelman sovelluslogiikan toimivan kunnolla. Sovelluslogiikasta
vastaavat luokat LoginServices, ImportServices ja StorageServices testataan luokilla TestLoginServices,
TestImportServices ja TestStorageServieces. 
Kaikissa luokissa injektoidaan tarvittavat riippuvuudet ennen jokaisen testin suorittamista setUp-metodissa.


###### Tietokannan kanssa kommunikoivan koodin testaus
Ohjelman testauksen toinen osa varmistaa ohjelman toiviman tietokannan kanssa ilman virheitä. Testauksessa varmistetaan
ohjelman keskeisen toiminnan eli tuotteiden lisääminen toiminta toimivan kunnolla. 
Repository-kansion luokan ProductRepository toimintaa testattiin ja varmistettiin toimivaksi.
Tietokannan koodiin kohdistuvat testit suoritetaan testitietokannssa kuin ohjelman päätietokanta.


### Testikattavuus
Ohjelman lopullinen testikattavuus on noin 75%. Testikattavuudesta on jätetty pois käyttöliitymän koodi
hakemistossa src/views. 


