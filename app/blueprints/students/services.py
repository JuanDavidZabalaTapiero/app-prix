from sqlalchemy import or_

from app.extensions import db

from .models import Student


# == CREATE ==
def create_student_service(document_id, name, phone):
    if not document_id or not name or not phone:
        return False, "Todos los campos son obligatorios", None

    try:
        existing_student = Student.query.filter_by(document_id=document_id).first()

        if existing_student:
            return False, "El alumno ya se encuentra registrado", None

        student = Student(document_id=document_id, name=name, phone=phone)
        db.session.add(student)
        db.session.commit()
        return True, "Alumno registrado correctamente", student
    except Exception as e:
        db.session.rollback()
        print(f"Error al intentar registrar el alumno: {e}")
        return False, "Ocurrió un error interno al intentar registrar el alumno", None


# == READ ==
def get_all_students():
    """
    Retrieve all students from the database.

    Returns:
        tuple: (success: bool, message: str, students: list[Student])
    """
    try:
        students = Student.query.all()
        return True, "Alumnos consultados correctamente", students
    except Exception as e:
        print(f"Error al intentar consultar los alumnos: {e}")
        return False, "Error interno al intentar consultar los alumnos", []


def get_student(document_id):
    if not document_id:
        return False, "Todos los campos son obligatorios", None
    try:
        student = Student.query.filter_by(document_id=document_id).first()

        # No existe el alumno
        if not student:
            return False, f"No existe el alumno con id {document_id}", None

        return True, "Alumno consultado correctamente", student

    except Exception as e:
        print(f"Error en get_student: {e}")
        return False, "Error al consultar el alumno", None


def search_students(term: str):
    """
    Search for students by name or document_id using LIKE.

    Args:
        term (str): search term.

    Returns:
        tuple: (success, message, list[Student])
    """
    try:
        students = (
            Student.query.filter(
                or_(
                    Student.name.ilike(f"%{term}%"),
                    Student.document_id.ilike(f"%{term}%"),
                )
            )
            .all()
            .limit(100)
        )

        return (
            True,
            "Alumnos consultados correctamente por nombre o documento",
            students,
        )
    except Exception as e:
        print(f"Error al buscar estudiantes: {e}")
        return False, "Error interno al buscar los estudiantes", []


#  == UPDATE ==

# == DELETE ==
