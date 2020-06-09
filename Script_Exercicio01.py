import pandas as pd
import numpy as np
import csv
import math

df = pd.read_csv("Planilha_Exercicio.csv", encoding="Utf-8")

instances = df.shape[0]
columns = df.shape[1]
name_column = df.keys()

lines = []
for i in range(0, instances):
    lines.append(df.loc[i])

maximos = []
minimos = []

for i in range(0, columns):
    max = 0.0
    min = math.inf

    for j in range(0, instances):
        if lines[j][name_column[i]] > max:
            max = lines[j][name_column[i]]
        elif lines[j][name_column[i]] < min:
            min = lines[j][name_column[i]]

    maximos.append(max)
    minimos.append(min)

final = []

for key in name_column:
    final.append(key)
for i in range(0, instances):
    for j in range(0, columns):
        final.append((lines[i][name_column[j]] -
                      minimos[j]) / (maximos[j]-minimos[j]))

final = np.reshape(final, (instances+1, columns))

with open('resposta_exe01.csv', 'w', encoding="utf-8", newline='\n') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(final)
