def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]

        salaries = []
        for line in lines:
            try:
                _, salary = line.split(',')
                salaries.append(float(salary))
            except ValueError:
                continue  # пропускаємо рядки з помилками формату

        if not salaries:
            return 0, 0

        total = sum(salaries)
        average = total / len(salaries)
        return total, round(average, 2)

    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return 0, 0


def main():
    print("Аналіз заробітних плат розробників\n")
    path = input("Вкажіть шлях до файлу із зарплатами: ").strip()

    total, average = total_salary(path)

    if total == 0 and average == 0:
        print("Обробку завершено — можливо, файл порожній або некоректний.")
    else:
        print(f"\nЗагальна сума заробітної плати: {total}")
        print(f"Середня заробітна плата: {average}")


if __name__ == '__main__':
    main()
