import sys

def main():
    """
    Решение задачи 'Найдите XOR на отрезке' с использованием префиксных XOR.

    Алгоритм:
    1. Считываем массив чисел.
    2. Строим массив префиксных XOR.
    3. Для каждого запроса вычисляем XOR на отрезке как XOR префиксных XOR.
    4. Выводим результаты запросов.

    Особенности:
    - Используется O(n) памяти для хранения префиксных XOR.
    - Каждый запрос обрабатывается за O(1) время после предварительной обработки.
    - Оптимизированное чтение входных данных и вывод результатов.
    """
    input = sys.stdin
    n = int(input.readline())
    a = list(map(int, input.readline().split()))
    
    # Построение массива префиксных XOR
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] ^ a[i - 1]
    
    q = int(input.readline())
    for _ in range(q):
        l, r = map(int, input.readline().split())
        # Вычисление XOR на отрезке [l, r]
        res = prefix[r] ^ prefix[l - 1]
        print(res)

if __name__ == '__main__':
    main()
