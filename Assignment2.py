import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import stats as st

# %%


def clean_worldbank_data(filename):
    """
    This function reads World Bank data, cleans it, and returns dataframes 
    with years as columns and countries as columns.
    """
    # skip unneccesary data
    data = pd.read_csv(filename, skiprows=4)
    data.set_index("Country Name", inplace=True)
    # Transpose the Data
    data_years = data.T
    # set meaningful header
    data_years.columns.name = "Country Name"
    return data_years, data


# Call the co2 dataframe
co2_dataframe_years, co2_dataframe_countries = clean_worldbank_data("co2.csv")
# Call the indicators
gdp_dataframe_years, gdp_dataframe_countries = clean_worldbank_data(
    "GDP.csv")  # Gdp per capita
forest_dataframe_years, forest_dataframe_countries = clean_worldbank_data(
    "FRST.csv")  # Forest Area in KM
urban_dataframe_years, urban_dataframe_countries = clean_worldbank_data(
    "UrbanPop.csv")  # Urban Population per country

# %%
# .describe()


def describe_dataframes(*dataframes):
    """
    Function to describe the contents of DataFrames.
    """
    for df in dataframes:

        print(f"Description of Dataframe: ")
        print(df.describe())
        print()


# Calls the dataframe you would like to descibe
describe_dataframes(
    urban_dataframe_countries, urban_dataframe_years,
    gdp_dataframe_years, gdp_dataframe_countries,
    forest_dataframe_years, forest_dataframe_countries,
    co2_dataframe_years, co2_dataframe_countries)

# %%
# countries from different economical backgrounds
rich_countries = ['United States']
middle_countries = ['Brazil']
poor_countries = ['India']
# %%
# CORRELATION BETWEEN CO2 AND GDP IN RICH, MIDDLE AND POOR COUNTRIES
# Rich country
rich_co2_gdp_corr = co2_dataframe_years[rich_countries].corrwith(
    gdp_dataframe_years[rich_countries])
# middle-income countries
middle_co2_gdp_corr = co2_dataframe_years[middle_countries].corrwith(
    gdp_dataframe_years[middle_countries])
# poor countries
poor_co2_gdp_corr = co2_dataframe_years[poor_countries].corrwith(
    gdp_dataframe_years[poor_countries])
# print conclusion
print("Correlation between GDP per capita and CO2 emissions for rich countries:")
print(rich_co2_gdp_corr)
print("\nCorrelation between GDP per capita and CO2 emissions for middle-income countries:")
print(middle_co2_gdp_corr)
print("\nCorrelation between GDP per capita and CO2 emissions for poor countries:")
print(poor_co2_gdp_corr)

countries = ['US', 'Brazil', 'India']
correlation_values = [rich_co2_gdp_corr.values[0],
                      middle_co2_gdp_corr.values[0], poor_co2_gdp_corr.values[0]]

plt.figure(figsize=(8, 6))
plt.bar(countries, correlation_values, color=['green', 'blue', 'red'])
plt.title('Correlation between CO2 Emissions and GDP')
plt.xlabel('Country')
plt.ylabel('Correlation')
plt.ylim(-1, 1)
plt.grid(axis='y', linestyle='--')
plt.axhline(0, color='black', linewidth=0.8)
plt.show()
# CORRELATION BETWEEN CO2 AND GDP IN RICH, MIDDLE AND POOR COUNTRIES
# Rich country
rich_co2_gdp_corr = co2_dataframe_years[rich_countries].corrwith(
    gdp_dataframe_years[rich_countries])
# middle-income countries
middle_co2_gdp_corr = co2_dataframe_years[middle_countries].corrwith(
    gdp_dataframe_years[middle_countries])
# poor countries
poor_co2_gdp_corr = co2_dataframe_years[poor_countries].corrwith(
    gdp_dataframe_years[poor_countries])
