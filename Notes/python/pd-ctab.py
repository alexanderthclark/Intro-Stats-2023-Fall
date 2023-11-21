df = pd.read_csv("marital_status_party_affiliation.csv")

# inspect the data using value_counts()
df.value_counts()

# repeat with crosstab
pd.crosstab(df['Marital Status'], df['Party Affiliation'], margins = True)