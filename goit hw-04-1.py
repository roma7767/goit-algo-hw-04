def total_salary(path):
    try:
        total = 0
        count = 0
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2 and parts[1].isdigit():
                    total += int(parts[1])
                    count += 1
            average = total // count if count > 0 else 0
            return total, average
        
    except FileNotFoundError:
        print("Файл не знайдено.")  
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")      
        
        
total, average = total_salary('salaries.txt')
print(f"Загальна сума: {total}, Середня зарплата: {average}")