# print conclusion
print("Correlation between GDP per capita and CO2 emissions for rich countries:")
print(rich_co2_gdp_corr)
print("\nCorrelation between GDP per capita and CO2 emissions for middle-income countries:")
print(middle_co2_gdp_corr)
print("\nCorrelation between GDP per capita and CO2 emissions for poor countries:")
print(poor_co2_gdp_corr)
# %%
# CORRELATION BETWEEN CO2 AND FOREST AREA IN RICH, MIDDLE AND POOR COUNTRIES
# Rich country
rich_co2_frst_corr = co2_dataframe_years[rich_countries].corrwith(
    forest_dataframe_years[rich_countries])
# middle-income countries
middle_co2_frst_corr = co2_dataframe_years[middle_countries].corrwith(
    forest_dataframe_years[middle_countries])
# poor countries
poor_co2_frst_corr = co2_dataframe_years[poor_countries].corrwith(
    forest_dataframe_years[poor_countries])
# print conclusion
print("Correlation between forest area in KM and CO2 emissions for rich countries:")
print(rich_co2_frst_corr)
print("\nCorrelation between forest area in KM  and CO2 emissions for middle-income countries:")
print(middle_co2_frst_corr)
print("\nCorrelation between forest area in KM  and CO2 emissions for poor countries:")
print(poor_co2_frst_corr)

countries = ['US', 'Brazil', 'India']
correlation_values = [rich_co2_frst_corr.values[0],
                      middle_co2_frst_corr.values[0], poor_co2_frst_corr.values[0]]
plt.figure(figsize=(8, 6))
plt.bar(countries, correlation_values, color=['green', 'blue', 'red'])
plt.title('Correlation between CO2 Emissions and Forest Area')
plt.xlabel('Country')
plt.ylabel('Correlation')
plt.ylim(-1, 1)
plt.grid(axis='y', linestyle='--')
plt.axhline(0, color='black', linewidth=0.8)
plt.show()
# %%
# CORRELATION BETWEEN CO2 AND URBAN POP IN RICH, MIDDLE AND POOR COUNTRIES
# Rich country
rich_co2_urban_corr = co2_dataframe_years[rich_countries].corrwith(
    urban_dataframe_years[rich_countries])
# middle-income countries
middle_co2_urban_corr = co2_dataframe_years[middle_countries].corrwith(
    urban_dataframe_years[middle_countries])
# poor countries
poor_co2_urban_corr = co2_dataframe_years[poor_countries].corrwith(
    urban_dataframe_years[poor_countries])
# print conclusion
print("Correlation between Urban Population and CO2 emissions for rich countries:")
print(rich_co2_urban_corr)
print("\nCorrelation between Urban Population  and CO2 emissions for middle-income countries:")
print(middle_co2_urban_corr)
print("\nCorrelation between Urban Population  and CO2 emissions for poor countries:")
print(poor_co2_urban_corr)

countries = ['US', 'Brazil', 'India']
correlation_values = [rich_co2_urban_corr.values[0],
                      middle_co2_urban_corr.values[0], poor_co2_urban_corr.values[0]]

plt.figure(figsize=(8, 6))
plt.bar(countries, correlation_values, color=['green', 'blue', 'red'])
plt.title('Correlation between CO2 Emissions and Urban Population')
plt.xlabel('Country')
plt.ylabel('Correlation')
plt.ylim(-1, 1)
plt.grid(axis='y', linestyle='--')
plt.axhline(0, color='black', linewidth=0.8)
plt.show()
# %%
# Correlation between CO2 and each indicator - first 15 years and last 15 years.


def calculate_correlation(co2_dataframe, other_dataframe, countries, years):
    # Split from 1990 - 2020 as 1990 is when data starts.
    co2_data_from_1990 = co2_dataframe.iloc[:, 30:]
    other_data_from_1990 = other_dataframe.iloc[:, 30:]

    # split data into first 15 years (1990-2004)
    first_15_years_co2 = co2_data_from_1990.iloc[:, :15]
    first_15_years_other = other_data_from_1990.iloc[:, :15]
    # split the data into last 15 years (2005-2020)
    last_15_years_co2 = co2_data_from_1990.iloc[:, 15:31]
    last_15_years_other = other_data_from_1990.iloc[:, 15:31]

    # Calculate the correlations for the first 15 years
    corr_first_15_years = first_15_years_co2.T.corrwith(first_15_years_other.T)
    # Filter for the rich, middle and poor countries
    corr_first_15_years_countries = corr_first_15_years.loc[countries]

    # calculate the correlations for the last 15 years
    corr_last_15_years = last_15_years_co2.T.corrwith(last_15_years_other.T)
    # Filter for the rich, middle and poor countries
    corr_last_15_years_countries = corr_last_15_years.loc[countries]

    return corr_first_15_years_countries, corr_last_15_years_countries


