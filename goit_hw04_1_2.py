def total_salary(path):
    try:
        total = 0.0
        count = 0
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    try:
                        salary = float(parts[1])
                        total += salary
                        count += 1
                    except ValueError:
                        print(f"неможливо перетворити '{parts[1]}' на число.")    
        if count == 0:
            print("Немає поточного запису із зарплатою.")
            return 0.0, 0.0
            
        average = total / count
        return total, average
        
    except FileNotFoundError:
        print("Файл не знайдено.")  
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")      
        
        
total, average = total_salary('salaries.txt')
print(f"Загальна сума: {total}, Середня зарплата: {average}")
