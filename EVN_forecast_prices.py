#!/usr/bin/env python
# coding: utf-8

# In[83]:


from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.metrics import median_absolute_error, mean_squared_log_error
from statsmodels.tsa.seasonal import seasonal_decompose
get_ipython().run_line_magic('matplotlib', 'inline')
import itertools
import warnings
plt.style.use('ggplot')


# In[84]:


data = pd.read_csv('Electricity_prices.csv')
data.head()


# In[85]:


plt.figure(figsize=[12, 5]); # Set dimensions for figure
data.plot(x='Date', y='Electricity', figsize = (14, 6), legend = True, color='g')
plt.title('Monthly electricity prices in Bulgaria')
plt.ylabel('EUR')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.grid(True)
plt.show()


# 
# # Testing the Stationarity of the Dataset:

# In[86]:


# Augmented Dickey-Fuller test (ADF Test)
ad_fuller_result = adfuller(data['Electricity'])
print(f'ADF Statistic: {ad_fuller_result[0]}')
print(f'p-value: {ad_fuller_result[1]}')


# In[87]:


# The augmented Dickey–Fuller (ADF) statistic, used in the test, is a negative number. 
# The more negative it is, the stronger the rejection of the hypothesis that there is a unit root 
# at some level of confidence.


# In[88]:


# The ADF test is a type of unit root test. Unit roots are a cause for non-stationarity, 
# the ADF test will test if the unit root is present. 
# The Null Hypothesis states there is the presence of a unit root. 
# If the P-Value is less than the Significance Level defined, 
# we reject the Null Hypothesis that the time series contains a unit root. 
# In other words, by rejecting the Null hypothesis, we can conclude that the time series is stationary.


# In[89]:


#Since the series isn’t stationary, we will commit to the first-order differencing of electricity values 
# and perform the ADF test again on the dataset.


# In[90]:


data['Electricity First Difference'] = data['Electricity'] - data['Electricity'].shift(1)
data.dropna(subset = ["Electricity First Difference"], inplace=True)
data


# In[91]:


ad_fuller_result = adfuller(data['Electricity First Difference'])
print(f'ADF Statistic: {ad_fuller_result[0]}')
print(f'p-value: {ad_fuller_result[1]}')


# # Visualize Differenced Series:

# In[92]:


# The p-value is now less than 0.05, meaning that we can reject the null hypothesis i.e. the time series is stationary. 
# Next, let us visualize the differenced series.


# In[93]:


plt.figure(figsize=[12, 5]); # Set dimensions for figure
data['Electricity First Difference'].plot()
plt.title('Monthly electricity prices in Bulgaria - Differenced Series')
plt.ylabel('EUR')
plt.grid(True)


# # ACF and PACF Plots:

# In[94]:


# building auto-correlation (ACF) and partial auto-correlation plots from the differenced series. 
# ACF describes how well the present value of the series is related to its past values while PACF 
# finds a correlation of the residuals with the next lag value.


# In[95]:


from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
import statsmodels.api as sm
fig = plt.figure(figsize=(14,6))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(data['Electricity First Difference'].dropna(),lags=12,ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(data['Electricity First Difference'].dropna(),lags=12,ax=ax2)


# ## SARIMAX Model:

# In[96]:


# After determining that our time series is stationary, we can use the SARIMA model to predict future values.
# The model’s notation is SARIMA(p, d, q) (P, D, Q)lag.
# These three parameters account for seasonality, trend, and noise in data. 
# We will use the AIC (Akaike information criterion) indicator which is an estimator of the relative quality of statistical models. 
# The lower the AIC value the better. After performing multiple iterations, 


# In[128]:


best_model = SARIMAX(data['Electricity'], order=(2, 1, 2), seasonal_order=(1, 1, 1, 3)).fit(dis=-1)
print(best_model.summary())


# In[129]:


#Diagnosing the model residuals
best_model.plot_diagnostics(figsize=(15,12));


# ## Model Forecast:

# In[130]:


#Forecasting 20 months ahead
forecast_values = best_model.get_forecast(steps = 20)

#Confidence intervals of the forecasted values
forecast_ci = forecast_values.conf_int()


# In[131]:


#Plot the data
ax = data.plot(x='Date', y='Electricity', figsize = (14, 6), legend = True, color='purple')

#Plot the forecasted values 
forecast_values.predicted_mean.plot(ax=ax, label='Forecast', figsize = (14, 6), grid=True)


plt.title('Electricity prices in Bulgaria, Monthly', size = 16)
plt.ylabel('EUR', size=12)
plt.legend(loc='upper left', prop={'size': 12})
ax.axes.get_xaxis().set_visible(True)
#annotation
ax.text(65, 65, 'Forecasted Values Until 01/12/2023', fontsize=12,  color='red')
plt.show()


# In[ ]:




