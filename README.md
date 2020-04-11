# TimeSeriesExploration
Understand your multivariate time series

With scout, you can quickly analyze and visualize the multivariate time series data with python in just few lines of code. Just read the time series data collected into a pandas dataframe with datetime column labeled as "time", and the rest is done for you. Make sure the datetime data is clean and converted to pandas datetime format using `pandas.to_datetime`

# Overview
The `ts_scout()` Python class was written to improve the time in analyzing the time series data in time domain and understand the significant the data better. It provides the following key features

  - Visualize the histogram of each variable in data
  - Visualize the probability density function using Gaussiah kernels
  - Visualize the **Autocorrelation Function and Partial autocorrelation** function
  - Print the summary of all variables of data using repr magic method

## Usage

In the following paragraphs, I am going to describe how you can get and use Denoise for your own projects.

###  Getting it

To download distributions, fork this github repo. 

### Using it

scout was programmed with ease-of-use in mind. First, import ts_scout from scout

```Python
from scout import ts_scout
```

And you are ready to go! At this point, I want to clearly explain ts_scout class 

## Initialize a Denoisefft object
The only input is the pandas dataframe with first column being the datetime values and labeled as
*time*
```Python
summary_one=ts_scout(df)
```

## Visualize the histogram and PDF
The class ts_scout has a two methods - histogram and pdf to visualize each variable data 
distribution.

```Python
summary_one.histogram()
summary_one.pdf()
```
#### Visualize autocorrelation and partial autocorrelation
Plot the autocorrelation and partial autocorrelation of each variable with the lags to understand the time series
relations

```Python
summary_one.ts()
```

#### Represent the data with magic method repr
Using the magic method to print out the `pandas.desrcibe()` output to get the distribution of variables as a quick 
quantification along with the plots.

```Python
summary_one
```

License
----

MIT License

Copyright (c) 2020 Chaitanya Joshi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

