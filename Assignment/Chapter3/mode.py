# import statistics 
#calculate for mean, mode and median.
#print your results

import statistics 

values = [9, 11, 22, 34, 17, 22, 34, 22, 40, 34]  #after including 34 to the values, the median changed to a decimal point, the mode didn't change and the mean increased.

print(statistics.mean(values))


print(statistics.median(values))


print(statistics.mode(values))
