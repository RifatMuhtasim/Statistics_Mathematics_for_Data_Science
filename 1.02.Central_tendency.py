## Central Tendency (Mean, Median, Mode)
import pandas as pd 


df = pd.read_csv("../data/survey_results_public.csv")
# print(df.columns)

salary = df["ConvertedComp"] 
# print(salary)

## Calculate Mean
mean = salary.mean()

## Calculate Median
median = salary.median()

## Calculate Mode
mode = salary.mode().iloc[0] # iloc[0] is used to get the first mode if multiple modes exist

print("Mean:", round(mean, 4)) # Show the Result on 2 Decimal Point
print("Median:", median)
print("Mode:", mode)


## Weighted Mean
Json_data = {  'CGPA': [3.5, 3.8, 4.0, 3.2, 3.9], 
                           'Credit': [3, 4, 3, 3, 4]   }
cgpa_data = pd.DataFrame(Json_data)

weighted_mean = (cgpa_data['CGPA'] * cgpa_data['Credit']).sum() / cgpa_data['Credit'].sum()

# Weighted Mean CGPA = ((3.5 * 3) + (3.8 * 4) + (4.0 * 3) + (3.2 * 3) + (3.9 * 4)) / (3 + 4 + 3 + 3 + 4) = (10.5 + 15.2 + 12.0 + 9.6 + 15.6) / 17 = 63.9 / 17 = 3.76 (approximately)
print("Weighted Mean:", weighted_mean)


## Trimmed mean
# Define the percentage of data to trim from each end
trim_percentage = 20  # Trim 20% from each end

# Sort the data
sorted_salary = salary.sort_values()

# Calculate the number of data points to trim from each end
trim_count = int(len(sorted_salary) * (trim_percentage/100))

# Trim the data by removing the specified number of points from each end
trimmed_salary = sorted_salary.iloc[trim_count:-trim_count]

# Calculate the trimmed mean
trimmed_salary_mean = trimmed_salary.mean()

print("Trimmed Mean", trimmed_salary_mean)
