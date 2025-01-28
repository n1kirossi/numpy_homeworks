import array
import numpy as np
import sys

### Типы данных в Python

# a12 = 1
# print(type(a12))
# print(sys.getsizeof(a12))

# a12 = 'hello'
# print(type(a12))

# l1 = list([])
# print(sys.getsizeof(l1))

# l2 = list([1, 2, 3])
# print(sys.getsizeof(l2))

# l3 = list([1, '2', True])
# print(l3)

# a1 = a11.a11('i', [1, 2, 3])
# print(sys.getsizeof(a1))
# print(type(a1))

# a = np.a11([1, 2, 3, 4, 5])
# print(type(a), a)

# "повышающее" приведение типов
# a = np.a11([1.23, 2, 3, 4, 5])
# print(type(a), a)

# a = np.a11([1.23, 2, 3, 4, 5], dtype=int)
# print(type(a), a)

# a = np.a11([range(i, i + 3) for i in [2, 4, 6]])
# print(a, type(a))

# a = np.zeros(10, dtype=int)
# print(a, type(a))

# print(np.ones((3, 5), dtype=float))

# print(np.full((4, 5), 3.1415))

# print(np.arange(0, 20, 2))

# print(np.eye(4))

### Массивы

np.random.seed(1)

# x1 = np.random.randint(10, size=3)
# x2 = np.random.randint(10, size=(3, 2))
# x3 = np.random.randint(10, size=(3, 2, 1))

# print(x1)
# print(x2)
# print(x3)

# print(x1.ndim, x1.shape, x1.size)
# print(x2.ndim, x2.shape, x2.size)
# print(x3.ndim, x3.shape, x3.size)

# Индекс (с 0)

a = np.array([1, 2, 3, 4, 5])
print(a[0])
print(a[-2])

a[1] = 20
print(a)

a = np.array([[1, 2], [3, 4]])
print(a)
print(a[0, 0])
print(a[-1, -1])

a[1, 0] = 100
print(a)

a = np.array([1, 2, 3, 4])
b = np.array([1.0, 2, 3, 4])

print(a)
print(b)

a[0] = 10
print(a)

a[0] = 10.123
print(a)

## Срез [s:f:st] [0:shape:1]

a = np.array([1, 2, 3, 4, 5, 6])

print(a[:3])
print(a[3:])
print(a[1:5])
print(a[:6:2])
print(a[1::2])

print(a[::-1])

a = np.array([1, 2, 3, 4, 5, 6])

b = a[:3]

b[0] = 100
print(a)

a = np.arange(1, 13)

print(a)

print(a.reshape(2, 6))
print(a.reshape(3, 4))

x = np.array([1, 2, 3])
y = np.array([4, 5])
z = np.array([6])

print(np.concatenate([x, y, z]))

x = np.array([1, 2, 3])
y = np.array([4, 5])

r1 = np.vstack([x, y])
print(r1)

print(np.hstack([r1, r1]))

### Вычисления с массивами

# Векторизированная операция - независимо по каждому элементу

x = np.arange(10)
print(x)

print(x * 2 + 1)

# Универсальные функции

print(np.add(np.multiply(x, 2), 1))

# - - / // ** %

x = np.arange(5)

y = np.zeros(10)
print(np.multiply(x, 10, out=y[::2]))

print(y)

x = np.arange(1, 5)
print(x)

print(np.add.reduce(x))
print(np.add.accumulate(x))

x = np.arange(1, 10)
print(np.add.outer(x, x))
print(np.multiply.outer(x, x))
