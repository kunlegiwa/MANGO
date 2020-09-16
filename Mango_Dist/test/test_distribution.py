from Mango_Dist.dist_functions import distribution_functions as df
from Mango_Dist.dist_classes.distribution_classes import Distribution


print(df.draw('lognormal', size=5, mean=4, sigma=2))

dist1 = Distribution(size=3)
print(dist1.draw())
dist1.size = 6
print(dist1.draw())
print(dist1.summarise())


