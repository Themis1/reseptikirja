# Asennusohje

Sovellus on websovellus, jonka toimintaympäristö on selain. Tästä syystä ohjelmalle ei ole varsinaisia asennusohjeita, vaan ohjeet kirjataan sovelluksen lokaalin käyttöympäristön luomista varten. Sovelluksen suunniteltu toimintaympäristö on kuitenkin erillinen verkkopalvelin tai Herokua vastaava alusta.

*Asennusohjeissa oletetaan, että käyttäjälle on tuttua komentorivin käyttö. Ohjeet on kirjoitettu Linux tai MacOS käyttäjille - Windows tuki on rajoitettua*

### Ennen sovelluksen lataamista
Varmista, että koneellesi on asennettu Python ja sqlite3. Nämä ovat sovelluksen lokaalin version kannalta pakollisia. Voit käyttää esimerkiksi alla olevia komentoja. Mikäli käytät Linuxia on koneellasi hyvin todennäköisesti Python valmiiksi asennettuna.
```
$ sudo apt-get update
$ sudo apt-get install python3
$ sudo apt-get install sqlite3
```
Mikäli käytät MacOS -laitetta, suosittelen käyttämään Homebrew nimistä paketinhallintaohjelmistoa, joka toimii Linuxin apt-get:in tapaan. Asenna Homebrew ja suorita seuraavat komennot
```
$ brew install python3
$ brew install sqlite3
```
Mikäli lataat sovelluksen ZIP pakkauksena, on sinulla oltava pakkausten purkamiseen soveltuva ohjelma, esimerkiksi 7zip.

Koneellasi on oltava jokin verkkoselain, jotta voit katsella projektin luomia sivunäkymiä.

Projekti on jaoteltu useisiin kansioihin ja tiedostoihin, joiden selaaminen kansiosta tai komentoriviltä voi olla hankalaa. Suositeltavaa on käyttää jonkinlaista IDE ohjelmistoa, esimerkiksi ilmaista Visual Studio Codea, jossa on hyvä Python tuki ja mukiinmenevä integroitu git käyttöliittymä.

(Mikäli haluat kloonata projektin, on koneellasi oltava asennettuna myös Git)


### Asennus step-by-step pakatun tiedoston kautta

1. Lataa sovellus pakattuna ZIP-tiedostona sovelluksen [Github](https://github.com/Themis1/reseptikirja) -sivulta Clone or download -painikkeen kautta

2. Pura tiedosto haluamaasi kansioon koneellasi

3. Navigoi komentorivin kautta kansioon, johon purit projektin pakkauksen

4. Luo Pythonin virtuaaliympäristö ja ota se käyttöön seuraavilla komennoilla
```
$ python3 -m venv venv
$ source venv/bin/activate
```

5. Python3:ssa on laajennusten asentamiseen käyttettävä Pip valmiiksi asennettuna, asennetaan sovelluksen käyttämä Flask -kirjasto. Voit myös tässä vaiheessa päivittää pip:in uudempaan versioon.
```
$ pip install Flask
$ pip install --upgrade pip 
```

6. Asenna sovelluksen requirements.txt määrittelemät riippuvuudet, jotta sovellus toimii oikein. Pip osaa etsiä omatoimisesti tiedostoon määritellyt riippuvuudet ja asentaa ne.
```
$ pip install -r requirements.txt
```
7. Voit nyt käyttää sovellusta käynnistämällä sen seuraavalla komennolla
```
$ python3 run.py
```

8. Navigoi osoitteeseen http://127.0.0.1:5000

9. Voit nyt käyttää sovellusta lokaalissa verkkoympäristössä

### Git kloonaus

1. Kopioi [Github](https://github.com/Themis1/reseptikirja) -sivulta Clone or download -painikkeen takaa löytyvä linkki

2. Navigoi komentorivillä haluamaasi kansioon, johon projektin kloonikansio tulee

3. Kloonaa kansio. Tämä operaatio kopioi projektin githubista määrittelemääsi kansioon.
```
$ git clone <github sivulta löytämäsi linkki> <nimi kansiolle>
```
4. Referoi ZIP -tiedoston asennusohjeita kohdasta 3. eteenpäin

## Sovelluksen asennus Herokuun
requirements.txt:n ja koodissa olevien määrittelyiden pitäisi olla ajantasalla automaattisesti, jos projekti on kopioitu githubista.

1. Asenna sovellus yllä kuvatun mukaisesti paikallisesti

2. Luo Herokuun käyttäjätunnus Herokun sivuilla

3. Asenna koneellesi Herokun komentorivisovellus  
  #### Linux
```
$ sudo snap install heroku --classic
```
  #### MacOS
```
$ brew install heroku/brew/heroku
```

4. Kirjaudu sisään Herokuun
```
$ heroku login
```

5. Navigoi kansioon johon loit paikallisen projektin ja luo Heroku projekti siitä
```
$ cd ~/projekti
$ heroku create projekti
```

6. Lisää paikalliseen versionhallintaan tieto Herokusta ja lähetä projekti Herokuun
```
$ git remote add heroku
$ git add .
$ git commit -m "Heroku asennus"
$ git push heroku master
```

7. Projekti pyörii nyt Herokussa

8. Viritä seuraavaksi Herokun PostgreSQL tietokanta, jotta sovelluksen tieto tallentuu myös Herokussa
```
$ heroku config:set HEROKU=1
$ heroku addons:add heroku-postgresql:hobby-dev
```

9. Sovelluksella on nyt toimiva PostgreSQL -tietokanta Herokun palvelimella
