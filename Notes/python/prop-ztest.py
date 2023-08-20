from statsmodels.stats.proportion import proportions_ztest

# Hypothesis testing with null of p = 0.6

# Wrong/Different
z1, pval1 = proportions_ztest(10, 20, value = .6)

# Correct/Matches Textbook
z2, pval2 = proportions_ztest(10, 20, value = .6, prop_var = .6)

# By hand
p_hat = 0.5
p = .6
n = 20
sd = (p*(1-p) / (n))**0.5 # st dev from sampling distribution
z3 = (p_hat - p)/sd # test stat