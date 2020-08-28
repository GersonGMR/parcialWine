
import pandas as pd
df = pd.read_csv('winequality-red.csv', sep=';')
df.head()

media_alcohol = df.alcohol.median()
for wine, alcohol in enumerate(df.alcohol):
    if alcohol >= media_alcohol:
        df.loc[wine, 'alcohol'] = 'alto'
    else:
        df.loc[wine, 'alcohol'] = 'bajo'
df.groupby('alcohol').quality.mean()

media_ph = df.pH.median()
for wine, pH in enumerate(df.pH):
    if pH >= media_ph:
        df.loc[wine, 'pH'] = 'alto'
    else:
        df.loc[wine, 'pH'] = 'bajo'
df.groupby('pH').quality.mean()

media_residual_sugar = df.residual_sugar.median()
for wine, residual_sugar in enumerate(df.residual_sugar):
    if residual_sugar >= media_residual_sugar:
        df.loc[wine, 'residual sugar'] = 'alto'
    else:
        df.loc[wine, 'residual sugar'] = 'bajo'
df.groupby('residual sugar').quality.mean()

media_citric_acid = df.citric_acid.median()
for wine, citric_acid in enumerate(df.citric_acid):
    if citric_acid >= media_citric_acid:
        df.loc[wine, 'citric acid'] = 'alto'
    else:
        df.loc[wine, 'citric acid'] = 'bajo'
df.groupby('citric acid').quality.mean()
