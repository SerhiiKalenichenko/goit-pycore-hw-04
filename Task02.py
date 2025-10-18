def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]

        for line in lines:
            try:
                cat_id, name, age = line.split(',')
                cats.append({"id": cat_id, "name": name, "age": age})
            except ValueError:
                continue  # пропускаємо некоректні рядки

        return cats

    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return []


def main():
    print("Інформація про котів\n")
    path = input("Вкажіть шлях до файлу з даними про котів: ").strip()

    cats_info = get_cats_info(path)

    if not cats_info:
        print("Дані відсутні або файл нечитабельний.")
    else:
        print("\nОтримана інформація про котів:")
        for cat in cats_info:
            print(f"id: {cat['id']}, name: {cat['name']}, age: {cat['age']}")


if __name__ == '__main__':
    main()
