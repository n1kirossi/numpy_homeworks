import numpy as np


# 1. Что надо изменить в последнем примере, чтобы он заработал без ошибок (транслирование)?

a = np.ones((3, 2))
b = np.arange(3)

c = a + b[:, np.newaxis]
print(c)

# или

a = np.ones((3, 2))
b = np.arange(3).reshape(3, 1)

c = a + b
print(c)

# 2. Пример для y. Вычислить количество элементов (по обеим размерностям), значения которых больше 3 и меньше 9

y = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

conditions = np.logical_and(y > 3, y < 9)

print(np.sum(conditions, axis=0))
print(np.sum(conditions, axis=1))

# или

print(np.sum(conditions, axis=0).sum())
print(np.sum(conditions, axis=1).sum())
