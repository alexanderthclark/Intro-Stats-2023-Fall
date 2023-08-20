N = 10_000
k = 0

n = 30
p = 0.5 # null hypothesis
sd = (p*(1-p) / n)**0.5 # st dev from sampling distribution

for sim in range(N):
    data = stats.bernoulli.rvs(p = .5, size = n)
    p_hat = sum(data) / len(data)
    z = (p_hat - p)/sd
    if abs(z) > 1.96:
        k += 1

print(k/N)