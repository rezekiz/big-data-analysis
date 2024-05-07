# Importamos o módulo time para efeitos de comparação de tempos de execução
import time

# Carregamento dos datasets
import pandas as pd

pd_start = time.time() # inicio do contador pandas

#Dataset populacional
pop = pd.read_csv('datasets/raw/population.csv')
pop.rename(columns={'Entity': 'Country'}, inplace = True)
pop = pop[pop['Year'] >= 1990]
pop = pop[pop['Year'] <= 2016]
pop.head()
pd_start = time.time()
pop = pd.read_csv('datasets/raw/population.csv')
pop.rename(columns={'Entity': 'Country'}, inplace = True)
pop = pop[pop['Year'] >= 1990]
pop = pop[pop['Year'] <= 2016]

# Carregamos o dataset para prevelência de obesidade
obes = pd.read_csv('datasets/raw/share-of-adults-defined-as-obese.csv')
obes.rename(columns={'Entity': 'Country'}, inplace = True)
obes = obes[obes['Year'] >= 1990]
obes = obes[obes['Year'] <= 2016]
obes.head()

# Carregamos o dataset para prevalência doenças mentais
mental = pd.read_csv('datasets/raw/mental-illnesses-prevalence.csv')
mental.rename(columns={'Entity': 'Country'}, inplace = True)
mental = mental[mental['Year'] >= 1990]
mental = mental[mental['Year'] <= 2016]

# Carregamos os dados relativos à pobreza (threshold abaixo de 6.85$ / dia)
poverty = pd.read_csv('datasets/raw/poverty.csv')
poverty.rename(columns={'country': 'Country', 'year' : 'Year'}, inplace = True)
poverty = poverty[poverty['Year'] <= 2016]
poverty = poverty[poverty['Year'] >= 1990]

# Mantemos apenas contagem de famílias abaixo de 5.5$ /dia e 10€ / dia
poverty = poverty[['Country','Year','headcount_ratio_upper_mid_income_povline','headcount_ratio_1000']]

# Fusão de datasets
dataframes = [pop, obes, mental, poverty]

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

# Verificamos que existem conjuntos de países no dataframe poverty, havendo algumas incompatibilidades
# Excluímos esses países excluindo valores omissos para os indicadores de obesidade, população e doenças mentais
exclude = ['headcount_ratio_1000','headcount_ratio_upper_mid_income_povline']
check = [col for col in fused.columns if col not in exclude]
fused = fused.dropna(subset=check,how = 'any')

# Exportamos para CSV
fused.to_csv('datasets/processed/pd_processed_data.csv')

pd_elapsed = pd_end - pd_start # tempo de execução do contador pandas
print(pd_elapsed)