
'''
The function clean_data(df) needs to be implemented. The df is the DataFrame on which operations are performed.
The data used for this is of different housing societies
The task is to clean the data before useful insights can be extracted from it. The following two steps are performed on the data.
1.Drop all the rows that have at least one NaN value in any of its columns.
2.Find and remove the outliers that might occur in the median_house_value, median_income, or housing_median_age column. Use the IQR method for finding outliers.

The output is a Dataframe with no NaN values, and all its outliers are in the required range.
'''
import pandas as pd

def clean_data(df):

    df = df.dropna() # dropping all rows with null values

    # A list of all columns on which outliers need to be removed
    out_list = ['median_house_value', 'median_income', 'housing_median_age']

    quantiles_df = (df.quantile([0.25,0.75])) # computing 1st & 3rd quartiles

    for out in out_list: # traversing through the list

        Q1 = quantiles_df[out][0.25] # Retrieving value of 1st quartile
        Q3 = quantiles_df[out][0.75] # Retrieving value of 3rd quartile

        iqr = Q3 - Q1 # computing the interquartile range

        lower_bound = (Q1 - (iqr * 1.5)) # computing lower bound
        upper_bound = (Q3 + (iqr * 1.5)) # computing upper bound

        col = df[out] # Storing reference of required column

        col[(col < lower_bound)] = lower_bound # Assign outliers to lower bound

        col[(col > upper_bound)] = upper_bound # Assign outliers to upper bound

    return df

# Test Code

df = pd.read_csv('housing.csv')

df_res = clean_data(df.copy())

print(df_res)
