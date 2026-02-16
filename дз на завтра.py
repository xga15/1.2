def find_subarray(arr, sub):
    n = len(arr)
    m = len(sub)
    
    if m > n:
        return -1
    if m == 0:
        return -2
    
    for i in range(n - m + 1):
        found = True
        for j in range(m):
            if arr[i + j] != sub[j]:
                found = False
                break
        if found:
            return i
    return -1

def find_all(arr, sub):
    positions = []
    n = len(arr)
    m = len(sub)
    
    if m > n or m == 0:
        return positions
    
    for i in range(n - m + 1):
        if arr[i:i+m] == sub:
            positions.append(i)
    return positions

def main():
    # Тест 1
    a = [1, 2, 3, 4, 5, 1, 2, 3, 4]
    b = [2, 3, 4]
    
    res = find_subarray(a, b)
    print(f"Массив: {a}")
    print(f"Ищем: {b}")
    
    if res >= 0:
        print(f"Нашли на индексе: {res}")
        print(f"Проверка: {a[res:res+len(b)]}")
    else:
        print("Не нашли")
    
    # Тест 2 - все вхождения
    c = [1, 1, 1, 2, 1, 1, 3]
    d = [1, 1]
    
    all_pos = find_all(c, d)
    print(f"\nМассив: {c}")
    print(f"Ищем: {d}")
    print(f"Все вхождения: {all_pos}")
    
    # Тест 3 - ручной ввод
    print("\nРучной ввод:")
    try:
        inp1 = input("Введите числа через пробел: ")
        inp2 = input("Введите что ищем: ")
        
        arr1 = [int(x) for x in inp1.split()]
        arr2 = [int(x) for x in inp2.split()]
        
        r = find_subarray(arr1, arr2)
        if r >= 0:
            print(f"Индекс: {r}")
        else:
            print("Не найдено")
    except:
        print("Ошибка ввода")

if __name__ == "__main__":
    main()