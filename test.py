import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from textwrap import wrap

levels = 256
maxVoltage = 3.3

voltagelist = np.loadtxt('data.txt', dtype=int)
voltagelist = voltagelist * maxVoltage/levels

with open('settings.txt', 'r') as f:
    T = float(f.readline())

timelist = np.arange(0, len(voltagelist), 1)
timelist = timelist * T
t1 = timelist[np.argmax(voltagelist)]
t2 = timelist[-1]

fig, ax = plt.subplots(figsize=(10, 10), dpi=75)
plt.plot(timelist, voltagelist, color='b', marker='o', linestyle='-',  linewidth=0.5, markersize=1.5)
title = 'Процесс зарядки и разрядки конденсатора в RC-цепочке.'
ax.set_title("\n".join(wrap(title, 100)))
plt.xlabel('Время, с')
plt.ylabel('Напряжение, В')
plt.legend('V(t)', loc='upper right')
ax.minorticks_on()
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.125))
ax.set_xlim(0, t2)
ax.set_ylim(0, round(maxVoltage*2)/2)
ax.grid(which='minor', linewidth='0.5', linestyle='-', color='grey')
ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.grid(which='major', linewidth='1.25', linestyle='-', color='grey')

plt.text(3*t2/4, maxVoltage/2, "Время заряда = {:.2f} с".format(t1))
plt.text(3*t2/4, maxVoltage/2.1, "Время разряда = {:.2f} с".format(t2))
plt.savefig('saved_figure.svg')

plt.show()
