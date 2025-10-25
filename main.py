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
    uncovered = set(subjects)
    for t in teachers:
        t.assigned_subjects = []

    selected = []

    while uncovered:
        best = None
        best_new = set()

        for t in teachers:
            new_subjects = t.can_teach_subjects & uncovered
            if not new_subjects:
                continue
            # Вибір за кількістю нових предметів, при рівності — наймолодший
            if (
                best is None
                or len(new_subjects) > len(best_new)
                or (len(new_subjects) == len(best_new) and t.age < best.age)
            ):
                best = t
                best_new = new_subjects

        if best is None:
            # Не вдається покрити залишок предметів
            return None

        # Призначаємо знайдені предмети цьому викладачу
        best.assigned_subjects = list(best_new)
        selected.append(best)
        uncovered -= best_new

    return selected


if __name__ == "__main__":
    # Множина предметів
    subjects = {"Math", "Physics", "Chemistry", "Biology", "Informatics"}
    # Створення списку викладачів
    teachers = [
        Teacher(
            "Oleksandr", "Ivanenko", 45, "o.ivanenko@example.com", {"Math", "Physics"}
        ),
        Teacher(
            "Maria", "Petrenko", 38, "m.petrenko@example.com", {"Informatics", "Math"}
        ),
        Teacher(
            "Sergiy",
            "Kovalenko",
            50,
            "s.kovalenko@example.com",
            {"Chemistry", "Biology"},
        ),
        Teacher(
            "Dmytro",
            "Bondarenko",
            35,
            "d.bondarenko@example.com",
            {"Physics", "Informatics"},
        ),
        Teacher(
            "Olena",
            "Grycenko",
            42,
            "o.grycenko@example.com",
            {"Biology"},
        ),
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(
                f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}"
            )
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
