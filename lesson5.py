# питоновские программы можно запускать в разных программах
# 1. сценарий
# 2. командная оболочка iPython
# 3. Jupyter

# 1
# plt.show() - запускается только один раз
# В процессе работы создаются Figure. Они ищутся

import matplotlib.pyplot as plt
import numpy as np


# x = np.linspace(0, 10, 100)
#
# fig = plt.figure()
# plt.plot(x, np.sin(x))
# plt.plot(x, np.cos(x))
#
# plt.show()

# IPython
# %matplotlib
# import matplotlib.pyplot as plt
# plt.plot(...)
# plt.draw()
# plt.show() не нужно

# 3
# %matplotlib inline - в блокнот добавляется статическая картинка
# %matplotlib notebook - графики будут интерактивные

# fig.savefig('save_images.png')

# print(fig.canvas.get_supported_filetypes())

# два способа вывода графиков
# - Matlab-подобный стиль
# - в ОО стиле

# 1

# x = np.linspace(0, 10, 100)

# plt.figure()
#
# plt.subplot(2, 1, 1)
# plt.plot(x, np.sin(x))
#
# plt.subplot(2, 1, 2)
# plt.plot(x, np.cos(x))
#
# plt.show()

# 2
# fig: Figure, ax: Axes
# fig, ax = plt.subplots(2)
#
# ax[0].plot(x, np.sin(x))
# ax[1].plot(x, np.sin(x))

# fig: plt.Figure - контейнер, содержит объекты (СК, тексты, метки), ax: Axes - система координат (СК),
# прямоугольник, деления, метки

# Цвета линий color
# - 'blue'
# - 'rgbcmyk' -> 'rg'
# - '0.14' - градация серого от 0 до 1
# - RRGGBB - '#FF00EE'
# - HTML - 'salmon'

# СТили линии linestyle
# - сплошная '-', 'solid'
# - штриховая '--', 'dashed'
# - штрихпунктирная '-.', 'dashdot'
# - пунктирная ':', 'dotted'

# fig = plt.figure()
# ax = plt.axes()
#
# ax.plot(x, np.sin(x), color='blue')
# ax.plot(x, np.sin(x - 1), c='g', linestyle='solid')
# ax.plot(x, np.sin(x - 2), c='0.75', linestyle='dashed')
# ax.plot(x, np.sin(x - 3), c='#FF00EE', linestyle='dashdot')
# ax.plot(x, np.sin(x - 4), c='(1.0, 0.2, 0.3', linestyle='dotted')
# ax.plot(x, np.sin(x - 5), c='salmon')
# ax.plot(x, np.sin(x - 6), '--b')

# fig, ax = plt.subplots(4)
#
# ax[0].plot(x, np.sin(x))
# ax[1].plot(x, np.sin(x))
# ax[2].plot(x, np.sin(x))
# ax[3].plot(x, np.sin(x))
#
# ax[1].set_xlim(-2, 12)
# ax[1].set_ylim(-1.5, 1.5)
#
# ax[1].set_xlim(12, -2)
# ax[1].set_ylim(1.5, -1.5)
#
# ax[1].autoscale(tight=True)

# plt.subplot(3, 1, 1)
# plt.plot(x, np.sin(x))
#
# plt.title('Синус')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
#
# plt.subplot(3, 1, 2)
# plt.plot(x, np.sin(x), '-g', label='sin(x)')
# plt.plot(x, np.cos(x), ':b', label='cos(x)')
#
# plt.title('Синус и косинус')
# plt.xlabel('x')
# plt.legend()
#
# plt.subplot(3, 1, 3)
#
# plt.plot(x, np.sin(x), '-g', label='sin(x)')
# plt.plot(x, np.cos(x), ':b', label='cos(x)')
#
# plt.title('Синус и косинус')
# plt.xlabel('x')
# plt.axis('equal')
#
# plt.legend()
#
# plt.subplots_adjust(hspace=0.5)

# x = np.linspace(0, 10, 100)
# plt.plot(x, np.sin(x), 'o', color='green')
# plt.plot(x, np.sin(x + 1), '>', color='green')
# plt.plot(x, np.sin(x + 2), '^', color='green')
# plt.plot(x, np.sin(x + 3), 's', color='green')

# x = np.linspace(0, 10, 30)
# plt.plot(x, np.sin(x), markersize=15, linewidth=4, makerfacecolor='white', markeredgecolor='gray', markeredgewidth=2)

# rng = np.random.default_rng(0)
#
# colors = rng.random(30)
# sizes = 100 * rng.random(30)
#
# plt.scatter(x, np.sin(x), marker='o', c=colors)
# plt.colorbar()

# Если точек больше 1000б от plot предпочтительнее из-за производительности

# Визуализация погрешностей

# x = np.linspace(0, 10, 30)
#
# dy = 0.4
# y = np.sin(x) + dy * np.random.randn(30)
#
# plt.errorbar(x, y, yerr=dy, fmt='.k')
# plt.fill_between(x, y - dy, y + dy, color='red', alpha=0.4)

def f(x, y):
    return np.sin(x) ** 5 + np.cos(20 + x * y) * np.cos(x)


x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)
X, Y = np.meshgrid(x, y)

Z = f(X, Y)

# plt.contour(X, Y, Z, cmap='RdGy')
# plt.contourf(X, Y, Z, cmap='RdGy')

c = plt.contour(X, Y, Z, color='red')
plt.clabel(c)
plt.imshow(Z, extend=[0, 5, 0, 5], cmap='RdGy', interpolation='gaussian', origin='lower')
plt.colorbar()

plt.show()
