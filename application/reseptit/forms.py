from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators, HiddenField, SubmitField
from application.reseptit.models import Resepti

class ReseptiForm(FlaskForm):
    name = StringField("Reseptin nimi", [validators.DataRequired(message=("Nimi ei voi olla tyhjä")), validators.Length(min=2, max=144)])
#    kuvaus = StringField("Kuvaus", [validators.DataRequired(message=("Kuvaus ei voi olla tyhjä")), validators.Length(min=2, max=300)])
    done = BooleanField ("Kokeiltu")
    ainesosat = StringField("Ainesosat", [validators.Length(max=1000)])
    tyovaiheet = StringField("Työvaiheet", [validators.Length(max=1000)])


    class Meta:
        csrf = False

class EditReseptiForm(FlaskForm):
    name = StringField("Reseptin nimi", [
        validators.DataRequired(message=("Anna reseptin nimi")),
        validators.Length(min=2, max=144, message=("Reseptin nimessä on 2-144 merkkiä"))
    ])
    ainesosat = StringField("Ainesosat", [
        validators.Length(max=1000, message=("Kuvauksessa on korkeintaan 1000 merkkiä")),
    ])

    tyovaiheet = StringField("Työvaiheet", [
        validators.Length(max=1000, message=("Työvaiheissa on korkeintaan 1000 merkkiä")),
    ])

    id = HiddenField("Reseptin ID", [
        validators.DataRequired(message=("ID puuttuu"))
    ])
    submit = SubmitField("Tallenna")

    done = BooleanField("Kokeiltu")

    def validate_name(self, name):
        name = Resepti.query.filter_by(name=name.data).first()

    def validate_ainesosat(self, ainesosat):
        ainesosat = Resepti.query.filter_by(ainesosat=ainesosat.data).first()

    def validate_tyovaiheet(self, tyovaiheet):
        tyovaiheet = Resepti.query.filter_by(tyovaiheet=tyovaiheet.data).first()


    class Meta:
        csrf = False


