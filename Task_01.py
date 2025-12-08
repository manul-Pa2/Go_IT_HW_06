def total_salary(path: str) -> tuple:
    total = 0
    count = 0

    try:                     # Відкриваємо файл з правильним кодуванням
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:           # пропускаємо порожні рядки
                    continue

                try:
                    name, salary_str = line.split(",")
                    salary = int(salary_str)
                
                except ValueError:       # Якщо рядок пошкоджений або зарплата не число
                    continue

                total += salary
                count += 1

    except FileNotFoundError:      # Повертає 0 якщо файлів немає
        return 0, 0

    if count == 0:      # Запису немає
        return 0, 0

    average = total / count
    return total, average

#Test:
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