# Print Results
countries = ['United States', 'Brazil', 'India']
years = range(1990, 2005)
corr_first_15_years_CG, corr_last_15_years_CG = calculate_correlation(
    co2_dataframe_countries, gdp_dataframe_countries, countries, years)
corr_first_15_years_CF, corr_last_15_years_CF = calculate_correlation(
    co2_dataframe_countries, forest_dataframe_countries, countries, years)
corr_first_15_years_CU, corr_last_15_years_CU = calculate_correlation(
    co2_dataframe_countries, urban_dataframe_countries, countries, years)

print("Correlation for US:")
print("First 15 years (GDP):", corr_first_15_years_CG['United States'],
      "\tLast 15 years (GDP):", corr_last_15_years_CG['United States'])
print("First 15 years (Forest):", corr_first_15_years_CF['United States'],
      "\tLast 15 years (Forest):", corr_last_15_years_CF['United States'])
print("First 15 years (Urban):", corr_first_15_years_CU['United States'],
      "\tLast 15 years (Urban):", corr_last_15_years_CU['United States'])

print("\nCorrelation for Brazil:")
print("First 15 years (GDP):", corr_first_15_years_CG['Brazil'],
      "\tLast 15 years (GDP):", corr_last_15_years_CG['Brazil'])
print("First 15 years (Forest):", corr_first_15_years_CF['Brazil'],
      "\tLast 15 years (Forest):", corr_last_15_years_CF['Brazil'])
print("First 15 years (Urban):", corr_first_15_years_CU['Brazil'],
      "\tLast 15 years (Urban):", corr_last_15_years_CU['Brazil'])

print("\nCorrelation for India:")
print("First 15 years (GDP):", corr_first_15_years_CG['India'],
      "\tLast 15 years (GDP):", corr_last_15_years_CG['India'])
print("First 15 years (Forest):", corr_first_15_years_CF['India'],
      "\tLast 15 years (Forest):", corr_last_15_years_CF['India'])
print("First 15 years (Urban):", corr_first_15_years_CU['India'],
      "\tLast 15 years (Urban):", corr_last_15_years_CU['India'])
# %%
# PLOT THE PREVIOUS WORKING ON A GRAPH
indicators = ['GDP', 'Forest Area', 'Urban Population']

# Dictionary holding correlation coefficients
corr_coefficients = {
    'First 15 Years': [[corr_first_15_years_CG[country] for country in countries],
                       [corr_first_15_years_CF[country]
                           for country in countries],
                       [corr_first_15_years_CU[country] for country in countries]],
    'Last 15 Years': [[corr_last_15_years_CG[country] for country in countries],
                      [corr_last_15_years_CF[country]
                          for country in countries],
                      [corr_last_15_years_CU[country] for country in countries]]
}
# Create subplots for each period
fig, axes = plt.subplots(1, 2, figsize=(15, 6))
bar_width = 0.35
index = np.arange(len(countries))
# Iterates over each time frame (first 15 and last fifteen)
for i, (period, corr_values) in enumerate(corr_coefficients.items()):
    # Iterates over each indicator
    for j, indicator in enumerate(indicators):
        ax = axes[i]
        ax.bar(index + j * bar_width,
               corr_values[j], bar_width, label=f'{indicator} ({period})')

        ax.set_xlabel('Country')
        ax.set_title(f'Correlation ({period})')
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(countries)
        ax.legend()

axes[0].set_ylabel('Correlation Coefficient')
plt.tight_layout()
plt.show()
