from app import root
from forms.user_form import LoginForm
from models.models import User, PromoCode, Offer
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

SESSION = None

@root.route("/", methods=["GET", "POST"])
@root.route("/home", methods=["GET", "POST"])
def home_page() -> render_template:
    form = LoginForm()
    if form.validate_on_submit():
        phone_number = "998" + form.phone_number.data
        password = form.password.data
        user = User.query.filter_by(phone = phone_number, password=password, is_deleted=False, is_active = True).first()
        if user is None:
            flash("Username or Password are not match! Please try again!", category="danger")
        elif user.role == "ADMIN":
            login_user(user)
            studnets = User.query.filter_by(role = "STUDENT", is_deleted = False).all()
            promo_codes = PromoCode.query.filter_by(is_deleted = False).all()
            offers = Offer.query.filter_by(is_deleted = False).all()
            receptions = User.query.filter_by(role = "RECEPTION", is_deleted = False).all()
            flash(f"Successfully logged in! Welcome {user.first_name}", category="success")
            return render_template("home_admin.html", form=form, session=user, student_count=len(studnets), promo_code_count=len(promo_codes), offer_count=len(offers), reception_count=len(receptions))
        elif user.role == "RECEPTION":
            login_user(user)
            studnets = User.query.filter_by(role = "STUDENT", is_deleted = False).all()
            promo_codes = PromoCode.query.filter_by(is_deleted = False).all()
            offers = Offer.query.filter_by(is_deleted = False).all()
            receptions = User.query.filter_by(role = "RECEPTION", is_deleted = False).all()
            flash(f"Successfully logged in! Welcome {user.first_name}", category="success")
            return render_template("home_reception.html", form=form, session=user, student_count=len(studnets), promo_code_count=len(promo_codes))
        else:
            flash("Permission denied! Please try again!", category="danger")
    if current_user.is_authenticated:
        if current_user.role == "ADMIN":
            studnets = User.query.filter_by(role = "STUDENT", is_deleted = False).all()
            promo_codes = PromoCode.query.filter_by(is_deleted = False).all()
            offers = Offer.query.filter_by(is_deleted = False).all()
            receptions = User.query.filter_by(role = "RECEPTION", is_deleted = False).all()
            return render_template("home_admin.html", form=form, session=current_user, student_count=len(studnets), promo_code_count=len(promo_codes), offer_count=len(offers), reception_count=len(receptions))
        else:
            studnets = User.query.filter_by(role = "STUDENT", is_deleted = False).all()
            promo_codes = PromoCode.query.filter_by(is_deleted = False).all()
            offers = Offer.query.filter_by(is_deleted = False).all()
            receptions = User.query.filter_by(role = "RECEPTION", is_deleted = False).all()
            return render_template("home_reception.html", form=form, session=current_user, student_count=len(studnets), promo_code_count=len(promo_codes))
    else:
        return render_template("user/login.html", form=form)

@root.route("/logout", methods=["GET"])
@login_required
def logout_page():
    logout_user()
    return redirect(url_for("home_page"))

@root.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404

@root.errorhandler(401)
def unauthorized(e):
    return render_template('error/401.html'), 401
