import numpy as np
import scipy.stats as stats
np.random.seed(1)

x = np.random.normal(1, 1, size = 25)  # 25 draws from N(1,1)
y = np.random.normal(0, 1, size = 10)  # 10 draws from N(0,1)
stats.ttest_ind(x, y, equal_var = False)