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
