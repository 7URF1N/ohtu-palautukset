Viikko 2 – Tehtävä 9: Kokemuksia OpenCodesta

Käytin tehtävässä OpenCode-koodausagenttia NHL-reader-projektissa. Kokeilin sekä Build- että Plan-agenttia.

Metodin toteuttaminen

Pyysin Build-agenttia toteuttamaan PlayerStats-luokkaan metodin top_goal_scorers. Agentti toteutti metodin docstringin mukaisesti: se järjestää pelaajat tehtyjen maalien mukaan laskevasti ja palauttaa halutun määrän pelaajia. Toteutus oli myös tyyliltään samanlainen kuin luokan aikaisempi metodi.

Koodin ja Pylint-virheiden selittäminen

Plan-agentti selitti player_reader.py-tiedoston toiminnan sekä top_scorers_by_nationality-metodin vaihe vaiheelta. Selitykset olivat ymmärrettäviä ja vastasivat koodin toimintaa.

Kokeilin myös tehdä tarkoituksella liian pitkän koodirivin. Agentti selitti oikein Pylintin line-too-long-huomautuksen ja sen korjaamisen.

Uusi toiminnallisuus

Pyysin Build-agenttia lisäämään mahdollisuuden hakea NHL-pelaajia joukkueen perusteella ja järjestää heidät pisteiden mukaan. Agentti toteutti uuden top_scorers_by_team-metodin ja muokkasi ohjelman käyttöliittymää.

Kokeilin uutta toimintoa itse. Joukkuehaku toimi, ja myös aikaisemmat ominaisuudet säilyivät käytössä.

Yksikkötestit

Agentti loi kolme yksikkötestiä PlayerStats-luokalle. Testeissä käytettiin StubPlayerReader-luokkaa ja itse määriteltyjä testipelaajia, joten verkkoyhteyttä ei tarvittu.

Aikaisemmista harjoituksista poiketen en kirjoittanut kaikkia testejä itse, vaan tekoälyagentti loi ne antamieni ohjeiden perusteella.

Testit eivät aluksi käynnistyneet moduulien hakupolkuun liittyvän virheen vuoksi. Korjasin ongelman lisäämällä pytest-asetukset pyproject.toml-tiedostoon. Tämän jälkeen kaikki kolme testiä menivät läpi.

Pylint ja opitut asiat

Agentin tekemien muutosten jälkeen Pylint ilmoitti kerran rivinvaihtotapojen sekoittumisesta. Korjasin ongelman, ja lopuksi Pylint antoi tuloksen 10.00/10.

Opin, että tekoälyagentti voi auttaa nopeasti koodin kirjoittamisessa, selittämisessä ja testien tekemisessä. Sen tekemää koodia ei kuitenkaan kannata hyväksyä tarkistamatta. Ohjelmaa pitää kokeilla itse, testit suorittaa ja tehdyt muutokset käydä läpi.