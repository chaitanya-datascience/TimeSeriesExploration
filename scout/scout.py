import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.graphics.tsaplots import plot_acf

class ts_scout():
    def __init__(self, df):
        """
        Initialize the summary class
        Arguments:
            df( pandas dataframe)
            The first column of the dataframe
            is the datetime values. The label for column ='time')
            The remaining columns of the dataframe are the values/measurements of interest"""
        self.df = df

    def histogram(self):
        
        """
            Method to plot the histogram of variable.
            Arguments: None

            Returns: None
        """
        for i in self.df.columns:
            if i == 'time':
                continue
            print('Histogram for {}'.format(i))
            plt.hist(self.df[str(i)])
            plt.xlabel(str(i),fontsize=15)
            plt.ylabel('Count',fontsize=15)
            plt.title('Histogram of data {}'.format(i),fontsize=15)
            plt.show()
            print('\n')
    
    def pdf(self):
        """
        Method to plot the probability density function of variables.
            Arguments: None

            Returns : None
        """
        for i in self.df.columns:
            if i == 'time':
                continue
            print('Probability Density Function for {}'.format(i))
            self.df[str(i)].plot(kind='kde')
            plt.title('PDF of data {}'.format(i),fontsize=15)
            plt.xlabel(str(i),fontsize=15)
            plt.ylabel('Density',fontsize=15)
            plt.show()
            print('\n')

    def ts(self,lag):
        """
        Methods to plot the autocorrelation and partial
        autocorrelation function of variables

            Arguments:
                lag (int): Number of time periods to restrict the plots at
            Return:
                None
        """
        self.df['time']=pd.to_datetime(self.df['time'])
        for i in self.df.columns:
            if i == 'time':
                continue
            d=self.df.resample('24H',on='time')[str(i)].median().ffill()
            d.dropna(inplace=True)
            print('Autocorrelation plot for {}'.format(i))
            plot_acf(d.values,lags=lag)
            plt.title('Autocorrelation plot for data {}'.format(i),fontsize=15)
            plt.show()
            print('\n')

            print('Partial autocorrelation plot for {}'.format(i))
            plot_pacf(d.values,lags=lag)
            plt.title('Partia autocorrelation plot for data {}'.format(i),fontsize=15)
            plt.show()
            print('\n')
    
    def __repr__(self):
        """
        Magic method to represent the data frame.
        
        """
        return ('The summary of your data \n{}'.format(self.df.describe()))
