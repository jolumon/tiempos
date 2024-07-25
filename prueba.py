import pandas as pd
import matplotlib.pyplot as plt

# Creating a simple dataframe
data = {
    'Year': [2015, 2016, 2017, 2018, 2019],
    'Sales': [2000, 3000, 4000, 3500, 6000]
}
df = pd.DataFrame(data)

# Plotting data
plt.plot(df['Year'], df['Sales'])
plt.xlabel('Year')
plt.ylabel('Sales')
plt.show()