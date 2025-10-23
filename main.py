# Визначення класу Teacher
class Teacher:

    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = []


def create_schedule(subjects, teachers):
    for subject in subjects:
        for teacher in teachers:
            if (
                subject in teacher.can_teach_subjects
                and subject not in teacher.assigned_subjects
            ):
                teacher.assigned_subjects.append(subject)
                break

    return teachers


if __name__ == "__main__":
    # Множина предметів
    subjects = {"Math", "Physics", "Chemistry", "Biology", "Informatics"}
    # Створення списку викладачів
    teachers = []

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(
                f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}"
            )
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
