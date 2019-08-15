from application import app, db, login_required

from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application.kommentit.models import Kommentti
from application.kommentit.forms import KommenttiForm
from application.kommentit.forms import EditKommenttiForm

@app.route("/kommentit", methods=["GET"])
def kommentit_index():
    return render_template("kommentit/list.html", kommentit = Kommentti.query.all())

@app.route("/kommentit/new/")
@login_required()
def kommentit_form():
    return render_template("kommentit/new.html", form = KommenttiForm())

@app.route("/kommentit/<kommentti_id>/", methods=["GET"])
@login_required()
def get_kommentti(kommentti_id):
    kommentti = Kommentti.query.get(kommentti_id)
    form = KommenttiForm(obj=kommentti)
    return render_template("kommentit/get_kommentti.html", kommentti=Kommentti.query.get(kommentti_id), form = form)

@app.route("/kommentit/<kommentti_id>/edit", methods=["GET","POST"])
@login_required()
def edit_kommentti(kommentti_id):

    if request.method == "GET":
        form = EditKommenttiForm(obj=Kommentti.query.get(kommentti_id))
        return render_template("kommentit/edit_kommentti.html", kommentti=Kommentti.query.get(kommentti_id), form = form)

    form = EditKommenttiForm(request.form)

    if not form.validate():
        return render_template("kommentit/edit_kommentti.html", kommentti=Kommentti.query.get(kommentti_id), form = form)

    kommentti = Kommentti.query.get(kommentti_id)

    kommentti.id = form.id.data
    kommentti.name = form.name.data
    db.session().commit()

    return redirect(url_for("kommentit_index"))

@app.route("/kommentit/", methods=["POST"])
@login_required()
def kommentit_create():
    form = KommenttiForm(request.form)

    if not form.validate():
        return render_template("kommentit/new.html", form=form)

    kommentti = Kommentti(form.name.data)
    kommentti.account_id = current_user.id

    db.session().add(kommentti)
    db.session().commit()
  
    return redirect(url_for("kommentit_index"))

@app.route("/kommentit/<kommentti_id>/delete", methods=["POST"])
@login_required()
def delete_kommentti(kommentti_id):
    c = Resepti.query.get(kommentti_id)
    db.session().delete(c)
    db.session().commit()

    return redirect(url_for("kommentit_index"))

