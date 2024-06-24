from app import root, db
from models.models import Offer
from forms.offer_form import OfferForm
from flask_login import login_required, current_user
from flask import render_template, request, redirect, url_for

@root.route("/offers", methods=["GET"])
@root.route("/offer/list", methods=["GET"])
@login_required
def offer_page() -> render_template:
    offers = Offer.query.filter_by(is_deleted = False).all()
    return render_template("offer/list.html", session=current_user, offer_list=offers)

@root.route("/offer/create", methods=["GET", "POST"])
@login_required
def offer_create_page() -> render_template:
    form = OfferForm()
    if form.validate_on_submit():
        price = request.form['price']
        month = request.form['month']
        active = request.form.get('is_active')
        if active == "y":
            offer = Offer(price, month, True, current_user.id)
        else:
            offer = Offer(price, month, False, current_user.id)
        db.session.add(offer)
        db.session.commit()
        return redirect(url_for('offer_page'))
    return render_template("offer/create.html", form=form)

@root.route("/offer/delete/<id>", methods=["GET","POST"])
@login_required
def offer_delete_page(id) -> render_template:
    offer = Offer.query.filter_by(id=id, is_deleted=False).first()
    offer.is_deleted = True
    db.session.add(offer)
    db.session.commit()
    return redirect(url_for('offer_page'))
