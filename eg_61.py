# -*- coding:utf-8 -*-
# 题目：打印出杨辉三角形（要求打印出10行）
a = []
for i in range(10):
    a.append([])
    for j in range(10):
        a[i].append(0)
for i in range(10):
    a[i][0] = 1
    a[i][i] = 1
for j in range(2, 10):
    for k in range(1, j):
        a[j][k] = a[j-1][k-1]+a[j-1][k]
for i in range(10):
    for j in range(i + 1):
        print(str(a[i][j]), end=' ')
    print()