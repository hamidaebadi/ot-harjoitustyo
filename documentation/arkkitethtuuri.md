## Arkkitehtuuri
## Rakenne

Ohjelman rakenne noudattaa MVC-arkkitehtuuria. projektin juuressa
Model-hakemisto kuvaa sovelluksessa olevia tietokohtia. Sovelluksessa
Tärkeimmät tietokohteet ovat User ja Product. Repositories-pakkaus
huolehtii tietokonnan kanssa kommunikoivasta koodista. Services-pakkaus
vastaa sovelluslogiikasta ja views-pakkaus huolehtii käyttöliittymän
koodista.

<img width="1202" alt="classDiagram" src="https://user-images.githubusercontent.com/65080068/146021551-9ae1a45b-3879-4bb6-b880-fb6ad5802213.png">




## Tietojen pysyvätallennus
Sovellus käyttää tietojen pysyvätallennukseen SQLite tietokantaa.
Tietokantaa alustetaan sopivilla tiedoilla ohjelman käynnistäessä.
Tietojen tallennuksesta vastaa pakkaus repositories luokat CageRepository,
ProductRepository ja UserRepository.


## Päätoiminnallisuudet
Kuvataan sovelluksen toimintalogiikka muutaman päätoiminnallisuuden osalta sekvenssikaaviona.

  ## Käyttäjän kirjautuminen

  Sovlluksen käynnistyessä, käyttäjän on kirjauduttuva sisään sovellukseen.
  Kun käyttäjä syöttää tunnukset ja painaa *kirjaudu siään* nappia, luokka LoginView käyttää
  LoginServices-luokasta muodostetun olion metodi login(), jolle annetaan tunnukset. Metodissa login 
  käytetään luokan UserRepository:n metodia verify_user(), jolle välitetään käyttäjän antamat tunnukset.
  Jos välitetyt tiedot ovat oikein, metodi verify_user() palauttaa True metodille login, joka sekin
  palauttaa True sitä kutsuvalle muuttujalle.
  Jos kaikki on kunnossa, suoritetaan luokan UI metodia _show_workstation_view(), joka näyttää
  sovelluksen päänäkymää.

 <img width="926" alt="skvenssi-login" src="https://user-images.githubusercontent.com/65080068/145084071-f0a3577a-45bf-4e38-9643-97653bae087d.png">

 ## Uuden tuotteen lisääminen
 
 <img width="1250" alt="product_addition_sequence_diagram" src="https://user-images.githubusercontent.com/65080068/146032300-08968a91-ce35-4fe1-bd0d-3c79add4a422.png">
