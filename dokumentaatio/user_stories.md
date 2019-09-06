## Käyttötapauksia

1. Käyttäjä rekisteröityy sovellukseen.
2. Käyttäjä kirjautuu sovellukseen sisään.
3. Käyttäjä lisää uuden reseptin.
4. Käyttäjä muokkaa reseptiä.
5. Pääkäyttäjä poistaa reseptin. (toteuttamatta)
6. Käyttäjä listaa kaikki reseptit.
7. Käyttäjä listaa omat reseptinsä.


### SQL-kyselyt

SELECT * From Resepti;

SELECT Count(Account.id) AS count From Account JOIN Resepti ON Resepti.account_id = Account.id WHERE Account.id = :account_id").params(account_id = current_user.id);
        
SELECT * FROM Resepti WHERE resepti.account_id = :account_id").params(account_id = current_user.id);
  
SELECT * FROM Resepti JOIN Luokat ON Luokat.resepti_id = Resepti.id JOIN Luokka ON Luokka.id = luokat.luokat_id WHERE (Luokka.name = 'paaruoka') AND (resepti.account_id = :account_id)").params(account_id = current_user.id);
       
SELECT * FROM Resepti JOIN Luokat ON Luokat.resepti_id = resepti.id JOIN Luokka ON Luokka.id = luokat.luokat_id WHERE (Luokka.name = 'jalkiruoka') AND (Resepti.account_id = :account_id)").params(account_id = current_user.id);
   
SELECT Resepti.name FROM Resepti LEFT JOIN Account ON Account.id = Resepti.account_id" WHERE (account.id = :id)").params(id=account_id);

INSERT INTO Reseptit (nimi, ainesosat, tyovaiheet) VALUES ('xxx', 'xxx', 'xxx');
UPDATE Reseptit SET nimi='xxx' WHERE nimi='xx';
INSERT into Kommentit (nimi) VALUES ('xxx');
DELETE FROM Reseptit WHERE nimi = 'xxx';
DELETE FROM Kommentit WHERE nimi = 'xxx';
INSERT INTO Account (nimi, email, kayttajatunnus, salasana) VALUES ('xxx', 'xxx', 'xxx');
