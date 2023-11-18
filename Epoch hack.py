#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
raw_df = pd.read_csv("C:/Users/RLee/Downloads/epoch-hackathon-2023/train.csv")


# In[14]:


df = raw_df


# In[15]:


df.head(10)


# In[16]:


len(df)


# In[24]:


df.describe()


# In[23]:


# Categorical variables
df.describe(include=['object'])


# In[18]:


# Duplicate province (on -> ON)
df["Province"] = [x.upper() for x in df["Province"]]


# In[19]:


# Checking unique ness
df['Loc_prov'] = df['Location'] + df['Province']


# In[22]:


# EXPORT EXCEL 
# Specifying a file name for the Excel file
excel_filename = "C:/Users/RLee/Downloads/epoch_hack_test.xlsx"
df.to_excel(excel_filename, index=False)  # Set index=False to exclude the index from the Excel file


# In[27]:


df["Year"].unique()


# In[29]:


import numpy as np

def parse_years(years, round_up):
    """
    Function to parse an array of years, where years can be a single year or a range in 'year1-year2' format.
    Args:
    years (array-like): Array of years to parse.
    round_up (bool): If True, rounds up dual years to the latter year; if False, rounds down to the former year.

    Returns:
    np.array: Array of parsed years as integers.
    """
    parsed_years = []

    for year in years:
        if isinstance(year, str):
            if '-' in year:
                # Split the year range and convert to integers
                start_year, end_year = map(int, year.split('-'))
                # Choose the year based on the round_up flag
                parsed_year = end_year if round_up else start_year
            else:
                # Single year, convert to integer
                parsed_year = int(year)
        else:
            # Handle NaN or None
            parsed_year = np.nan

        parsed_years.append(parsed_year)

    return np.array(parsed_years)

# Sample data from the DataFrame's "Year" column
years = np.array(['1979', '1980', np.nan, '1981', '1978', '1981-1982', '1982', '1983', '1982-1983'], dtype=object)

# Example usage of the function
df["Year_up"] = parse_years(df["Year"], round_up=True)
df["Year_down"] = parse_years(df["Year"], round_up=False)


# In[37]:


import matplotlib.pyplot as plt


# In[38]:


import seaborn as sns


# In[45]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Creating the scatter plot
x_var = "Year_up"
y_var = "Biomass"
plt.scatter(data=df, x = x_var , y = y_var, marker = ".", alpha = 0.5)

plt.xlabel(x_var)
plt.ylabel(y_var)
plt.show()


# In[52]:


# Boxplot comparing different categories
def boxplot_for_categories(df, categorical_col, target_col):
    plt.figure(figsize=(12, 6))
    ax = sns.boxplot(data=df, x=categorical_col, y=target_col)  # 'ax' now holds the axis object
    plt.title(f'Boxplot of "{target_col}" for each category in "{categorical_col}"')
    # Rotate Xticks for readability
    if rotate_axis == True:
        plt.xticks(rotation=45) 
    # Setting the y-axis limits
    # ax.set_ylim([lower_bound, upper_bound])
    plt.show()
    
    year_counts = parsed_years_series.value_counts(dropna=False)


# In[51]:


# Define your plot bounds (for convenient horizont comparison)
# lower_bound, upper_bound = 0, 2000

# Make boxplots (df, x, y)
rotate_axis = False

# Sorting by the 'Age' column in ascending order
sorted_year_df = df.sort_values(by='Year')

boxplot_for_categories(sorted_year_df, 'Year', 'Biomass') # per meter
# boxplot_for_categories(df, 'site_id', 'meter_reading') # per site


# In[ ]:




