try:
    with open('text.txt', 'r', encoding='utf-8') as file:
        print(file.read())
        # этот метод сам открывает и закрывает файл (with и as)
except FileNotFoundError:
    print("Файл не найден")