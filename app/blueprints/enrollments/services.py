from app.extensions import db

from .models import Enrollment


# == CREATE ENROLLMENT ==
def create_enrollment_service(student_id, category_id):
    try:
        existing_enrollment = Enrollment.query.filter_by(
            student_id=student_id, category_id=category_id
        ).first()

        if existing_enrollment:
            return False, "La matricula ya se encuentra registrada", None

        enrollment = Enrollment(student_id=student_id, category_id=category_id)
        db.session.add(enrollment)
        db.session.commit()

        return True, "Matricula registrada correctamente", enrollment

    except Exception as e:
        db.session.rollback()
        print(f"Error al intentar registrar la matricula: {e}")
        return False, "Error interno al intentar registrar la matricula", None


# == READ ENROLLMENT ==
# == UPDATE ENROLLMENT ==
# == DELETE ENROLLMENT ==
