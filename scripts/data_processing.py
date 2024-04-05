import sys
import pandas as pd

# Setting path
sys.path.append('../datasets')



# Carregamos o dataset com dados populacionais
pop = pd.read_csv('../datasets/raw/population.csv')
pop.rename(columns={'Entity': 'Country'}, inplace = True)
pop = pop[pop['Year'] >= 1990]
pop = pop[pop['Year'] <= 2016]

# Carregamos o dataset para prevelência de obesidade
obes = pd.read_csv('../datasets/raw/share-of-adults-defined-as-obese.csv')
obes.rename(columns={'Entity': 'Country'}, inplace = True)
obes = obes[obes['Year'] >= 1990]

# Carregamos o dataset para prevalência doenças mentais
mental = pd.read_csv('../datasets/raw/mental-illnesses-prevalence.csv')
mental.rename(columns={'Entity': 'Country'}, inplace = True)
mental = mental[mental['Year'] <= 2016]

# Carregamos os dados relativos à pobreza (threshold abaixo de 6.85$ / dia)
# TODO para portefólio: adicionar mais elementos à pipeline como ver as dimensões, min maxing, etc.

poverty = pd.read_csv('../datasets/raw/poverty.csv')
poverty.rename(columns={'country': 'Country', 'year' : 'Year'}, inplace = True)
poverty = poverty[poverty['Year'] <= 2016]
poverty = poverty[poverty['Year'] >= 1990]

# Filtro para limitar apenas aos indicadores de poverty line.
pov_filter = poverty[['Country','Year','headcount_ratio_international_povline','headcount_ratio_lower_mid_income_povline','headcount_ratio_upper_mid_income_povline']]

# Fusão de dataframes
merged = pd.DataFrame()
merged = pd.merge(pop,obes,on=['Country','Code','Year'])
merged = pd.merge(merged,mental,on=['Country','Code','Year'])
merged = pd.merge(merged,pov_filter, left_on=['Country', 'Year'], right_on=['Country','Year'] )

# Salvar o ficheiro com os datasets juntos na diretoria indicada
merged.to_csv('../datasets/processed/dataset_final.csv', index=False)