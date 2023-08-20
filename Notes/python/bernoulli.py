data = stats.bernoulli.rvs(p = .52, size = 30)
p = 0.5 # null hypothesis
p_hat = sum(data) / len(data)
sd = (p*(1-p) / n)**0.5 # st dev from sampling distribution
z = (p_hat - p)/sd # test stat