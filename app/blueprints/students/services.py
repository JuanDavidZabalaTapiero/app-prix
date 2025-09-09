from sqlalchemy import or_

from .models import Student


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


def search_students(term: str, only_incomplete: bool = False):
    """
    Search for students by name or document_id using LIKE.

    Args:
        term (str): search term.

    Returns:
        tuple: (success, message, list[Student])
    """
    try:
        students = Student.query.filter(
            or_(Student.name.ilike(f"%{term}%"), Student.document_id.ilike(f"%{term}%"))
        ).all()
        return (
            True,
            "Alumnos consultados correctamente por nombre o documento",
            students,
        )
    except Exception as e:
        print(f"Error al buscar estudiantes: {e}")
        return False, "Error interno al buscar los estudiantes", []
