from app import root, db
from models.models import User
from forms.user_form import ReceptionForm
from flask_login import login_required, current_user
from flask import render_template, redirect, request, url_for

@root.route("/receptions", methods=["GET"])
@root.route("/reception/list", methods=["GET"])
@login_required
def reception_page() -> render_template:
    receptions = User.query.filter_by(role = "RECEPTION", is_deleted = False).all()
    return render_template("reception/list.html", session=current_user, reception_list=receptions)

@root.route("/reception/create", methods=["GET","POST"])
@login_required
def reception_create_page() -> render_template:
    form = ReceptionForm()
    if form.validate_on_submit():
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        password = request.form['password']
        active = request.form.get('is_active')
        if active == "y":
            reception = User(first_name, last_name, phone_number, password, None, None, "RECEPTION", 0, True, current_user.id)
        else:
            reception = User(first_name, last_name, phone_number, password, None, None, "RECEPTION", 0, False, current_user.id)
        db.session.add(reception)
        db.session.commit()
        return redirect(url_for('reception_page'))
    return render_template("reception/create.html", form=form)

@root.route("/reception/delete/<id>", methods=["GET","POST"])
@login_required
def reception_delete_page(id) -> render_template:
    user = User.query.filter_by(id=id, is_deleted=False, role = "RECEPTION").first()
    user.is_deleted = True
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('reception_page'))
