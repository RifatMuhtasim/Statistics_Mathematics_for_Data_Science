## Measure of Dispersion 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


df = pd.read_csv("../data/survey_results_public.csv")
# print(df.columns)
# print(df.describe())

# Example data
data = pd.Series([5, 6, 7, 8, 9])


salary = df["ConvertedComp"] 
work_week_hrs = df['WorkWeekHrs']
code_rev_hrs = df['CodeRevHrs']
age = df['Age']
comp_total = df['CompTotal']

# print(salary.sort_values()[10000:10100]) # Sorted Salary 


'''
 Quantiles and percentiles are statistical measures that help analyze the distribution of a dataset by dividing it into equal parts or 
   specifying particular data points. They are commonly used to understand the spread and central tendency of data.
'''
def Quantiles_and_Percentiles():
   # Create a Random Number
   data1 = pd.Series(np.random.randn(100000))

   # Calculate quartiles (25th, 50th, and 75th percentiles) using Pandas
   quartiles =  data1.quantile([0.25, 0.50, 0.75])

   # Calculate specific percentiles (e.g., 10th, 90th) using Pandas
   percentiles = data1.quantile([0.1, 0.9])

   print("Quartiles:", quartiles)
   print("10th and 90th Percentiles:", percentiles)

   # Create a boxplot to visualize the quartiles
   plt.figure(figsize=(8,4))
   plt.boxplot(data1, vert=False)
   plt.title("Boxplot with Quartiles")
   plt.xlabel("Value")
   plt.savefig("assests/1.04.Plot.png")
   plt.show()


   # Create a histogram to visualize the distribution
   plt.figure(figsize=(8,4))
   plt.hist(data1, bins=20, edgecolor="black")
   plt.title("Histogram")
   plt.xlabel("Value")
   plt.ylabel("Frequency")
   plt.savefig("assests/1.04.Plot_F2.png")
   plt.show()

# Quantiles_and_Percentiles()


''' 
   The "Five-Number Summary" is a descriptive statistics summary of a dataset that includes five key values:
   Minimum: The smallest value in the dataset.
   First Quartile (Q1): The 25th percentile of the data, which separates the lowest 25% of the data from the rest.
   Median (Q2): The 50th percentile of the data, which is the middle value when the data is sorted.
   Third Quartile (Q3): The 75th percentile of the data, which separates the lowest 75% of the data from the highest 25%.
   Maximum: The largest value in the dataset.
   A box plot (or box-and-whisker plot) is a graphical representation of the five-number summary that provides a visual summary of the distribution of the data,
      including the presence of outliers. It is a useful tool for visualizing the spread and central tendency of data. In a box plot:
'''
def Five_number_summary_and_boxplot():
   data = [10, 15, 20, 25, 30, 35, 40, 45, 50, 100]
   df = pd.DataFrame({"Data": data})

   plt.boxplot(df['Data'], vert=False) # vert=False for horizontal box plot
   plt.xlabel("Value")
   plt.title("BoxPlot")
   plt.tight_layout()
   plt.show()

# Five_number_summary_and_boxplot()

''' 
Skewness is a statistical measure that quantifies the asymmetry of the probability distribution of a dataset about its mean. 
It indicates the degree to which a dataset deviates from a normal distribution in terms of its tail behavior. 
A dataset can be positively skewed (right-skewed), negatively skewed (left-skewed), or have zero skewness (symmetric).
'''
def Skewness():
   data = np.random.exponential(scale=2, size=1000) # Left-skewed (exponential distribution with a scale parameter)
   skewness = np.mean(data) - np.median(data)

   plt.hist(data, bins=20, color="blue", alpha=0.7)
   plt.title("Histogram With Right Skewness")
   plt.xlabel("Value")
   plt.ylabel("Frequency")
   plt.tight_layout()

   # Add skewness annotation
   plt.annotate(f'Skewness: {skewness:.2f}', xy=(8,80), fontsize=12, color="red")
   plt.savefig("assests/1.04.Plot_F3_Skewness.png")
   plt.show()


# Skewness()

'''
Kurtosis is a statistical measure that quantifies the "tailedness" or peakedness of the probability distribution of a dataset in relation to 
a normal distribution. It provides insights into the shape of the data distribution, particularly the behavior of data in the tails.
'''
def Kurtosis():
   # Generate a dataset (you can replace this with your data)
   data = np.random.laplace(loc=0, scale=1, size=1000) # Leptokurtic (Laplace distribution)
   df = pd.Series(data)

   data_kurtosis = df.kurtosis()
   print("Kurtosis Value is :", round(data_kurtosis, 2))

   # Create a histogram
   plt.hist(df, bins=30, color="blue", alpha=0.75)
   plt.title("Histogram with Leptokurtic Distribution")
   plt.xlabel("Value")
   plt.ylabel("Frequency")

   plt.tight_layout()
   plt.savefig("assests/1.04.Plot_F3_Kurtosis.png")
   plt.show()

Kurtosis()