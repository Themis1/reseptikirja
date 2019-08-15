from application import db
from application.models import Base

from sqlalchemy.sql import text

class Resepti(Base):

    __tablename__ = "resepti"

    name = db.Column(db.String(144), nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    ainesosat = db.Column(db.String(1000), nullable=False)
    tyovaiheet = db.Column(db.String(1000), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    kommentit = db.relationship("Kommentti", backref='resepti', passive_deletes=True, lazy=True)

    def __init__(self, name, ainesosat, tyovaiheet):
        self.name = name
        self.done = False
        self.ainesosat = ainesosat
        self.tyovaiheet = tyovaiheet

    @staticmethod
    def reseptin_kommentit(resepti_id):
        stmt = text("SELECT Kommentti.name FROM Kommentti"
                    " LEFT JOIN Resepti ON Resepti.id = Kommentti.resepti_id"
                    " WHERE Resepti.id  = resepti_id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0]})
        return response
