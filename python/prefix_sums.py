# -*- coding: utf-8 -*-
# Построение префиксных сумм
# https://codeforces.com/edu/course/3/lesson/10/1/practice/contest/324365/problem/A

import sys

def main():
    """
    Решение задачи "Построение префиксных сумм".
    
    Алгоритм:
    1. Считываем массив чисел
    2. Строим массив префиксных сумм, где каждый элемент равен сумме всех предыдущих
    3. Выводим результат, начиная с 0
    
    Сложность: O(n) по времени и памяти
    """
    input = sys.stdin.read().split()
    n = int(input[0])
    a = list(map(int, input[1:n+1]))
    
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + a[i - 1]
    
    print(' '.join(map(str, prefix)))

if __name__ == '__main__':
    main()