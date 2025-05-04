import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel('2.08д (3В).xlsx')

plt.figure(figsize=(28.3, 19.65))
ax = plt.gca()

plt.scatter(df['X'], df['Y'], color='black', s=10, zorder=3)

plt.scatter(0.65, 520, color='black', s=10, zorder=3)

plt.plot([0, 0.65], [520, 520], 
         color='black', 
         linewidth=1.5)

plt.plot([0.65, 2.2], 
         [-300*0.65 + 715, -300*2.2 + 715],
         color='black', 
         linewidth=1.5,
         linestyle='-')

plt.plot([0.65, 0.65], [0, 520], 
         color='black', 
         linewidth=1,
         linestyle=':')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, markersize=8)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False, markersize=8)

ax.text(0.04, 1.02, r'$I_a$, мкА', transform=ax.transAxes, ha='right', va='bottom')
ax.text(1.01, 0.01, r'$I_L$, А', transform=ax.transAxes, ha='left', va='top')

ax.xaxis.set_major_locator(plt.MultipleLocator(0.2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.05))
ax.yaxis.set_major_locator(plt.MultipleLocator(50))
ax.yaxis.set_minor_locator(plt.MultipleLocator(12.5))

plt.grid(True, linestyle='-', alpha=0.7, which='major')
plt.grid(True, linestyle=':', alpha=0.5, which='minor')

ax.annotate('0.65', xy=(0.65, 0), xytext=(0.67, -0.02), 
            textcoords=ax.get_xaxis_transform(),
            ha='center', va='top', fontsize=9)

plt.title(r'Рис 1. Зависимость $I_a$ от $I_L$ при анодном напряжении 3В')
plt.xlim(0, 2.25)
plt.ylim(0, 550)
# plt.subplots_adjust(left=0.12, right=0.95, bottom=0.15, top=0.95)

plt.show()


# 4В

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('2.08д (4В).xlsx')

plt.figure(figsize=(10, 4))
ax = plt.gca()

plt.scatter(df['X'], df['Y'], color='black', s=10, zorder=3)

plt.scatter(0.7, 590, color='black', s=10, zorder=3)

plt.plot([0, 0.7], [590, 590], 
         color='black', 
         linewidth=1.5)

plt.plot([0.7, 2.6], 
         [-300*0.7 + 800, -300*2.6 + 800],
         color='black', 
         linewidth=1.5,
         linestyle='-')

plt.plot([0.7, 0.7], [0, 590], 
         color='black', 
         linewidth=1,
         linestyle=':')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, markersize=8)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False, markersize=8)

ax.text(0.04, 1.02, r'$I_a$, мкА', transform=ax.transAxes, ha='right', va='bottom')
ax.text(1.01, 0.01, r'$I_L$, А', transform=ax.transAxes, ha='left', va='top')

ax.xaxis.set_major_locator(plt.MultipleLocator(0.2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.05))
ax.yaxis.set_major_locator(plt.MultipleLocator(50))
ax.yaxis.set_minor_locator(plt.MultipleLocator(12.5))

plt.grid(True, linestyle='-', alpha=0.7, which='major')
plt.grid(True, linestyle=':', alpha=0.5, which='minor')

ax.annotate('0.7', xy=(0.7, 0), xytext=(0.7, -0.02), 
            textcoords=ax.get_xaxis_transform(),
            ha='center', va='top', fontsize=9)

plt.title(r'Рис 2. Зависимость $I_a$ от $I_L$ при анодном напряжении 4В')
plt.xlim(0, 2.65)
plt.ylim(0, 620)
# plt.subplots_adjust(left=0.12, right=0.95, bottom=0.15, top=0.95)

plt.show()


# 5 В

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('2.08д (5В).xlsx')

plt.figure(figsize=(10, 4))
ax = plt.gca()

plt.scatter(df['X'], df['Y'], color='black', s=10, zorder=3)

plt.scatter(0.8, 655, color='black', s=10, zorder=3)

plt.plot([0, 0.8], [655, 655], 
         color='black', 
         linewidth=1.5)

plt.plot([0.8, 2.6], 
         [-330*0.8 + 919, -330*2.6 + 919],
         color='black', 
         linewidth=1.5,
         linestyle='-')

plt.plot([0.8, 0.8], [0, 655], 
         color='black', 
         linewidth=1,
         linestyle=':')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, markersize=8)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False, markersize=8)

ax.text(0.04, 1.02, r'$I_a$, мкА', transform=ax.transAxes, ha='right', va='bottom')
ax.text(1.01, 0.01, r'$I_L$, А', transform=ax.transAxes, ha='left', va='top')

ax.xaxis.set_major_locator(plt.MultipleLocator(0.2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.05))
ax.yaxis.set_major_locator(plt.MultipleLocator(50))
ax.yaxis.set_minor_locator(plt.MultipleLocator(12.5))

plt.grid(True, linestyle='-', alpha=0.7, which='major')
plt.grid(True, linestyle=':', alpha=0.5, which='minor')

ax.annotate('', xy=(0.8, 0), xytext=(0.8, -0.02), 
            textcoords=ax.get_xaxis_transform(),
            ha='center', va='top', fontsize=9)

plt.title(r'Рис 3. Зависимость $I_a$ от $I_L$ при анодном напряжении 5В')
plt.xlim(0, 2.75)
plt.ylim(0, 675)
# plt.subplots_adjust(left=0.12, right=0.95, bottom=0.15, top=0.95)

plt.show()

# 6В

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('2.08д (6В).xlsx')

plt.figure(figsize=(10, 4))
ax = plt.gca()

plt.scatter(df['X'], df['Y'], color='black', s=10, zorder=3)

plt.scatter(0.5, 720, color='black', s=10, zorder=3)

plt.plot([0, 0.5], [720, 720], 
         color='black', 
         linewidth=1.5)

plt.plot([0.5, 2.6], 
         [-310*0.5 + 875, -310*2.6 + 875],
         color='black', 
         linewidth=1.5,
         linestyle='-')

plt.plot([0.5, 0.5], [0, 720], 
         color='black', 
         linewidth=1,
         linestyle=':')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, markersize=8)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False, markersize=8)

ax.text(0.04, 1.02, r'$I_a$, мкА', transform=ax.transAxes, ha='right', va='bottom')
ax.text(1.01, 0.01, r'$I_L$, А', transform=ax.transAxes, ha='left', va='top')

ax.xaxis.set_major_locator(plt.MultipleLocator(0.2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.05))
ax.yaxis.set_major_locator(plt.MultipleLocator(50))
ax.yaxis.set_minor_locator(plt.MultipleLocator(12.5))

plt.grid(True, linestyle='-', alpha=0.7, which='major')
plt.grid(True, linestyle=':', alpha=0.5, which='minor')

ax.annotate('0.5', xy=(0.5, 0), xytext=(0.5, -0.02), 
            textcoords=ax.get_xaxis_transform(),
            ha='center', va='top', fontsize=9)

plt.title(r'Рис 4. Зависимость $I_a$ от $I_L$ при анодном напряжении 6В')
plt.xlim(0, 2.65)
plt.ylim(0, 750)
# plt.subplots_adjust(left=0.12, right=0.95, bottom=0.15, top=0.95)

plt.show()