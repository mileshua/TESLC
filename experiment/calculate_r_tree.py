
import csv
import re
import matplotlib.pyplot as plt
import scipy
import numpy as np
data = {'WASHINGTON (GREATER)': {'built': 15.7311, 'water': 0.0054, 'tree': 0.0027}, 'BOSTON': {'built': 14.6817, 'water': 0.027, 'tree': 0.0576}, 'JACKSONVILLE': {'built': 1.3914, 'water': 0.0036, 'tree': 0.0936}, 'PHOENIX': {'built': 0.9738, 'water': 0.0072, 'tree': 0.0675}, 'SACRAMENTO': {'built': 644.6682, 'water': 7.3773, 'tree': 1.8440999999999999}, 'SAN FRANCISCO (GREATER)': {'built': 157.2534, 'water': 1.1043, 'tree': 0.8775}, 'DENVER': {'built': 403.1028, 'water': 4.8582, 'tree': 0.2844}, 'LAS VEGAS': {'built': 232.02179999999998, 'water': 0.0063, 'tree': 0.0072}, 'ALBUQUERQUE': {'built': 256.7691, 'water': 0.062099999999999995, 'tree': 3.2553}, 'LOS ANGELES (GREATER)': {'built': 3679.1342999999997, 'water': 5.9822999999999995, 'tree': 49.0878}, 'SAN DIEGO': {'built': 542.3877, 'water': 1.1385, 'tree': 5.0904}, 'AUSTIN': {'built': 16.2612, 'water': 0.35819999999999996, 'tree': 0.7343999999999999}, 'HOUSTON': {'built': 3.5846999999999998, 'water': 0.0, 'tree': 0.9747}, 'NEW ORLEANS': {'built': 42.9264, 'water': 2.4867, 'tree': 0.0081}, 'INDIANAPOLIS': {'built': 759.798, 'water': 6.0777, 'tree': 21.4191}, 'NEW YORK (GREATER)': {'built': 369.4824, 'water': 7.9308, 'tree': 9.0522}, 'SAN ANTONIO': {'built': 29.4345, 'water': 0.0, 'tree': 0.7676999999999999}}
data = {a.lower(): b for a, b in data.items()}

x_label = []
x = []
y = []
key = "water"
with open("carbon.csv") as carbon:
    reader = csv.reader(carbon, delimiter = ",", quotechar = '"')
    data_carbon = {}
    for row in reader:
        row[0] = row[0].lower()
        if row[1] == "United States" and row[0] not in data_carbon:
            data_carbon[row[0]] = [0, 0, 0]
        if row[1] == "United States" and "2019" in row[2]:
            data_carbon[row[0]][0] = data_carbon.get(row[0], [0,0,0])[0] + float(row[4])

        if row[1] == "United States" and "2020" in row[2]:
            data_carbon[row[0]][1] = data_carbon.get(row[0], [0,0,0])[1] + float(row[4])

        if row[1] == "United States" and "2021" in row[2]:
            data_carbon[row[0]][2] = data_carbon.get(row[0], [0,0,0])[2] + float(row[4])

#for city in data:
#    x_label.append(city)
#    x.append(data[city]["tree"])
#    y.append(data_carbon[city.lower()][0])
    
with open("solar.csv") as solar:
    reader = csv.reader(solar, delimiter = ",", quotechar = '"')
    for row in reader:
        row[1] = row[1].lower()
        if row[1] not in data_carbon:
            print(row[1])

        else:
            if row[4] == "N/A":
                continue
            x_label.append(row[1])
            x.append(data[row[1]][key]/sum(data[row[1]].values()))
            y.append(data_carbon[row[1]][0]/int(row[5].replace(",", "")))

            #y.append(data_carbon[row[1]][0])
print(x, y)
fig, ax = plt.subplots()
ax.set_title(key)
ax.scatter(x, y)

for i, txt in enumerate(x_label):
    ax.annotate(txt, (x[i], y[i]))
m, b, r_value, p_value, std_err = scipy.stats.linregress(x, y)

ax.plot(x, m*np.array(x)+ b)
print('r^2: ' + str("{:.2f}".format(r_value**2)))
plt.show()
