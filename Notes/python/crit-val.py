# Two-sided Critical Value
confidence_level = 0.9
alpha = 1 - confidence_level
critical_value = stats.norm.ppf(1 - alpha/2)
print(critical_value)