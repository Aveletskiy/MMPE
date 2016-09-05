#!/usr/bin/python
# coding: utf8

import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# читаем данные
data = sp.genfromtxt("data.tsv", delimiter="\t")
# print(data[:10]) # часть данных можно напечатать, чтобы убедиться, что всё в порядке

# берём срезы: первую и вторую колонку нашего файла
x = data[:, 0]
y = data[:, 1]

# настраиваем детали отрисовки графиков
plt.figure(figsize=(10, 8))
plt.title("Installations")
plt.xlabel("Days")
plt.ylabel("Installations")
# plt.xticks([...], [...]) # можно назначить свои тики
plt.autoscale(tight=True)

# рисуем исходные точки
plt.scatter(x, y)

legend = []
# аргументы для построения графиков моделей: исходный интервал + 60 дней
fx = sp.linspace(0, 100)
for d in range(1, 4):
    # получаем параметры модели для полинома степени d
    fp, residuals, rank, sv, rcond = sp.polyfit(x, y, d, full=True)
    # print("Параметры модели: %s" % fp1)
    # функция-полином, если её напечатать, то увидите математическое выражение
    f = sp.poly1d(fp)
    print(f)
    # рисуем график модельной функции
    plt.plot(fx, f(fx), linewidth=2)
    legend.append("d=%i" % f.order)
    f2 = f - 1000  # из полинома можно вычитать
    t = fsolve(f2, x[-1])  # ищем решение уравнения f2(x)=0, отплясывая от точки x[-1]
    # print("Полином %d-й степени:" % f.order)
    # print("- Мы достигнем 1000 установок через %d дней" % (t[0] - x[-1]))
    # print("- Через 60 дней у нас будет %d установок" % f(x[-1] + 60))

plt.legend(legend, bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=1, mode="expand", borderaxespad=0.)
plt.grid()
# plt.savefig('data.png', dpi=50)
plt.show()
