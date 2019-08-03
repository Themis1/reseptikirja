from application import db
from application.models import Base

class Resepti(Base):

    name = db.Column(db.String(144), nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    ainesosat = db.Column(db.String(1000), nullable=False)
    tyovaiheet = db.Column(db.String(1000), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name, ainesosat, tyovaiheet):
        self.name = name
        self.done = False
        self.ainesosat = ainesosat
        self.tyovaiheet = tyovaiheet
