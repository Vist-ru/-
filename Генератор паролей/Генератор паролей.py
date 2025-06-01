import random

# Приветствие пользователя и инструкции
print("Я генератор паролей! Могу создавать пароли из букв, чисел, а также из чисел и букв.")
print("Если хотите завершить работу, то напишите 'Нет'")
print("Если хотите продолжить, напишите 'Да'")

# Начальная переменная для управления циклом
f = input()

# Функция для вывода сгенерированного пароля
def k():
    print(*z, sep = "")

# Главный цикл программы
while f != "Нет":
    # Запрос на выбор типа пароля
    print("Выберите, какой пароль хотите сгенерировать!")
    print("1. Из букв.(Аа)")
    print("2. Из букв.(А)")
    print("3. Из букв.(а)")
    print("4. Из чисел.")
    print("5. Из чисел и букв.(Аа)")
    print("6. Из чисел и букв.(А)")
    print("7. Из чисел и букв.(а)")
    print("8. Из чисел и англ. букв.(Bb)")
    print("9. Из чисел и англ. букв.(B)")
    print("10. Из чисел и англ. букв.(b)")
    print("11. Из англ. букв.(Bb)")
    print("12. Из англ. букв.(B)")
    print("13. Из англ. букв.(b)")
    print("14. СУПЕР ПАРОЛЬ")

    # Считываем выбор пользователя
    print("Напишите число, под которым расположен выбранный вами вариант.")
    # Количество символов в пароле
    x = int(input())
    y = int(input())

    # Список для хранения символов пароля
    z = list()

    # Генерация паролей в зависимости от выбора
    if x == 1:
        # Генерация пароля из всех букв (и заглавных, и строчных)
        for _ in range(y):
            z.append(random.choice("АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя"))
        k()
    
    if x == 2:
        # Генерация пароля из заглавных букв
        for _ in range(y):
            z.append(random.choice("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"))
        k()
    
    if x == 3:
        # Генерация пароля из строчных букв
        for _ in range(y):
            z.append(random.choice("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"))
        k()
    
    if x == 4:
        # Генерация пароля из чисел
        for _ in range(y):
            z.append(random.randrange(0, 10))
        k()
    
    if x == 5:
        # Генерация пароля из чисел и букв
        for _ in range(y):
            x = random.randrange(1, 3)
            if x == 1:
                z.append(random.choice("АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя"))
            if x == 2:
                z.append(random.randrange(0, 10))
        k()
    
    if x == 6:
        # Генерация пароля из заглавных букв и чисел
        for _ in range(y):
            x = random.randrange(1, 3)
            if x == 1:
                z.append(random.choice("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"))
            if x == 2:
                z.append(random.randrange(0, 10))
        k()
    
    if x == 7:
        # Генерация пароля из строчных букв и чисел
        for _ in range(y):
            x = random.randrange(1, 3)
            if x == 1:
                z.append(random.choice("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"))
            if x == 2:
                z.append(random.randrange(0, 10))
        k()
    
    if x == 8:
        # Генерация пароля из английских букв и чисел
        for _ in range(y):
            x = random.randrange(1, 3)
            if x == 1:
                z.append(random.choice("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"))
            if x == 2:
                z.append(random.randrange(0, 10))
        k()

    if x == 9:
        # Генерация пароля из заглавных английских букв и чисел
        for _ in range(y):
            x = random.randrange(1, 3)
            if x == 1:
                z.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
            if x == 2:
                z.append(random.randrange(0, 10))
        k()

    if x == 10:
        # Генерация пароля из строчных английских букв и чисел
        for _ in range(y):
            x = random.randrange(1, 3)
            if x == 1:
                z.append(random.choice("abcdefghijklmnopqrstuvwxyz"))
            if x == 2:
                z.append(random.randrange(0, 10))
        k()

    if x == 11:
        # Генерация пароля только из английских букв
        for _ in range(y):
            z.append(random.choice("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"))
        k()
    
    if x == 12:
        # Генерация пароля только из заглавных английских букв
        for _ in range(y):
            z.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        k()
    
    if x == 13:
        # Генерация пароля только из строчных английских букв
        for _ in range(y):
            z.append(random.choice("abcdefghijklmnopqrstuvwxyz"))
        k()
    
    if x == 14:
        # Супер пароль с разнообразными символами
        g = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
        x = random.sample(g, 7)
        for _ in range(y):
            x = random.randrange(1, 8)
            if x == 1:
                z.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
            if x == 2:
                z.append(random.randrange(0, 10))
            if x == 3:
                z.append(x)
            if x == 4:
                z.append(random.randrange(0, 99, 7))
            if x == 5:
                z.append(random.choice("abcdefghijklmnopqrstuvwxyz"))
            if x == 6:
                z.append(random.choice("!~@#$%^&*'"))
            if x == 7:
                z.append(random.choice("!~@#$%^&*'"))
        k()
    
    # Запрос на продолжение или завершение работы
    print("Если хотите закончить работу, то напишите 'Нет'.")
    print("Если хотите продолжить, напишите 'Да'")
    f = input()