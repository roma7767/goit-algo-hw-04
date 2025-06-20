def get_cats_info(path):
    try:
        cats = []
        
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat = {'id': parts[0],
                           'name': parts[1],
                           'age': int(parts[2])}
                    cats.append(cat)
        return cats
    except FileNotFoundError:
        print("файл не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []
                           
                           
cats = get_cats_info('cats.txt')
print(cats)                           