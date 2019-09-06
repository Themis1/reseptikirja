from application import db
from application.models import Base
from sqlalchemy.sql import text
from flask_login import current_user

luokat = db.Table('luokat', 
    db.Column('luokat_id', db.ForeignKey('luokka.id'), primary_key=True),
    db.Column('resepti_id', db.Integer, db.ForeignKey('resepti.id'), primary_key=True))

class Luokka(db.Model):


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name

class Resepti(Base):

    __tablename__ = "resepti"

    name = db.Column(db.String(144), nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    ainesosat = db.Column(db.String(1000), nullable=False)
    tyovaiheet = db.Column(db.String(1000), nullable=False)
    tyypit = db.Column(db.String(30), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    luokat = db.relationship('Luokka', secondary=luokat, lazy='subquery', backref=db.backref('resepti', lazy=True))



    def __init__(self, name, ainesosat, tyovaiheet, tyypit):
        self.name = name
        self.done = False
        self.ainesosat = ainesosat
        self.tyovaiheet = tyovaiheet
        self.tyypit = tyypit


    def count_by_current_user():
        statement = text("Select Count(Account.id) AS count From Account JOIN Resepti "
                      "ON Resepti.account_id = Account.id WHERE Account.id = :account_id").params(account_id = current_user.id)
        result = db.engine.execute(statement).fetchone()
        return result['count']

    def get_all():
        statement = text("Select * From Resepti")
        result = db.engine.execute(statement).fetchall()
        return result
    
    def by_current_user():
        statement = text("SELECT * FROM Resepti "
                    "WHERE resepti.account_id = :account_id").params(account_id = current_user.id)
        reseptit = db.engine.execute(statement)
        return reseptit

    def paaruoat_by_current_user_query():
        statement = text("SELECT * FROM Resepti "
                    "JOIN Luokat ON Luokat.resepti_id = Resepti.id JOIN Luokka ON Luokka.id = luokat.luokat_id WHERE (Luokka.name = 'paaruoka') AND (resepti.account_id = :account_id)").params(account_id = current_user.id)
        reseptikysely = db.engine.execute(statement)
        return reseptikysely

    def jalkiruoat_by_current_user_query():
        statement = text("SELECT * FROM Resepti JOIN Luokat ON Luokat.resepti_id = resepti.id JOIN Luokka ON Luokka.id = luokat.luokat_id WHERE (Luokka.name = 'jalkiruoka') AND (Resepti.account_id = :account_id)").params(account_id = current_user.id)
        reseptikysely = db.engine.execute(statement)
        return reseptikysely
