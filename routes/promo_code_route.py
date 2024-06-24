from app import root, db
from models.models import PromoCode
from forms.promocode_form import PromocodeForm
from flask_login import login_required, current_user
from flask import render_template, redirect, request, url_for

@root.route("/promo-codes", methods=["GET"])
@root.route("/promo-code/list", methods=["GET"])
@login_required
def promo_code_page() -> render_template:
    promo_codes = PromoCode.query.filter_by(is_deleted = False).all()
    return render_template("promo_code/list.html", session=current_user, promo_code_list=promo_codes)

@root.route("/promo-code/create", methods=["GET","POST"])
@login_required
def promo_code_create_page() -> render_template:
    form = PromocodeForm()
    if form.validate_on_submit():
        name = request.form['name']
        publish_day = request.form['publish_day']
        active = request.form.get('is_active')
        if active == "y":
            promo = PromoCode(name, publish_day, True, current_user.id)
        else:
            promo = PromoCode(name, publish_day, False, current_user.id)
        db.session.add(promo)
        db.session.commit()
        return redirect(url_for('promo_code_page'))
    return render_template("promo_code/create.html", form=form)

@root.route("/promo-code/delete/<id>", methods=["GET","POST"])
@login_required
def promo_code_delete_page(id) -> render_template:
    promo = PromoCode.query.filter_by(id=id, is_deleted=False).first()
    promo.is_deleted = True
    db.session.add(promo)
    db.session.commit()
    return redirect(url_for('promo_code_page'))
