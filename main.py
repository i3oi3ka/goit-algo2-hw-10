class Teacher:

    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = []

    def __repr__(self):
        return f"Teacher({self.first_name} {self.last_name}, {self.age})"


def create_schedule(subjects, teachers):
    uncovered = set(subjects)
    # Скидаємо попередні призначення
    for t in teachers:
        t.assigned_subjects = []

    selected = []

    while uncovered:
        best = None
        best_new = set()

        for t in teachers:
            # Знаходимо предмети, які викладач може вести І які ще не покриті
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
            # Повертаємо None і непокриті предмети для діагностики
            return None, uncovered

        # Призначаємо знайдені предмети цьому викладачу
        best.assigned_subjects = list(best_new)
        selected.append(best)
        uncovered -= best_new

    return selected, uncovered


if __name__ == "__main__":
    # Множина предметів (відповідно до умови)
    subjects = {"Математика", "Фізика", "Хімія", "Інформатика", "Біологія"}

    # Створення списку викладачів (відповідно до умови)
    teachers = [
        Teacher(
            "Олександр",
            "Іваненко",
            45,
            "o.ivanenko@example.com",
            {"Математика", "Фізика"},
        ),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher(
            "Сергій",
            "Коваленко",
            50,
            "s.kovalenko@example.com",
            {"Інформатика", "Математика"},
        ),
        Teacher(
            "Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}
        ),
        Teacher(
            "Дмитро",
            "Бондаренко",
            35,
            "d.bondarenko@example.com",
            {"Фізика", "Інформатика"},
        ),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"}),
    ]

    # Виклик функції створення розкладу
    schedule, uncovered = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад успішно складено:\n")
        for teacher in schedule:
            print(
                f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}"
            )
            print(f"  Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
        print(f"Залишились непокритими: {', '.join(uncovered)}")
