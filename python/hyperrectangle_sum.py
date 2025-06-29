# -*- coding: utf-8 -*-
# https://codeforces.com/edu/course/3/lesson/10/3/practice/contest/324368/problem/B

import sys

def main():
    """
    Решение задачи "Найдите сумму в 5D" с использованием 5D префиксных сумм.

    Алгоритм:
    1. Считывает пятимерный массив заданных размерностей n1×n2×n3×n4×n5
    2. Строит массив префиксных сумм в 5D пространстве, используя принцип включения-исключения
    3. Обрабатывает запросы, вычисляя сумму на гиперпрямоугольнике за O(1) на запрос
    4. Выводит результаты всех запросов

    Исправления:
    - Исправлен знак в формуле включения-исключения при вычислении суммы
    - Упрощена логика обработки масок
    """
    input = sys.stdin.read().split()
    ptr = 0
    n1, n2, n3, n4, n5 = map(int, input[ptr:ptr+5])
    ptr += 5

    # Инициализация 5D массива
    size = n1 * n2 * n3 * n4 * n5
    a = [0] * size

    # Функция для преобразования 5D индексов в 1D
    def get_idx(i1, i2, i3, i4, i5):
        return (((i1 * n2 + i2) * n3 + i3) * n4 + i4) * n5 + i5

    # Чтение элементов массива
    for i1 in range(n1):
        for i2 in range(n2):
            for i3 in range(n3):
                for i4 in range(n4):
                    elements = list(map(int, input[ptr:ptr+n5]))
                    ptr += n5
                    for i5 in range(n5):
                        a[get_idx(i1, i2, i3, i4, i5)] = elements[i5]

    # Построение префиксных сумм
    prefix = [0] * ((n1+1)*(n2+1)*(n3+1)*(n4+1)*(n5+1))
    
    def get_prefix_idx(i1, i2, i3, i4, i5):
        return (((i1 * (n2+1) + i2) * (n3+1) + i3) * (n4+1) + i4) * (n5+1) + i5

    for i1 in range(1, n1+1):
        for i2 in range(1, n2+1):
            for i3 in range(1, n3+1):
                for i4 in range(1, n4+1):
                    for i5 in range(1, n5+1):
                        idx = get_prefix_idx(i1, i2, i3, i4, i5)
                        val = a[get_idx(i1-1, i2-1, i3-1, i4-1, i5-1)]
                        prefix[idx] = (val + prefix[get_prefix_idx(i1-1, i2, i3, i4, i5)] +
                                     prefix[get_prefix_idx(i1, i2-1, i3, i4, i5)] +
                                     prefix[get_prefix_idx(i1, i2, i3-1, i4, i5)] +
                                     prefix[get_prefix_idx(i1, i2, i3, i4-1, i5)] +
                                     prefix[get_prefix_idx(i1, i2, i3, i4, i5-1)] -
                                     prefix[get_prefix_idx(i1-1, i2-1, i3, i4, i5)] -
                                     prefix[get_prefix_idx(i1-1, i2, i3-1, i4, i5)] -
                                     prefix[get_prefix_idx(i1-1, i2, i3, i4-1, i5)] -
                                     prefix[get_prefix_idx(i1-1, i2, i3, i4, i5-1)] -
                                     prefix[get_prefix_idx(i1, i2-1, i3-1, i4, i5)] -
                                     prefix[get_prefix_idx(i1, i2-1, i3, i4-1, i5)] -
                                     prefix[get_prefix_idx(i1, i2-1, i3, i4, i5-1)] -
                                     prefix[get_prefix_idx(i1, i2, i3-1, i4-1, i5)] -
                                     prefix[get_prefix_idx(i1, i2, i3-1, i4, i5-1)] -
                                     prefix[get_prefix_idx(i1, i2, i3, i4-1, i5-1)] +
                                     prefix[get_prefix_idx(i1-1, i2-1, i3-1, i4, i5)] +
                                     prefix[get_prefix_idx(i1-1, i2-1, i3, i4-1, i5)] +
                                     prefix[get_prefix_idx(i1-1, i2-1, i3, i4, i5-1)] +
                                     prefix[get_prefix_idx(i1-1, i2, i3-1, i4-1, i5)] +
                                     prefix[get_prefix_idx(i1-1, i2, i3-1, i4, i5-1)] +
                                     prefix[get_prefix_idx(i1-1, i2, i3, i4-1, i5-1)] +
                                     prefix[get_prefix_idx(i1, i2-1, i3-1, i4-1, i5)] +
                                     prefix[get_prefix_idx(i1, i2-1, i3-1, i4, i5-1)] +
                                     prefix[get_prefix_idx(i1, i2-1, i3, i4-1, i5-1)] +
                                     prefix[get_prefix_idx(i1, i2, i3-1, i4-1, i5-1)] -
                                     prefix[get_prefix_idx(i1-1, i2-1, i3-1, i4-1, i5)] -
                                     prefix[get_prefix_idx(i1-1, i2-1, i3-1, i4, i5-1)] -
                                     prefix[get_prefix_idx(i1-1, i2-1, i3, i4-1, i5-1)] -
                                     prefix[get_prefix_idx(i1-1, i2, i3-1, i4-1, i5-1)] -
                                     prefix[get_prefix_idx(i1, i2-1, i3-1, i4-1, i5-1)] +
                                     prefix[get_prefix_idx(i1-1, i2-1, i3-1, i4-1, i5-1)])
    
    # Обработка запросов
    q = int(input[ptr])
    ptr += 1
    output = []
    for _ in range(q):
        coords = list(map(int, input[ptr:ptr+10]))
        ptr += 10
        l1, l2, l3, l4, l5 = coords[0], coords[1], coords[2], coords[3], coords[4]
        r1, r2, r3, r4, r5 = coords[5], coords[6], coords[7], coords[8], coords[9]
        
        # Вычисление суммы по принципу включения-исключения
        sum_val = (prefix[get_prefix_idx(r1, r2, r3, r4, r5)] -
                  prefix[get_prefix_idx(l1-1, r2, r3, r4, r5)] -
                  prefix[get_prefix_idx(r1, l2-1, r3, r4, r5)] -
                  prefix[get_prefix_idx(r1, r2, l3-1, r4, r5)] -
                  prefix[get_prefix_idx(r1, r2, r3, l4-1, r5)] -
                  prefix[get_prefix_idx(r1, r2, r3, r4, l5-1)] +
                  prefix[get_prefix_idx(l1-1, l2-1, r3, r4, r5)] +
                  prefix[get_prefix_idx(l1-1, r2, l3-1, r4, r5)] +
                  prefix[get_prefix_idx(l1-1, r2, r3, l4-1, r5)] +
                  prefix[get_prefix_idx(l1-1, r2, r3, r4, l5-1)] +
                  prefix[get_prefix_idx(r1, l2-1, l3-1, r4, r5)] +
                  prefix[get_prefix_idx(r1, l2-1, r3, l4-1, r5)] +
                  prefix[get_prefix_idx(r1, l2-1, r3, r4, l5-1)] +
                  prefix[get_prefix_idx(r1, r2, l3-1, l4-1, r5)] +
                  prefix[get_prefix_idx(r1, r2, l3-1, r4, l5-1)] +
                  prefix[get_prefix_idx(r1, r2, r3, l4-1, l5-1)] -
                  prefix[get_prefix_idx(l1-1, l2-1, l3-1, r4, r5)] -
                  prefix[get_prefix_idx(l1-1, l2-1, r3, l4-1, r5)] -
                  prefix[get_prefix_idx(l1-1, l2-1, r3, r4, l5-1)] -
                  prefix[get_prefix_idx(l1-1, r2, l3-1, l4-1, r5)] -
                  prefix[get_prefix_idx(l1-1, r2, l3-1, r4, l5-1)] -
                  prefix[get_prefix_idx(l1-1, r2, r3, l4-1, l5-1)] -
                  prefix[get_prefix_idx(r1, l2-1, l3-1, l4-1, r5)] -
                  prefix[get_prefix_idx(r1, l2-1, l3-1, r4, l5-1)] -
                  prefix[get_prefix_idx(r1, l2-1, r3, l4-1, l5-1)] -
                  prefix[get_prefix_idx(r1, r2, l3-1, l4-1, l5-1)] +
                  prefix[get_prefix_idx(l1-1, l2-1, l3-1, l4-1, r5)] +
                  prefix[get_prefix_idx(l1-1, l2-1, l3-1, r4, l5-1)] +
                  prefix[get_prefix_idx(l1-1, l2-1, r3, l4-1, l5-1)] +
                  prefix[get_prefix_idx(l1-1, r2, l3-1, l4-1, l5-1)] +
                  prefix[get_prefix_idx(r1, l2-1, l3-1, l4-1, l5-1)] -
                  prefix[get_prefix_idx(l1-1, l2-1, l3-1, l4-1, l5-1)])
        output.append(str(sum_val))
    
    print('\n'.join(output))

if __name__ == '__main__':
    main()
