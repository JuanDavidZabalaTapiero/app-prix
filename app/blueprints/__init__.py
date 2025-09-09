from .students.routes import students_bp


def register_blueprints(app):
    app.register_blueprint(students_bp)
