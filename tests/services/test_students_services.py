from app.blueprints.students import services
from app.blueprints.students.models import Student


def test_get_all_students_returns_list(db, app):
    with app.app_context():
        s = Student(document_id="1234", name="Juan", phone="+317")
        db.session.add(s)
        db.session.commit()

        success, message, students = services.get_all_students()
        assert success is True
        assert message == "Alumnos consultados correctamente"
        assert isinstance(students, list)
        assert any(st.document_id == "1234" for st in students)
