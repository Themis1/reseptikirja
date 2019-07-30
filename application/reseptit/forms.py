from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators, HiddenField, SubmitField
from application.reseptit.models import Resepti

class ReseptiForm(FlaskForm):
    name = StringField("Reseptin nimi", [validators.DataRequired(message=("Nimi ei voi olla tyhjä")), validators.Length(min=2, max=300)])
#    kuvaus = StringField("Kuvaus", [validators.DataRequired(message=("Kuvaus ei voi olla tyhjä")), validators.Length(min=2, max=300)])
    done = BooleanField ("Kokeiltu")

    class Meta:
        csrf = False

class EditReseptiForm(FlaskForm):
    name = StringField("Reseptin nimi", [
        validators.DataRequired(message=("Anna reseptin nimi")),
        validators.Length(min=2, max=300, message=("Reseptin nimessä on 2-300 merkkiä"))
    ])
#    kuvaus = StringField("Kuvaus", [
#        validators.Length(min=3, max=300, message=("Kuvauksessa on 3-300 merkkiä")),
#        validators.DataRequired(message=("Anna asetukselle kuvaus"))
#    ])
    id = HiddenField("Reseptin ID", [
        validators.DataRequired(message=("ID puuttuu"))
    ])
    submit = SubmitField("Tallenna")

    done = BooleanField("Kokeiltu")

    def validate_name(self, name):
        name = Resepti.query.filter_by(name=name.data).first()

#    def validate_kuvaus(self, kuvaus):
#        kuvaus = Vna.query.filter_by(kuvaus=kuvaus.data).first()

    class Meta:
        csrf = False


