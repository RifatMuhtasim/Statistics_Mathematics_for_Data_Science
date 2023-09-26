# Covariance, Covariance Matrix, Pearson Correlation Coefficient, Spearman Correlation Coefficient, Correlation and Causation

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import scipy.stats

df = pd.read_csv("../data/survey_results_public.csv")
# print(df.columns)
# print(df.describe())

salary = df["ConvertedComp"] 
work_week_hrs = df['WorkWeekHrs']
code_rev_hrs = df['CodeRevHrs']
age = df['Age']
comp_total = df['CompTotal']


ex_data = {'X': [1, 2, 3, 4, 5],
                     'Y': [5, 4, 3, 2, 1]}
ex_df = pd.DataFrame(ex_data)


''' @Covariance - 
Covariance is a statistical measure that quantifies the degree to which two random variables change together. 
In other words, it indicates whether two variables tend to increase or decrease in value simultaneously.
A positive covariance means that as one variable increases, the other tends to increase as well,
while a negative covariance indicates that as one variable increases, the other tends to decrease.
'''

covariance = ex_df['Y'].cov(ex_df['X'])
print("Covariance: ", covariance)



''' @Covariance Matrix - 
The covariance matrix is a useful tool for understanding how variables in a dataset are related to each other 
and can be used in various statistical and machine learning applications.
'''

ex_data2 = {'X': [1, 2, 3, 4, 5],
                        'Y': [5, 4, 3, 2, 1],
                        'Z': [2, 3, 1, 4, 5]}
ex_df2  = pd.DataFrame(ex_data2)

covariance_matrix = ex_df2.cov()
print("Covariance Matrix:")
print(covariance_matrix)

''' 
In this covariance matrix:
The diagonal elements (X, Y, and Z) represent the variances of the individual variables.
Off-diagonal elements represent the covariances between pairs of variables. For example, the covariance 
between X and Y is -2.5, and the covariance between Y and X is also -2.5 (covariance is symmetric).
'''



''' @Pearson Correlation Coefficient :- 
The Pearson correlation coefficient, also known as Pearson's r or simply the correlation coefficient,
 is a statistic that measures the linear relationship between two continuous variables. 
 It quantifies the strength and direction of the linear association between two variables. 
 The Pearson correlation coefficient ranges from -1 to 1
'''

person_corr = ex_df['X'].corr(ex_df['Y'])
print(f"Pearson Correlation Coefficient is: {round(person_corr, 4)}")


''' @Spearman Correlation Coefficient:
The Spearman correlation coefficient, also known as Spearman's rho (ρ), is a non-parametric measure of correlation between two variables. 
Unlike the Pearson correlation coefficient, which measures linear relationships, the Spearman correlation coefficient assesses the strength
 and direction of monotonic relationships, which may not necessarily be linear. 
'''

spearman_corr , _ = scipy.stats.spearmanr(ex_df["X"], ex_df["Y"])
print("Spearman Correlation Coefficient is:", spearman_corr)


''' @Causation:
Definition: Causation implies a cause-and-effect relationship between two variables. 
In causation, one variable (the independent variable) directly influences or causes a change in another variable (the dependent variable). 
Establishing causation requires more rigorous evidence than correlation.
Example: If a researcher conducts a controlled experiment and finds that administering a specific drug reliably leads to the 
improvement of a medical condition, they can conclude that the drug causes the improvement.
'''