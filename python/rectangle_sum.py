# A. Найдите сумму на прямоугольнике
# https://codeforces.com/edu/course/3/lesson/10/3/practice/contest/324368/problem/A

import sys

def main():
    """
    Оптимизированное решение задачи "Найдите сумму на прямоугольнике".
    Основные оптимизации:
    - Не хранит исходную матрицу, сразу строит префиксные суммы
    - Выводит результаты запросов сразу, без накопления
    - Использует быстрый ввод/вывод
    """
    input = sys.stdin
    n, m = map(int, input.readline().split())
    
    # Сразу строим префиксную сумму, не сохраняя исходную матрицу
    prefix = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        row = list(map(int, input.readline().split()))
        for j in range(1, m+1):
            prefix[i][j] = row[j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
    
    q = int(input.readline())
    for _ in range(q):
        lx, ly, rx, ry = map(int, input.readline().split())
        res = prefix[rx][ry] - prefix[lx-1][ry] - prefix[rx][ly-1] + prefix[lx-1][ly-1]
        print(res)

if __name__ == '__main__':
    main()