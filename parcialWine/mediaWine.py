
import pandas as pd
df = pd.read_csv('parcialWine/winequality-red.csv', sep=';')
df.head()

alcohol_median = df.alcohol.median()
for wine, alcohol in enumerate(df.alcohol):
    if alcohol >= alcohol_median:
        df.loc[wine, 'alcohol'] = 'high'
    else:
        df.loc[wine, 'alcohol'] = 'low'
df.groupby('alcohol').quality.mean()

ph_median = df.pH.median()
for wine, pH in enumerate(df.pH):
    if pH >= ph_median:
        df.loc[wine, 'pH'] = 'high'
    else:
        df.loc[wine, 'pH'] = 'low'
df.groupby('pH').quality.mean()

residual_sugar_median = df.residual_sugar.median()
for wine, residual_sugar in enumerate(df.residual_sugar):
    if residual_sugar >= residual_sugar_median:
        df.loc[wine, 'residual sugar'] = 'high'
    else:
        df.loc[wine, 'residual sugar'] = 'low'
df.groupby('residual sugar').quality.mean()

citric_acid_median = df.citric_acid.median()
for wine, citric_acid in enumerate(df.citric_acid):
    if citric_acid >= citric_acid_median:
        df.loc[wine, 'citric acid'] = 'high'
    else:
        df.loc[wine, 'citric acid'] = 'low'
df.groupby('citric acid').quality.mean()
