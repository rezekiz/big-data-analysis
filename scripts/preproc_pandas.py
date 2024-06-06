"""

====================================================
#                                                  #
#    Data preprocessing using Python Pandas        #
#    These scripts use the files located on the    #
#    datasets folder on the repo root              #
#                                                  #
====================================================


"""
import pandas as pd

# Dataset on world population
pop = pd.read_csv('../datasets/raw/population.csv')
pop.rename(columns={'Entity': 'Country'}, inplace = True)
pop = pop[pop['Year'] >= 1990]
pop = pop[pop['Year'] <= 2016]
pop.head()

# Dataset on obesity
obes = pd.read_csv('../datasets/raw/share-of-adults-defined-as-obese.csv')
obes.rename(columns={'Entity': 'Country'}, inplace = True)
obes = obes[obes['Year'] >= 1990]
obes = obes[obes['Year'] <= 2016]
obes.head()

# Dataset on mental disorders prevalence
mental = pd.read_csv('../datasets/raw/mental-illnesses-prevalence.csv')
mental.rename(columns={'Entity': 'Country'}, inplace = True)
mental = mental[mental['Year'] >= 1990]
mental = mental[mental['Year'] <= 2016]
mental.head()

# Mergint the dataframes
dataframes = [pop, obes, mental]

fused = dataframes[0]

for dataframe in dataframes[1:]:
    try:
        fused = pd.merge(
            fused,
            dataframe,
            on = ['Country', 'Year', 'Code'],
            how = 'inner'
        )
    except KeyError:
        fused = pd.merge(
            fused,
            dataframe,
            on = ['Country', 'Year'],
            how = 'outer'
        )

# Exporting to CSV
fused.to_csv('../datasets/processed/pd_processed_data.csv')