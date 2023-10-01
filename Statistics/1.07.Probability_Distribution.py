# Random Variable, Probability Distribution

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, gaussian_kde


''' @Random Variable:
Random variables can be categorized into two main types:
1. Discrete Random Variable: These random variables can only take on a countable number of distinct values.
2. Continuous Random Variable: These random variables can take on any value within a specified range or interval. 
'''

#Generate some Random Variable
# Generate random integers (discrete random variable)
random_integers = np.random.randint(1,100, size=20)  # 20 random integers between 1 and 99 (inclusive)
print("Random Integers:", random_integers)

# Generate random values from a uniform distribution (continuous random variable)
random_uniform = np.random.uniform(0, 1, size=10)  # 10 random values between 0 and 1
print("Uniform Random Variable:", random_uniform)

# Generate random values from a normal distribution (continuous random variable)
random_normal = np.random.normal(0, 1, size=20 )  # 20 random values from a standard normal distribution
print("Random Normal", random_normal)
'''
We use np.random.normal to generate random values from a standard normal distribution (mean=0, standard deviation=1) 
as an example of a continuous random variable following a normal distribution. 
'''

# Generate random binomial values (e.g., 10 trials with success probability 0.3)
# Generates random values from a binomial distribution with parameters n (number of trials) and p (probability of success).
random_binomial = np.random.binomial(10, 0.3, size=10)
print("Binomial Random Variable:", random_binomial)

# Generates random values from a Poisson distribution with a specified rate (λ).
# Generate random Poisson values with rate 2.5
random_poisson = np.random.poisson(2.5 , size=5)
print("Poission Random Variable: ", random_poisson)

# Generates random values from an exponential distribution with a specified rate (λ).
# Generate random exponential values with rate 0.5
random_exponential = np.random.exponential(0.5, size=10)
print("Random Exponential Variable: ", random_exponential)

# Generates random values from a gamma distribution with shape (k) and scale (θ) parameters.
# Generate random gamma values (e.g., shape=2, scale=1)
gamma_values = np.random.gamma(2, 1, size=5)
print("Gamma Random Variable:", gamma_values)



''' @Probability Distibution
   - Youtube Playlist link: https://www.youtube.com/playlist?list=PLaFfQroTgZnzbfK-Rie19FdV6diehETQy
'''


''' @Probability Distribtution and it's Type:
A probability distribution is a mathematical function that describes the likelihood of various outcomes or values in a random experiment or process. Probability distributions can be categorized into two main types: discrete and continuous.

1. **Discrete Probability Distribution:**
   - In a discrete probability distribution, the random variable can take on a countable number of distinct, separate values.
   - The probability mass function (PMF) defines the probability of each specific value.
   - Common examples include:
     - **Bernoulli Distribution:** Models a binary outcome (success or failure) with a single trial, characterized by a probability parameter \(p\).
     - **Binomial Distribution:** Models the number of successes in a fixed number of independent Bernoulli trials, characterized by parameters \(n\) (number of trials) and \(p\) (probability of success).
     - **Poisson Distribution:** Models the number of events occurring in a fixed interval of time or space when the events are rare and independent, characterized by a rate parameter \(\lambda\).
     - **Geometric Distribution:** Models the number of trials needed to achieve the first success in a sequence of independent Bernoulli trials, characterized by a probability parameter \(p\).

2. **Continuous Probability Distribution:**
   - In a continuous probability distribution, the random variable can take on any value within a specified range or interval.
   - The probability density function (PDF) defines the probability of intervals or ranges of values.
   - Common examples include:
     - **Normal Distribution (Gaussian Distribution):** Describes many naturally occurring phenomena with a bell-shaped curve. Characterized by mean (\(\mu\)) and standard deviation (\(\sigma\)).
     - **Exponential Distribution:** Models the time between events in a Poisson process, characterized by a rate parameter \(\lambda\).
     - **Uniform Distribution:** Represents a constant probability of selecting any value within a specified range, characterized by endpoints \(a\) and \(b\).
     - **Gamma Distribution:** Generalizes the exponential distribution and is used to model the time until a Poisson process reaches a certain number of events, characterized by shape (\(k\)) and scale (\(\theta\)) parameters.
'''



''' @Probability Mass Function, Cumulative Desity Function, Probability Density Function Learn:
   - Youtube Video: https://www.youtube.com/watch?v=YXLVjCKVP7U
'''

