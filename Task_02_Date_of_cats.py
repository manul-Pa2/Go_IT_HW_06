def get_cats_info(path: str) -> list[dict]:
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()            # Чистимо пробіли
                if not line:             # Мінусуємо порожні рядки
                    continue

                parts = line.split(",")    # Розбивка
                if len(parts) != 3:        
                    continue

                cat_id, name, age = parts

                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }

                cats.append(cat_info)

    except OSError:     # Обробка помилки файлу
        return []

    return cats

cats_info = get_cats_info("cats_file.txt")  # Виклик\тестування

print(cats_info)

