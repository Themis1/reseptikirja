## Käyttötapauksia

1. Käyttäjä kirjautuu sovellukseen sisään.
2. Käyttäjä lisää uuden reseptin.
3. Käyttäjä muokkaa reseptiä.
4. Käyttäjä kommentoi reseptiä (omaa tai toisen käyttäjän lisäämää).
5. Pääkäyttäjä poistaa reseptin.
6. Pääkäyttäjä poistaa kommentteja.
7. Käyttäjä rekisteröityy sovellukseen.

### SQL-kyselyt

2. INSERT INTO Reseptit (nimi, ainesosat, tyovaiheet) VALUES ('xxx', 'xxx', 'xxx');
3. UPDATE Reseptit SET nimi='xxx' WHERE nimi='xx';
4. INSERT into Kommentit (nimi) VALUES ('xxx');
5. DELETE FROM Reseptit WHERE nimi = 'xxx';
6. DELETE FROM Kommentit WHERE nimi = 'xxx';
7. INSERT INTO Account (nimi, email, kayttajatunnus, salasana) VALUES ('xxx', 'xxx', 'xxx');
