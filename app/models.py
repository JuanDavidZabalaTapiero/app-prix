from .blueprints.categories.models import LicenseCategory
from .blueprints.enrollments.models import Enrollment
from .blueprints.instructor_vehicles.models import InstructorVehicle
from .blueprints.instructors.models import Instructor
from .blueprints.lessons.models import Lesson
from .blueprints.students.models import Student
from .blueprints.vehicles.models import Vehicle

__all__ = [
    "Student",
    "LicenseCategory",
    "Instructor",
    "Vehicle",
    "InstructorVehicle",
    "Enrollment",
    "Lesson",
]
