from sqlalchemy.exc import IntegrityError

from app.extensions import db

from .models import LicenseCategory


# == CREATE ==
def create_category_service(name):
    if not name:
        return False, "Todos los campos son obligatorios", None

    try:
        category = LicenseCategory(name=name)
        db.session.add(category)
        db.session.commit()
        return True, "Categoría creada correctamente", category

    except IntegrityError:
        db.session.rollback()
        return False, "La categoría ya está registrada", None

    except Exception as e:
        db.session.rollback()
        print(f"Error en create_category_service: {e}")
        return False, "Error al intentar crear la categoría", None


# == READ ==
def get_all_categories():
    try:
        categories = LicenseCategory.query.all()
        return True, "Categorías consultadas correctamente", categories
    except Exception as e:
        print(f"Error al intentar consultar las categorías: {e}")
        return False, "Error interno al consultar las categorías", []


def get_category(category_id):
    if not category_id:
        return False, "Todos los campos son obligatorios", None

    try:
        category = LicenseCategory.query.get(category_id)
        return True, "Categoría consultada correctamente", category

    except Exception as e:
        print(f"Error en get_category: {e}")
        return False, "Error al intentar consultar la categoría", None


# == UPDATE ==
def update_category(category_id, name):
    if not category_id or not name:
        return False, "Todos los campos son obligatorios", None

    try:
        category = get_category(category_id)
        category.name = name
        db.session.commit()
        return True, "Categoría editada correctamente", category

    except Exception as e:
        print(f"Error en update_category: {e}")
        return False, "Error al intentar editar la categoría", None


# == DELETE ==
