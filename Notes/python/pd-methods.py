df = pd.read_csv('file.csv')

mean = df.response_variable.mean()
grouped_means = df.groupby("assignment").response_variable.mean()

var = df.var() # variance of each column
corr = df.corr() # correlation table