def pmf():
   data = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5])
   pmf = data.value_counts(normalize=True).sort_index()
   cdf = pmf.cumsum()

   plt.figure(figsize=(12, 5))

   #PDF Plot
   plt.subplot(1, 2, 1)
   plt.bar(pmf.index, pmf.values)
   plt.title("Probability Mass Function (PMF)")
   plt.xlabel("Values")
   plt.ylabel("Probability")

   #CDF Plot
   plt.subplot(1, 2, 2)
   plt.step(cdf.index, cdf.values, where='mid')
   plt.title("Cumulative Density Function")
   plt.xlabel("Values")
   plt.ylabel("Cumulative Probability")

   plt.tight_layout()
   plt.savefig("assests/1.07.Plot.png")
   plt.show()


# pmf()

def pdf():
   data = np.random.normal(loc=0, scale=1, size=1000)
   data_series = pd.Series(data)
   
   # Plot PDF
   plt.figure(figsize=(12, 6))
   plt.subplot(1,2,1)
   plt.hist(data_series, bins=30, density=True, alpha=0.75, color="blue")
   plt.title("Probability Density Function (PDF)")
   plt.xlabel("Values")
   plt.ylabel("Density")

   # Plot CDF
   hist, bin_edge = np.histogram(data_series, bins=30, density=True)
   cdf = np.cumsum(hist) * np.diff(bin_edge)
   plt.subplot(1,2,2)
   plt.plot(bin_edge[1:], cdf, drawstyle="steps", color="green")
   plt.title('Cumulative Density Function (CDF)')
   plt.xlabel('Values')
   plt.ylabel('Cumulative Probability')

   plt.tight_layout()
   plt.savefig("assests/1.07.Plot_F2.png")
   plt.show()

# pdf()


''' @Density Estimation:
   Density estimation is a statistical technique used to estimate the probability density function (PDF) of a random variable 
   based on a finite set of data points. It is a fundamental concept in statistics and data analysis, and it's used for a variety of purposes, 
   including data visualization, outlier detection, hypothesis testing, and generating synthetic data.
   KDE is a non-parametric method used to estimate the PDF of a continuous random variable.
'''

def Density_estimation(): #KDE ( Kernal Density Estimation )
   np.random.seed(0)
   data = np.random.normal(0, 1, size=1000)

   # Perform KDE
   kde = norm(loc=data.mean(), scale=data.std())
   x = np.linspace(data.min(), data.max(), 100)
   y = kde.pdf(x)

   plt.hist(data, bins=30, density=True, alpha=0.75)
   plt.plot(x, y, "r-", linewidth=2)
   plt.xlabel("Values")
   plt.ylabel("Density")
   plt.tight_layout()
   plt.savefig("assests/1.07.Plot_F3.png")
   plt.show()


# Density_estimation()


''' @2D-Density Plot
A 2D density plot, also known as a 2D kernel density plot or contour plot, is a graphical representation used to visualize
the distribution of data points in a two-dimensional space. It is especially useful when you have a large dataset and want to 
understand the density or concentration of data points in different regions of the plot. This type of plot is commonly used in data analysis, 
data visualization, and statistics.
'''

def Box_plot_2D():   
   np.random.seed(0)
   x = np.random.normal(0, 1, 1000)
   y = np.random.normal(0, 1, 1000)

   # Calculate 2D kernel density estimate
   kde = gaussian_kde([x, y])

   # Create a grid of x and y values
   x_grid, y_grid = np.meshgrid(np.linspace(x.min(), x.max(), 100), np.linspace(y.min(), y.max(), 100))

   # Evaluate the KDE on the grid
   density = kde([x_grid.ravel(), y_grid.ravel()]).reshape(x_grid.shape)

   # Create the 2D density plot
   plt.figure(figsize=(8, 6))
   plt.contourf(x_grid, y_grid, density, cmap='viridis')  # You can change the colormap to your preference
   plt.colorbar()  # Add a colorbar to the plot
   plt.xlabel('X-axis')
   plt.ylabel('Y-axis')
   plt.title('2D Density Plot')
   plt.tight_layout()
   plt.savefig("assests/1.07.Plot_F4.png")
   plt.show()


# Box_plot_2D()

