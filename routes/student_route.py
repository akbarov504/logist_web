from app import root
from models.models import User
from flask import render_template
from flask_login import login_required, current_user

@root.route("/students", methods=["GET"])
@root.route("/student/list", methods=["GET"])
@login_required
def student_list_page() -> render_template:
    students = User.query.filter_by(role = "STUDENT", is_deleted = False).all()
    return render_template("student/list.html", session=current_user, student_list=students)
