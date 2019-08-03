from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, HiddenField, SubmitField, validators
from application.auth.models import User

class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus", [
        validators.DataRequired(message=("Anna käyttäjätunnus")),
        validators.Length(min=3, max=30, message=("Käyttäjätunnuksessa on 3-30 merkkiä"))
    ])
    password = PasswordField("Salasana", [
        validators.DataRequired(message=("Anna salasana")),
        validators.Length(min=3, max=30, message=("Salasanassa on 3-30 merkkiä"))
    ])

    class Meta:
        csrf = False

class SignUpForm(FlaskForm):
    name = StringField("Nimi", [
        validators.DataRequired(message=("Anna nimesi")),
        validators.Length(min=3, max=30, message=("Nimessä on oltava 3-30 merkkiä"))
    ])
    email = StringField("Sähköposti", [
        validators.Length(min=3, max=30, message=("Sähköpostissa on oltava 3-30 merkkiä")),
        validators.Email(message=("Anna toimiva sähköpostiosoite")),
        validators.DataRequired(message=("Sähköpostikenttä ei voi olla tyhjä"))
    ])
    username = StringField("Käyttäjätunnus", [
        validators.DataRequired(message=("Käyttäjätunnuskenttä ei voi olla tyhjä")),
        validators.Length(min=3, max=30, message=("Käyttäjätunnuksessa on oltava 3-30 merkkiä"))
    ])
    password = PasswordField("Salasana", [
        validators.DataRequired(message=("Salasanakenttä ei voi olla tyhjä")),
        validators.Length(min=3, max=30, message=("Salasanassa on oltava 3-30 merkkiä"))
    ])
    confirm = PasswordField("Varmista salasana", [
        validators.EqualTo("password", message=("Salasanakenttien on vastattava toisiaan"))
    ])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise validators.ValidationError("Käyttäjätunnus varattu. Valitse uusi käyttäjätunnus.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise validators.ValidationError("Sähköpostiosoite on jo rekisteröity. Valitse toinen sähköpostiosoite.")
    
    class Meta:
        csrf = False

class EditUserForm(FlaskForm):
    name = StringField("Nimi", [
        validators.DataRequired(message=("Anna nimesi")),
        validators.Length(min=3, max=30, message=("Nimessä on oltava 3-30 merkkiä"))
    ])
    email = StringField("Sähköposti", [
        validators.Length(min=3, max=30, message=("Sähköpostissa on oltava 3-30 merkkiä")),
        validators.Email(message=("Anna toimiva sähköpostiosoite")),
        validators.DataRequired(message=("Sähköpostikenttä ei voi olla tyhjä"))
    ])
    username = StringField("Käyttäjätunnus", [
        validators.DataRequired(message=("Käyttäjätunnuskenttä ei voi olla tyhjä")),
        validators.Length(min=3, max=30, message=("Käyttäjätunnuksessa on oltava 3-30 merkkiä"))
    ])
    id = HiddenField("Käyttäjän ID", [
        validators.DataRequired(message=("ID puuttuu"))
    ])
    submit = SubmitField("Päivitä")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()

        if user is not None and user.get_id() != int(self.id.data):
            raise validators.ValidationError("Käyttäjätunnus varattu. Valitse uusi käyttäjätunnus.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if user is not None and user.get_id() != int(self.id.data):
            raise validators.ValidationError("Sähköpostiosoite on jo rekisteröity. Valitse toinen sähköpostiosoite.")

    class Meta:
        csrf = False

class EditUserPasswordForm(FlaskForm):
    old_password = PasswordField("Vanha salasana", [
        validators.DataRequired(message=("Anna vanha salasana")),
    ])
    new_password = PasswordField("Uusi salasana", [
        validators.DataRequired(message=("Salasanakenttä ei voi olla tyhjä")),
        validators.Length(min=3, max=30, message=("Salasanassa on oltava 3-30 merkkiä"))
    ])
    confirm_password = PasswordField("Varmista salasana", [
        validators.EqualTo("new_password", message=("Salasanakenttien on vastattava toisiaan"))
    ])
    id = HiddenField("Käyttäjän ID", [
        validators.DataRequired(message=("ID puuttuu"))
    ])
    submit = SubmitField("Päivitä salasana")


    class Meta:
        csrf = False

