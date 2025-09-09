from flask import Blueprint, flash, render_template, request

from .services import search_students

students_bp = Blueprint("students", __name__)


@students_bp.route("/", methods=["GET", "POST"])
def home():
    students = []

    # FORM
    if request.method == "POST":
        success, message, students = search_students()

        if not success:
            flash(message, "error_students_home")

    return render_template("students/home.html", students=students)


@students_bp.route("/new")
def new_student():
    return render_template("students/new_student.html")
