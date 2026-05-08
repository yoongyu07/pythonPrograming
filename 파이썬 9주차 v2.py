import matplotlib.pyplot as plt

year = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
gdp = [3079.9, 3250.1, 3398.8, 3574, 3678.2, 3721.8, 3744, 4003.6, 4165.5]

plt.figure(figsize=(5, 3))
plt.plot(year, gdp, color='#008080', marker='h', linestyle='--')
plt.title('GDP per capita')
plt.xlabel('years')
plt.ylabel('ten thousand won')
plt.ylim(2500, 4500)
plt.show()