import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%
def clean_worldbank_data(filename):
    """
    This function reads World Bank data, cleans it, and returns dataframes 
    with years as columns and countries as columns.
    """
    #skip unneccesary data
    data = pd.read_csv(filename, skiprows=4)
    data.set_index("Country Name", inplace=True)
    #Transpose the Data
    data_years = data.T
    #set meaningful header
    data_years.columns.name = "Country Name"
    return data_years, data
#Call the co2 dataframe
co2_dataframe_years, co2_dataframe_countries = clean_worldbank_data("co2.csv")
#Call the indicators
gdp_dataframe_years, gdp_dataframe_countries = clean_worldbank_data("GDP.csv") #Gdp per capita
forest_dataframe_years, forest_dataframe_countries = clean_worldbank_data("FRST.csv") #Forest Area in KM
urban_dataframe_years,urban_dataframe_countries = clean_worldbank_data("UrbanPop.csv") #Urban Population per country

#%%
#.describe()
def describe_dataframes(*dataframes):
    """
    Function to describe the contents of DataFrames.
    """
    for df in dataframes:
        
        print(f"Description of Dataframe: ")
        print(df.describe())
        print()

#Calls the dataframe you would like to descibe
describe_dataframes(urban_dataframe_countries["1990"], urban_dataframe_countries["2020"])

#%%
#countries from different economical backgrounds
rich_countries = ['United States']
middle_countries = ['Brazil']
poor_countries = ['India']

#%%
#CORRELATION BETWEEN CO2 AND GDP IN RICH, MIDDLE AND POOR COUNTRIES
#Rich country 
rich_co2_gdp_corr = co2_dataframe_years[rich_countries].corrwith(gdp_dataframe_years[rich_countries])
#middle-income countries
middle_co2_gdp_corr = co2_dataframe_years[middle_countries].corrwith(gdp_dataframe_years[middle_countries])
# poor countries
poor_co2_gdp_corr = co2_dataframe_years[poor_countries].corrwith(gdp_dataframe_years[poor_countries])
#print conclusion
print("Correlation between GDP per capita and CO2 emissions for rich countries:")
print(rich_co2_gdp_corr)
print("\nCorrelation between GDP per capita and CO2 emissions for middle-income countries:")
print(middle_co2_gdp_corr)
print("\nCorrelation between GDP per capita and CO2 emissions for poor countries:")
print(poor_co2_gdp_corr)
#%%
#CORRELATION BETWEEN CO2 AND FOREST AREA IN RICH, MIDDLE AND POOR COUNTRIES
#Rich country 
rich_co2_frst_corr = co2_dataframe_years[rich_countries].corrwith(forest_dataframe_years[rich_countries])
#middle-income countries
middle_co2_frst_corr = co2_dataframe_years[middle_countries].corrwith(forest_dataframe_years[middle_countries])
# poor countries
poor_co2_frst_corr = co2_dataframe_years[poor_countries].corrwith(forest_dataframe_years[poor_countries])
#print conclusion
print("Correlation between forest area in KM and CO2 emissions for rich countries:")
print(rich_co2_frst_corr)
print("\nCorrelation between forest area in KM  and CO2 emissions for middle-income countries:")
print(middle_co2_frst_corr)
print("\nCorrelation between forest area in KM  and CO2 emissions for poor countries:")
print(poor_co2_frst_corr)
#%%
#CORRELATION BETWEEN CO2 AND URBAN POP IN RICH, MIDDLE AND POOR COUNTRIES
#Rich country 
rich_co2_urban_corr = co2_dataframe_years[rich_countries].corrwith(urban_dataframe_years[rich_countries])
#middle-income countries
middle_co2_urban_corr = co2_dataframe_years[middle_countries].corrwith(urban_dataframe_years[middle_countries])
# poor countries
poor_co2_urban_corr = co2_dataframe_years[poor_countries].corrwith(urban_dataframe_years[poor_countries])
#print conclusion
print("Correlation between Urban Population and CO2 emissions for rich countries:")
print(rich_co2_urban_corr)
print("\nCorrelation between Urban Population  and CO2 emissions for middle-income countries:")
print(middle_co2_urban_corr)
print("\nCorrelation between Urban Population  and CO2 emissions for poor countries:")
print(poor_co2_urban_corr)