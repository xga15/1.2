# Лабораторная работа по поиску подмассива
# Сделал: Студент группы ИВТ-123
# Дата: 2024

def poisk_vhodov(osnovnoy, podmassiv):
    """
    Функция ищет входит ли подмассив в основной массив
    Возвращает индекс или -1
    """
    dlina_osn = len(osnovnoy)
    dlina_pod = len(podmassiv)
    
    # Проверка на пустой подмассив
    if dlina_pod == 0:
        print("Подмассив пустой!")
        return -1
    
    # Проверка если подмассив больше основного
    if dlina_pod > dlina_osn:
        print("Подмассив больше основного массива!")
        return -1
    
    # Перебираем все возможные позиции
    for i in range(dlina_osn - dlina_pod + 1):
        sovpadenie = True
        
        # Проверяем каждый элемент
        for j in range(dlina_pod):
            if osnovnoy[i + j] != podmassiv[j]:
                sovpadenie = False
                break
        
        if sovpadenie == True:
            return i
    
    return -1

def vyvod_rezultata(indeks, osnovnoy, podmassiv):
    """Выводит результат поиска красиво"""
    if indeks == -1:
        print("Ничего не найдено :(")
    else:
        print(f"Ура! Нашли на позиции {indeks}")
        print(f"Основной массив: {osnovnoy}")
        print(f"Искомый кусок:   {podmassiv}")
        # Рисуем стрелочку
        stroka = " " * (indeks * 3 + 2) + "^"
        print(stroka)

# Основная программа
def main():
    print("=" * 50)
    print("ПРОГРАММА ПОИСКА ПОДМАССИВА")
    print("=" * 50)
    
    # Создаем тестовые данные
    arr1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    arr2 = [2, 3, 4]
    arr3 = [5, 5, 5]
    arr4 = [1, 2, 3]
    arr5 = []  # Пустой для проверки
    
    # Тестируем
    print("\nТест 1: Ищем [2,3,4] в массиве")
    rez = poisk_vhodov(arr1, arr2)
    vyvod_rezultata(rez, arr1, arr2)
    
    print("\nТест 2: Ищем [5,5,5] в массиве")
    rez = poisk_vhodov(arr1, arr3)
    vyvod_rezultata(rez, arr1, arr3)
    
    print("\nТест 3: Ищем пустой массив")
    rez = poisk_vhodov(arr1, arr5)
    vyvod_rezultata(rez, arr1, arr5)
    
    print("\nТест 4: Ищем [1,2,3] (должно найти 2 раза)")
    rez1 = poisk_vhodov(arr1, arr4)
    vyvod_rezultata(rez1, arr1, arr4)
    
    # А теперь ручной ввод
    print("\n" + "=" * 50)
    print("РУЧНОЙ ВВОД")
    print("=" * 50)
    
    try:
        # Ввод основного массива
        vvod = input("Введите числа через пробел для основного массива: ")
        chisla = vvod.split()
        osnovnoy = []
        for x in chisla:
            osnovnoy.append(int(x))
        
        # Ввод подмассива
        vvod2 = input("Введите числа через пробел для подмассива: ")
        chisla2 = vvod2.split()
        podmassiv = []
        for x in chisla2:
            podmassiv.append(int(x))
        
        print("\nИщем...")
        rezultat = poisk_vhodov(osnovnoy, podmassiv)
        
        if rezultat != -1:
            print(f"Нашли на индексе {rezultat}!")
            # Показываем найденный кусок
            naydeno = osnovnoy[rezultat:rezultat + len(podmassiv)]
            print(f"Нашли: {naydeno}")
        else:
            print("Не нашли :(")
            
    except:
        print("Ошибка! Наверное ввели не числа...")

# Дополнительная функция для домашки
def poisk_vseh_vhodov(osnovnoy, podmassiv):
    """Ищет все позиции где встречается подмассив"""
    pozicii = []
    
    for i in range(len(osnovnoy) - len(podmassiv) + 1):
        if osnovnoy[i:i+len(podmassiv)] == podmassiv:
            pozicii.append(i)
    
    return pozicii

# Запускаем программу
if __name__ == "__main__":
    main()
    
    # Дополнительный тест
    print("\n" + "=" * 50)
    print("ДОПОЛНИТЕЛЬНЫЙ ТЕСТ")
    print("=" * 50)
    
    test_arr = [1, 1, 1, 1, 2, 1, 1, 3]
    test_pod = [1, 1]
    
    vse = poisk_vseh_vhodov(test_arr, test_pod)
    print(f"Массив {test_arr}")
    print(f"Ищем {test_pod}")
    print(f"Нашли на позициях: {vse}")
    print(f"Всего вхождений: {len(vse)}")