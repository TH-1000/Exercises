import pandas as pd 
import matplotlib.pyplot as plt
from fpdf import FPDF 
import numpy as np

# suppress scientific notation 
pd.set_option('display.float_format', lambda x: '%.2f' % x)

df = pd.read_csv('per-capita-energy-use.csv')

# Rename 'Entity' column >> 'Country'
df = df.rename(columns = {'Entity' : 'Country'})

# Rename last column as 'Consumption'
df = df.rename(columns = {'Energy consumption per capita (kWh)': 'Consumption'})

# Which countries are represented in this DataFrame?
countries = [i for i in df['Country'].unique()]

# How many countries are represented?
len(countries)

# What is the range of data in terms of Years:
min_year = df['Year'].min()
max_year = df['Year'].max()

# What is the total energy spent by each country during this period?
total_consumption = df.groupby('Country', as_index=False).Consumption.sum()

# What is the average of global energy consumption per year?
yearly_global_consumption = df.groupby('Year').Consumption.sum()

result = f'''Countries represented:\n{countries}
Number of countries represented: {len(countries)}
First year of reporting: {min_year}\nLatest year of reporting: {max_year}
Total energy spent by each country(kwh\capita):\n{total_consumption}
Yearly Global Consumption(kwh\capita):\n{yearly_global_consumption}'''

print(result)

# Print result on a PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.multi_cell(0,10,result, border = 1)
pdf.output('energy_conumption.pdf', 'F')

# Plot the yearly global consumption
fig, ax = plt.subplots(dpi = 100)
ax.ticklabel_format(style = 'plain')
ax.set_xlabel('Year')
ax.set_ylabel('Consumption: kwh/capita')
ax.plot(yearly_global_consumption,'r-')
plt.title('Yearly Global Consumption')

plt.savefig('global_consumption.png')

# Draw a pie chart showing the total energy consumption/capita of the top 20 consumers vs the rest of the world
# Who are the top 20?
top_twenty = total_consumption.sort_values(by = 'Consumption', ascending = False, ignore_index = True).head(20)

# Calculate the consumption of the top twenty
top_twenty['Consumption'].sum()

# Calculate the consumption of the rest of the world
rest_of_world = df['Consumption'].sum() - top_twenty['Consumption'].sum()

# add the rest of the world to the top_twenty dataframe
df_rest = pd.DataFrame(columns = ['Country','Consumption'])
df_rest.loc[0] = ['Rest of the World', rest_of_world]
top_twenty = top_twenty.append(df_rest, ignore_index = True)

fig1, ax1 = plt.subplots(figsize = (10,10))
cmap = plt.get_cmap("tab20c")
colors = cmap(np.arange(3)*4)
size = 0.3
ax1.pie(top_twenty['Consumption'],labels = top_twenty['Country'], shadow = True, colors = colors)
plt.title('Top Twenty Energy Consumers per Capita')

plt.savefig('energy_pie_chart.png')



