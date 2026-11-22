# Viikko 4 – Tehtävä 4: Testikoodin siistiminen tekoälyagentilla

Käytin OpenCode-agenttia verkkokauppaprojektin testikoodin siistimiseen. Pyysin agenttia poistamaan toistuvaa koodia siirtämällä yhteiset Mock-olioiden alustukset `setUp`-metodiin. Agentti teki muutoksen mielestäni järkevästi. Pankin, varaston ja viitegeneraattorin Mock-oliot luodaan nyt yhdessä paikassa ennen jokaista testiä. Myös `Kauppa`-olio alustetaan siellä.

Tarkistin muutokset `git diff` -komennolla ja lukemalla koko testitiedoston. Kaikki viisi testiä säilyivät. Agentti ei poistanut eikä heikentänyt `assert_called_with`- tai `assert_called_once_with`-tarkistuksia. Myös testikohtaiset varastosaldot ja tuotteet säilyivät. Agentti ilmoitti kaikkien viiden testin menneen läpi. On edelleen joitain alutuskoodia mitä on tarpeetonta.

Agentti kysyi luvan ennen muutosten tekemistä, ja annoin luvan säilyttäen vaatimuksen, ettei testien toiminta saa muuttua. Muita korjauksia ei tarvinnut tehdä. 

Opin, että tekoälyagentti voi auttaa vähentämään koodin toisteisuutta, mutta sen tekemät muutokset pitää aina tarkistaa. Pelkkä testien läpäisy ei takaa, että testien tarkistukset ovat säilyneet yhtä tarkkoina.