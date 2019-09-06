from application import app, db, login_required

from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application.reseptit.models import Resepti, Luokka
from application.reseptit.forms import ReseptiForm
from application.reseptit.forms import EditReseptiForm

@app.route("/reseptit", methods=["GET"])
def reseptit_index():
    return render_template("reseptit/list.html", reseptit = Resepti.query.all())

@app.route("/reseptit/new/")
@login_required()
def reseptit_form():
    return render_template("reseptit/new.html", form = ReseptiForm())

@app.route("/reseptit/<resepti_id>/", methods=["GET"])
@login_required()
def get_resepti(resepti_id):
    resepti = Resepti.query.get(resepti_id)
    form = ReseptiForm(obj=resepti)
    return render_template("reseptit/get_resepti.html", 
        resepti=Resepti.query.get(resepti_id), 
        form = form) 


@app.route("/reseptit/<resepti_id>/edit", methods=["GET","POST"])
@login_required()
def edit_resepti(resepti_id):

    if request.method == "GET":
        form = EditReseptiForm(obj=Resepti.query.get(resepti_id))
        return render_template("reseptit/edit_resepti.html", resepti=Resepti.query.get(resepti_id), form = form)

    form = EditReseptiForm(request.form)

    if not form.validate():
        return render_template("reseptit/edit_resepti.html", resepti=Resepti.query.get(resepti_id), form = form)

    resepti = Resepti.query.get(resepti_id)

    resepti.id = form.id.data
    resepti.name = form.name.data
    resepti.done = form.done.data
    resepti.ainesosat = form.ainesosat.data
    resepti.tyovaiheet = form.tyovaiheet.data
    resepti.tyypit = form.tyypit.data

    if form.liharuoka.data:
        luokka = Luokka("Liharuoka")
        resepti.luokat.append(luokka)

    if form.kasvis.data:
        luokka = Luokka("Kasvis")
        resepti.luokat.append(luokka)

    if form.vegaani.data:
        luokka = Luokka("Vegaani")
        resepti.luokat.append(luokka)
  
    if form.maidoton.data:
        luokka = Attribute("Maidoton")
        resepti.luokat.append(luokka)

    db.session().commit()

    return redirect(url_for("reseptit_index"))


@app.route("/reseptit/<resepti_id>/", methods=["POST"])
@login_required()
def reseptit_set_done(resepti_id):

    resepti = Resepti.query.get(resepti_id)
    resepti.done = True

    db.session().commit()
 
    return redirect(url_for("reseptit_index"))

@app.route("/reseptit/", methods=["POST"])
@login_required()
def reseptit_create():
    form = ReseptiForm(request.form)

    if not form.validate():
        return render_template("reseptit/new.html", form=form)

    resepti = Resepti(form.name.data, form.ainesosat.data, form.tyovaiheet.data, form.tyypit.data)
    resepti.account_id = current_user.id


    if form.liharuoka.data:
        luokka = Luokka("Liharuoka")
        resepti.luokat.append(luokka)

    if form.kasvis.data:
        luokka = Luokka("Kasvis")
        resepti.luokat.append(luokka)

    if form.vegaani.data:
        luokka = Luokka("Vegaani")
        resepti.luokat.append(luokka)
  
    if form.maidoton.data:
        luokka = Attribute("Maidoton")
        resepti.luokat.append(luokka)

    db.session().add(resepti)
    db.session().commit()
  
    return redirect(url_for("reseptit_index"))

@app.route("/reseptit/<resepti_id>/delete", methods=["POST"])
@login_required()
def delete_resepti(resepti_id):
    c = Resepti.query.get(resepti_id)
    db.session().delete(c)
    db.session().commit()

    return redirect(url_for("reseptit_index"))



@app.route("/reseptit/paaruoat/", methods=["GET"])
@login_required()
def paaruoat_by_current_user():
    reseptit = Resepti.paaruoat_by_current_user_query()

    return render_template("/reseptit/paaruoat_by_user.html", reseptit = reseptit)


@app.route("/reseptit/jalkkarit/", methods=["GET"])
@login_required()
def jalkiruoat_by_current_user():

    kayttajan_reseptit = ""
    if current_user.is_authenticated:
        kayttajan_reseptit = Resepti.jalkiruoat_by_current_user_query()
    return render_template("/reseptit/jalkiruoat_by_user.html", kayttajan_reseptit = kayttajan_reseptit)



