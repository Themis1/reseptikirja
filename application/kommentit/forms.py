from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators, HiddenField, SubmitField
from application.kommentit.models import Kommentti

class KommenttiForm(FlaskForm):
    name = StringField("Kommentti", [validators.DataRequired(message=("Anna kommentti!")), validators.Length(min=2, max=300)])

    class Meta:
        csrf = False

class EditKommenttiForm(FlaskForm):
    name = StringField("Kommentti", [
        validators.DataRequired(message=("Anna kommentti!")),
        validators.Length(min=2, max=300, message=("Kommentissa on maksimissaan 300 merkkiä"))
    ])

    id = HiddenField("Kommentin ID", [
        validators.DataRequired(message=("ID puuttuu"))
    ])
    submit = SubmitField("Tallenna")

    def validate_name(self, name):

        class Meta:
            csrf = False


