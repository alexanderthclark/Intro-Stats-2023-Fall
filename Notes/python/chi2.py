import scipy.stats as stats
ctab = pd.crosstab(df['Marital Status'], df['Party Affiliation'], margins = False)
stats.chi2_contingency(ctab, correction = False)