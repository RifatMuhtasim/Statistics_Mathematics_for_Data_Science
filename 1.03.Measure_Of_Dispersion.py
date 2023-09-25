## Measure of Dispersion (Range, Variance, Standard Deviation, Coefficient of Variation)
import pandas as pd 

df = pd.read_csv("../data/survey_results_public.csv")
# print(df.columns)
# print(df.describe())

# Example data
data = pd.Series([5, 6, 7, 8, 9])


salary = df["ConvertedComp"] 
# print(salary.sort_values()[10000:10100]) # Sorted Salary 

work_week_hrs = df['WorkWeekHrs']
code_rev_hrs = df['CodeRevHrs']
age = df['Age']
comp_total = df['CompTotal']


## Range - Age Range
salary_range = salary.max() - salary.min()
print("Range:", salary_range)



## Variance 
# Variance is a measure of the spread or dispersion of data points in a dataset relative to their mean.

variance = code_rev_hrs.var()
print("Variance:", variance)


'''
Standard Deviation
Standard deviation is a statistical measure that quantifies the amount of variation or dispersion in a dataset. 
It provides a way to understand how spread out the values in a dataset are from the mean (average) value. In other words,
it measures the degree to which data points deviate from the mean.
'''

std_deviation = work_week_hrs.std()
print("Standard Deviation:", std_deviation)



'''
Coefficient of variation - 
The coefficient of variation (CV) is a relative measure of variability that expresses the standard deviation as a percentage of the mean.
It is a useful statistic when comparing the variability of data sets with different units or scales.
'''

mean = data.mean()
std_deviation = data.std()
coefficient_of_variation = (std_deviation / mean) * 100
print("Coefficient of Variation", coefficient_of_variation)