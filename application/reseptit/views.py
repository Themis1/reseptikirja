from application import app, db
from flask import redirect, render_template, request, url_for
from application.reseptit.models import Resepti
from application.reseptit.forms import ReseptiForm
from application.reseptit.forms import EditReseptiForm

@app.route("/reseptit", methods=["GET"])
def reseptit_index():
    return render_template("reseptit/list.html", reseptit = Resepti.query.all())

@app.route("/reseptit/new/")
def reseptit_form():
    return render_template("reseptit/new.html", form = ReseptiForm())

@app.route("/reseptit/<resepti_id>/", methods=["GET"])
def get_resepti(resepti_id):
    resepti = Resepti.query.get(resepti_id)
    form = ReseptiForm(obj=resepti)
    return render_template("reseptit/get_resepti.html", resepti=Resepti.query.get(resepti_id), form = form)

@app.route("/reseptit/<resepti_id>/edit", methods=["GET","POST"])
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
    db.session().commit()

    return redirect(url_for("reseptit_index"))


@app.route("/reseptit/<resepti_id>/", methods=["POST"])
def reseptit_set_done(resepti_id):

    t = Resepti.query.get(resepti_id)
    t.done = True
    db.session().commit()
  
    return redirect(url_for("reseptit_index"))

@app.route("/reseptit/", methods=["POST"])
def reseptit_create():
    form = ReseptiForm(request.form)

    if not form.validate():
        return render_template("reseptit/new.html", form=form)

    t = Resepti(form.name.data)
    t.done = form.done.data

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("reseptit_index"))

@app.route("/reseptit/<resepti_id>/delete", methods=["POST"])
def delete_resepti(resepti_id):
    c = Resepti.query.get(resepti_id)
    db.session().delete(c)
    db.session().commit()

    return redirect(url_for("reseptit_index"))

