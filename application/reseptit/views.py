from application import app, db
from flask import redirect, render_template, request, url_for
from application.reseptit.models import Resepti

@app.route("/reseptit", methods=["GET"])
def reseptit_index():
    return render_template("reseptit/list.html", reseptit = Resepti.query.all())

@app.route("/reseptit/new/")
def reseptit_form():
    return render_template("reseptit/new.html")

@app.route("/reseptit/<resepti_id>/", methods=["POST"])
def reseptit_set_done(resepti_id):

    t = Resepti.query.get(resepti_id)
    t.done = True
    db.session().commit()
  
    return redirect(url_for("reseptit_index"))

@app.route("/reseptit/", methods=["POST"])
def reseptit_create():
    t = Resepti(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("reseptit_index"))
