from application import db
from application.models import Base

class Kommentti(Base):

    name = db.Column(db.String(300), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    resepti_id = db.Column(db.Integer, db.ForeignKey('resepti.id'), nullable=False)

    def __init__(self, name):
        self.name = name

