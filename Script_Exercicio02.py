import pandas as pd
import numpy as np
import csv
import math

df = pd.read_csv("resposta_exe01.csv", encoding="Utf-8")

instances = df.shape[0]
columns = df.shape[1]
name_column = df.keys()

lines = []
for i in range(0, instances):
    lines.append(df.loc[i])

final = []

for key in name_column:
    final.append(key)
for i in range(0, instances):
    for j in range(0, columns):
        if lines[i][name_column[j]] >= 0 and lines[i][name_column[j]] < 0.1667:
            final.append('cat01')
        elif lines[i][name_column[j]] >= 0.1667 and lines[i][name_column[j]] < 0.3334:
            final.append('cat02')
        elif lines[i][name_column[j]] >= 0.3334 and lines[i][name_column[j]] < 0.5:
            final.append('cat03')
        elif lines[i][name_column[j]] >= 0.5 and lines[i][name_column[j]] < 0.6667:
            final.append('cat04')
        elif lines[i][name_column[j]] >= 0.6667 and lines[i][name_column[j]] < 0.8334:
            final.append('cat05')
        else:
            final.append('cat06')

final = np.reshape(final, (instances+1, columns))

with open('resposta_exe02.csv', 'w', encoding="utf-8", newline='\n') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(final)
