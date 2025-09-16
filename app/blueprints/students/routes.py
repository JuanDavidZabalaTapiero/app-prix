from flask import Blueprint, flash, redirect, render_template, request, url_for

from app.blueprints.categories.services import get_all_categories
from app.blueprints.enrollments.services import create_enrollment_service

from .services import create_student_service, get_student, search_students

students_bp = Blueprint("students", __name__)


# == HOME ==
@students_bp.route("/", methods=["GET", "POST"])
def home():
    students = []

    # FORM
    if request.method == "POST":
        search_term = request.form.get("search_term")
        success, message, students = search_students(search_term)

        if not success:
            flash(message, "error_students_home")

    return render_template("students/home.html", students=students)


# == REGISTRAR NUEVO ALUMNO ==
@students_bp.route("/new")
def new_student():
    return render_template("students/new_student.html")


@students_bp.route("/create", methods=["POST"])
def create_student():
    if request.method == "POST":
        student_document_id = request.form.get("student_document_id").strip()
        student_name = request.form.get("student_name").strip()
        student_phone = request.form.get("student_phone").strip()

        success, message, _ = create_student_service(
            student_document_id, student_name, student_phone
        )

        if not success:
            flash(message, "error_students_new_student")
            return redirect(url_for("students.new_student"))

        flash(message, "success_students_new_student")

    return redirect(url_for("students.new_student"))


# == MATRICULAR ALUMNO ==
@students_bp.route("/new/enrollment")
def new_enrollment():
    success, message, categories = get_all_categories()

    if not success:
        flash(message, "error_students_new_enrollment")

    return render_template("students/new_enrollment.html", categories=categories)


@students_bp.route("/create/enrollment", methods=["POST"])
def create_enrollment():
    if request.method == "POST":
        student_document_id = request.form.get("student_document_id")

        # Buscar alumno
        success_student, message_student, student = get_student(student_document_id)

        if not success_student:
            flash(message_student, "error_students_new_enrollment")
            return redirect(url_for("students.new_enrollment"))

        # categoría
        category_id = request.form.get("category_id")

        # nueva matricula
        success_enrollment, message_enrollment, _ = create_enrollment_service(
            student.id, category_id
        )

        if success_enrollment:
            flash(message_enrollment, "success_students_new_enrollment")
        else:
            flash(message_enrollment, "error_students_new_enrollment")

    return redirect(url_for("students.new_enrollment"))
