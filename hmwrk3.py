import numpy as np
import pandas as pd

# 1. Привести различные способы создания объектов типа Series
# Для создания Series можно использовать
# - списки Python или массивы NumPy
# - скалярные значение
# - словари

list_python = pd.Series([1, 2, 3, 4, 5])
# print(list_python)

array_numpy = pd.Series(np.array([1, 2, 3, 4, 5]))
# print(array_numpy)

scalar_values = pd.Series(1)
# print(scalar_values)

dict_ = pd.Series({
    'num1': 1,
    'num2': 2,
    'num3': 3,
    'num4': 4,
    'num5': 5,
})
# print(dict_)

# 2. Привести различные способы создания объектов типа DataFrame
# - через объекты Series
# - списки словарей
# - словари объектов Series
# - двумерный массив NumPy
# - структурированный массив Numpy

# 1
digits = pd.Series([1, 2, 3])
letters = pd.Series(['a', 'b', 'c'])

symbols = pd.DataFrame([digits, letters])
print(symbols)

# 2
result = pd.DataFrame([
    {
        'name': 'Artem',
        'surname': 'Fedorov',
        'age': 27
    },
    {
        'name': 'Michael',
        'surname': 'Perch',
        'age': 63
    }
])
print(result)

# 3
car = pd.Series(['lada', 'renault', 'bmw'])
nums = pd.Series([1, 2, 3])
result = pd.DataFrame({
    'first': car,
    'second': nums
})
print(result)

# 4
numbers = pd.DataFrame([[1, 2], [3, 4], [5, 6]])
print(numbers)

# 5
np_array = np.array([(1, 'a'), (2, 'b'), (3, 'c')], dtype=[('num', 'i4'), ('letter', 'U1')])
result = pd.DataFrame(np_array)
print(result)

# 3. Объедините два объекта Series с неодинаковыми множествами ключей (индексов) так, чтобы вместо NaN было установлено
# значение 1

pop = pd.Series(
    {
        'city_1': 1001,
        'city_2': 1002,
        'city_3': 1003,
        'city_41': 1004,
        'city_51': 1005,
    })

area = pd.Series(
    {
        'city_1': 9991,
        'city_2': 9992,
        'city_3': 9993,
        'city_42': 9994,
        'city_52': 9995,
    })

data = pd.DataFrame({'area1': area, 'pop1': pop}).fillna(1)
print(data)

# 4. Переписать пример с транслированием для DataFrame так, чтобы вычитание происходило по СТОЛБЦАМ

rng = np.random.default_rng(1)

A = rng.integers(0, 10, (3, 4))

df = pd.DataFrame(A, columns=['a', 'b', 'c', 'd'])
print(df)
print(df.iloc[:, 0])
print(df - df.iloc[:, 0].values.reshape(-1, 1))

# 5. На примере объектов DataFrame продемонстрируйте использование методов ffill() и bfill()

df = pd.DataFrame({
    'A': [1, 2, 3, np.nan, np.nan, 6],
    'B': [np.nan, 2, 3, 4, 5, np.nan]
})

print(df.ffill())  # заполняет nan предыдущим перед nan значением, если таковое имеется
print(df.bfill())  # заполняет nan следующим за nan значением, если таковое имеется
