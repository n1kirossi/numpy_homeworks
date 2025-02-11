import array
import sys
import numpy as np


# 1. Какие еще существуют коды типов?

"""
'b' - знаковый символ (целое число от -128 до 127)
'B' - беззнаковый символ (целое число от 0 до 255)
'h' - знаковое короткое целое (целое число от -32768 до 32767)
'H' - беззнаковое короткое целое (целое число от 0 до 65535)
'i' - знаковое целое (целое число от -2147483648 до 2147483647)
'I' - беззнаковое целое (целое число от 0 до 4294967295)
'q' - знаковое очень длинное целое (целое число от -9223372036854775808 до 9223372036854775807)
'Q' - беззнаковое очень длинное целое (целое число от 0 до 18446744073709551615)
'f' - число с плавающей запятой (одинарной точности)
'd' - число с двойной точностью (двойной точности)
"""

# 2. Напишите код, подобный приведенному выше, но с другим типом

a2 = array.array('H', [1, 2, 3, 4])
print(a2)

# 3. Напишите код для создания массива с 5 значениями, располагающимися через равные интервалы в диапазоне от 0 до 1

a3 = np.linspace(0, 1, 5)
print(a3)

# 4. Напишите код для создания массива с 5 равномерно распределенными случайными значениями в диапазоне от 0 до 1

np.random.seed(1)
a4 = np.random.rand(5)
print(a4)

# 5. Напишите код для создания массива с 5 нормально распределенными случайными значениями с мат. ожиданием = 0
# и дисперсией 1

a5 = np.random.normal(0, 1, 5)
print(a5)

# 6. Напишите код для создания массива с 5 случайными целыми числами в диапазоне [0, 10)

a6 = np.random.randint(0, 10, 5)
print(a6)

# 7. Написать код для создания срезов массива 3 на 4
# - первые две строки и три столбца
# - первые три строки и второй столбец
# - все строки и столбцы в обратном порядке
# - второй столбец
# - третья строка

a7 = np.array([range(i, i + 4) for i in [2, 4, 6]])
print(a7)
print(a7[:2, :3])
print(a7[:, 1])
print(a7[::-1, ::-1])
print(a7[:, 1])
print(a7[2])

# 8. Продемонстрируйте, как сделать срез-копию

a8 = a7[:2, 2].copy()
print(a8)

# 9. Продемонстрируйте использование newaxis для получения вектора-столбца и вектора-строки

a9 = np.array([1, 2, 3, 4])
print(a9[np.newaxis, :])
a91 = np.array([1, 2, 3, 4])
print(a91[:, np.newaxis])

# 10. Разберитесь, как работает метод dstack

a10 = np.array([[1, 2], [3, 4]])
a101 = np.array([[5, 6], [7, 8]])
a102 = np.array([[9, 10], [11, 12]])

print(np.dstack((a10, a101, a102)))

# 11. Разберитесь, как работают методы split, vsplit, hsplit, dsplit

a11 = np.array([1, 2, 3, 4, 5, 6])
print(np.split(a11, 3))
a111 = np.array([[1, 2], [3, 4], [5, 6]])
print(np.vsplit(a111, 3))
a112 = np.array([[1, 2, 3], [4, 5, 6]])
print(np.hsplit(a112, 3))

a113 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(np.dsplit(a113, 2))

# 12. Привести пример использования всех универсальных функций, которые я привел

a12 = np.array([1, 2, 3, 4, 5])

print(np.subtract(a12, 1))
print(np.divide(a12, 2))
print(np.floor_divide(a12, 2))
print(np.power(a12, 2))
print(np.mod(a12, 2))