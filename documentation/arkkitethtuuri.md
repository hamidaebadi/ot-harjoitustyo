## Arkkitehtuuri
#### Rakenne
Ohjelman rakenne noudattaa MVC-arkkitehtuuria. projektin juuressa
Model-hakemisto kuvaa sovelluksessa olevia tietokohtia. Sovelluksessa
Tärkeimmät tietokohteet ovat User ja Product. Repositories-pakkaus
huolehtii tietokonnan kanssa kommunikoivasta koodista. Services-pakkaus
vastaa sovelluslogiikasta ja views-pakkaus huolehtii käyttöliittymän
koodista.

<img width="1038" alt="Screenshot 2021-11-30 at 20 59 45" src="https://user-images.githubusercontent.com/65080068/144111478-62d31fd6-8ea7-4355-83a1-1952a8a09888.png">



#### Tietojen pysyvätallennus
Sovellus käyttää tietojen pysyvätallennukseen SQLite tietokantaa.
Tietokantaa alustetaan sopivilla tiedoilla ohjelman käynnistäessä.
Tietojen tallennuksesta vastaa pakkaus repositories luokat CageRepository,
ProductRepository ja UserRepository.


#### Päätoiminnallisuudet
Kuvataan sovelluksen toimintalogiikka muutaman päätoiminnallisuuden osalta sekvenssikaaviona.

    ##### Käyttäjän kirjautuminen
    
    <img width="926" alt="skvenssi-login" src="https://user-images.githubusercontent.com/65080068/145084071-f0a3577a-45bf-4e38-9643-97653bae087d.png">
