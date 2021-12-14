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
 
 <img width="926" alt="skvenssi-login" src="https://user-images.githubusercontent.com/65080068/145084071-f0a3577a-45bf-4e38-9643-97653bae087d.png">
