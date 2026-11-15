# Viikko 3 – Tehtävä 8: Kokemuksia tekoälyagentin käytöstä

## Agentin ohjetiedosto

Käytin tehtävässä OpenCode-agenttia. Generoin `/init`-komennolla `AGENTS.md`-ohjetiedoston. Aluksi tiedosto sisälsi ohjeita koko `ohtu-palautukset`-repositorion projekteista, joten muokkasin sitä keskittymään vain WebLogin-sovellukseen.

Lisäsin ohjeisiin tiedot `uv`-komennoista, Flask-sovelluksen käynnistämisestä, portista 5001, Robot Framework -testien suorittamisesta ja käyttäjätietojen validoinnin sijainnista.

## Testit ennen toteutusta

Agentti kirjoitti hyväksymistestit ennen sovelluksen toteutuksen muuttamista, kun ohjeistin sitä tekemään niin.

Ensimmäisessä käyttäjätarinassa testattiin, ettei salasana saa koostua pelkästään kirjaimista. Uusista testeistä kaksi epäonnistui odotetusti ennen toteutuksen korjaamista.

Toisessa käyttäjätarinassa testattiin salasanan ja salasanavahvistuksen yhtäsuuruus. Myös tässä uusi testi epäonnistui odotetusti ennen korjausta.

Kun molemmat toiminnallisuudet oli toteutettu, kaikki 15 Robot Framework -testiä menivät läpi.

## Agentin ohjaaminen

Agenttia piti ohjata useamman kerran. Se käytti aluksi Robot Frameworkin `Fill Secret` -avainsanaa virheellisesti, minkä vuoksi testit eivät toimineet. Virhe korjattiin.

Pidin myös huolen siitä, ettei agentti muuttanut sovelluksen toteutusta ennen epäonnistuvien testien suorittamista. Agentti ehdotti eräässä vaiheessa testin URL-tarkistuksen poistamista, mutta en hyväksynyt tarkistuksen heikentämistä.

Asetin OpenCoden kysymään luvan tiedostojen muokkaamiseen ja komentojen suorittamiseen. Näin pystyin tarkistamaan agentin ehdotuksia.

## Testien luotettavuuden tarkistaminen

Rikoin sovelluksen tarkoituksella kahdella tavalla.

Ensin poistin väliaikaisesti käytöstä tarkistuksen, joka hylkää pelkistä kirjaimista koostuvan salasanan. Tätä testaava Robot-testi epäonnistui odotetusti.

Seuraavaksi poistin väliaikaisesti käytöstä salasanan vahvistuksen tarkistuksen. Myös tätä testaava Robot-testi epäonnistui.

Palautin molemmat tarkistukset ja suoritin kaikki testit uudelleen. Lopputuloksena oli 15 onnistunutta testiä eikä yhtään epäonnistumista.

## Mitä opin?

Opin, että tekoälyagentti pystyy nopeuttamaan testien ja sovelluskoodin kirjoittamista, mutta sen ehdotuksia ei kannata hyväksyä tarkistamatta.

Erityisen tärkeää on kirjoittaa testit ennen toteutusta ja varmistaa, että ne todella havaitsevat virheet. Opin myös, että testin epäonnistuminen voi johtua joko sovelluksen virheestä tai itse testin virheellisestä toteutuksesta.

Agentin työtä pitää valvoa, ja vastuu koodin oikeellisuudesta jää ohjelmoijalle.